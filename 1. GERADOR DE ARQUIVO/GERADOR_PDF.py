from fpdf import FPDF

# Criar um novo PDF para os documentos
documents = FPDF()

# Função para adicionar documentos ao PDF
def add_docs(categoria, assunto, corpo):
    documents.add_page()
    documents.set_font("Arial", size=12)
    documents.cell(200, 10, txt=f"Categoria: {categoria}", ln=True, align="C")
    documents.ln(10)
    documents.multi_cell(0, 10, txt=f"Assunto: {assunto}\n\n{corpo}")

# Lista de documentos (categoria, assunto, corpo)
documentos = [
    ("RH/PESSOAL", "Solicitação de Alteração de Benefício de Saúde",
     "Prezada Equipe de RH,\n\nGostaria de solicitar a alteração do meu plano de saúde para a categoria premium, conforme discutido na última reunião.\n\nAtenciosamente,\nJoana Pereira\nAnalista de Projetos"),
    ("ALMOXARIFADO", "Pedido de Reposição de Materiais de Escritório",
     "Prezada Equipe do Almoxarifado,\n\nSolicitamos a reposição de materiais de escritório, como papéis A4, canetas e clipes, para o setor de atendimento.\n\nAtenciosamente,\nCarlos Oliveira\nAssistente Administrativo"),
    ("MARKETING", "Sugestão de Parceria com Agência de Publicidade",
     "Prezada Diretoria,\n\nEncaminho a proposta de parceria com a Agência XYZ para a criação de campanhas digitais e redes sociais.\n\nAtenciosamente,\nAna Cláudia\nEspecialista em Publicidade"),
    ("INFORMÁTICA", "Relatório de Atualização do Servidor Interno",
     "Prezada Equipe,\n\nSegue o relatório de atualização do servidor interno realizado no último fim de semana. Informamos que o sistema está estável e seguro.\n\nAtenciosamente,\nRicardo Alves\nAnalista de Sistemas"),
    ("CONTAS A PAGAR", "Solicitação de Pagamento de Fatura de Serviços de TI",
     "Prezada Equipe de Contas a Pagar,\n\nEncaminho a fatura referente aos serviços prestados pela empresa de TI. O vencimento é em 25/11/2024.\n\nAtenciosamente,\nFernanda Souza\nCoordenadora de TI"),
    ("RH/PESSOAL", "Pedido de Férias",
     "Prezada Equipe de RH,\n\nGostaria de formalizar meu pedido de férias no período de 15/01/2025 a 31/01/2025. Agradeço a confirmação.\n\nAtenciosamente,\nMarcos Lima\nAnalista de Qualidade"),
    ("ALMOXARIFADO", "Solicitação de Compra de Equipamentos de Limpeza",
     "Prezada Equipe do Almoxarifado,\n\nNecessitamos da compra de novos equipamentos de limpeza, incluindo rodos, vassouras e baldes, para o setor de manutenção.\n\nAtenciosamente,\nPaula Mendes\nSupervisora de Serviços Gerais"),
    ("MARKETING", "Plano de Publicidade para Novos Produtos",
     "Prezada Equipe de Marketing,\n\nEncaminho o plano de publicidade para os novos produtos a serem lançados no próximo trimestre, com foco em campanhas digitais.\n\nAtenciosamente,\nLucas Carvalho\nGerente de Produto"),
    ("INFORMÁTICA", "Problema Técnico no Sistema de Gestão",
     "Prezada Equipe de TI,\n\nEstamos enfrentando problemas de lentidão no sistema de gestão. Solicitamos uma verificação urgente para evitar atrasos no trabalho.\n\nAtenciosamente,\nPatrícia Lima\nCoordenadora de Projetos"),
    ("CONTAS A PAGAR", "Pedido de Antecipação de Pagamento a Fornecedor",
     "Prezada Equipe de Contas a Pagar,\n\nGostaria de solicitar a antecipação do pagamento ao fornecedor XYZ para garantir o cumprimento do contrato.\n\nAtenciosamente,\nGuilherme Costa\nSupervisor de Compras"),
]

# Adicionar cada documento ao PDF
for doc in documentos:
    add_docs(doc[0], doc[1], doc[2])

# Salvar o PDF
documents.output("documentos.pdf")