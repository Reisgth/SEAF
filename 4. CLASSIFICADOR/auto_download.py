from googleapiclient.discovery import build
from fpdf import FPDF
import base64
import os
import pickle
import re
from google_auth_oauthlib.flow import InstalledAppFlow  # Certifique-se de que essa linha está presente
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def list_emails(service, user_id='me', max_results=10):
    results = service.users().messages().list(userId=user_id, maxResults=max_results).execute()
    messages = results.get('messages', [])
    return messages

def get_email_content(service, user_id, msg_id):
    message = service.users().messages().get(userId=user_id, id=msg_id, format='full').execute()
    payload = message['payload']
    headers = payload.get("headers", [])
    
    subject = ""
    for header in headers:
        if header["name"] == "Subject":
            subject = header["value"]
            break

    body = ""
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                data = part["body"].get('data')
                if data:
                    body = base64.urlsafe_b64decode(data).decode("utf-8")
                    break
    else:
        data = payload["body"].get('data')
        if data:
            body = base64.urlsafe_b64decode(data).decode("utf-8")
    
    return subject, body

def save_to_pdf(subject, content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Assunto: {subject}", ln=True, align='L')
    pdf.ln(10)  # Nova linha
    pdf.multi_cell(0, 10, txt=content)
    
    pdf.output(f"documentos_novos/{filename}")
    print(f"E-mail salvo como {filename}")

def main():
    service = build('gmail', 'v1', credentials=authenticate_gmail())  # Construir o serviço Gmail com as credenciais
    messages = list_emails(service)
    for msg in messages:
        msg_id = msg['id']
        subject, content = get_email_content(service, 'me', msg_id)
        if not content.strip():
            print(f"O e-mail com ID {msg_id} não tem conteúdo em texto.")
            continue
        # Remover caracteres inválidos do nome do arquivo
        subject_sanitized = re.sub(r'[<>:"/\\|?*]', '', subject)
        filename = f"{subject_sanitized[:50]}.pdf"  # Nome do arquivo baseado no assunto (cortado a 50 caracteres)
        save_to_pdf(subject, content, filename)

if __name__ == "__main__":
    main()