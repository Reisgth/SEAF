from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']  # Ajuste o escopo conforme necessário

def authenticate_gmail():
    creds = None
    # Verifica se existe um token armazenado
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Se não houver credenciais válidas, o usuário precisa se autenticar manualmente
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Atualiza automaticamente o token usando o token de atualização
            creds.refresh(Request())
        else:
            # Realiza a autenticação manual na primeira vez
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para reutilização futura
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds