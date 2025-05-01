import streamlit as st
import json
import os
from datetime import datetime
import re
import requests
import pytesseract
from PIL import Image
import fitz
from app.services.instagram_service import get_instagram_followed_pages, get_instagram_user_id

# Configurar o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para validar o documento usando OCR ou extração direta de texto
def validate_document(document_path, expected_name, expected_cpf):
    try:
        extracted_text = ""

        # Verificar se o arquivo é um PDF
        if document_path.endswith('.pdf'):
            # Abrir o PDF e extrair texto de todas as páginas
            with fitz.open(document_path) as pdf:
                for page in pdf:
                    extracted_text += page.get_text()
        else:
            # Abrir o documento como imagem
            image = Image.open(document_path)
            extracted_text = pytesseract.image_to_string(image, lang='por')

        # Validar nome e CPF no texto extraído
        name_valid = expected_name.lower() in extracted_text.lower()
        cpf_valid = re.search(rf"{expected_cpf[:3]}\.?{expected_cpf[3:6]}\.?{expected_cpf[6:9]}-?{expected_cpf[9:]}", extracted_text)

        return name_valid, bool(cpf_valid)
    except Exception as e:
        print(f"Erro ao validar documento: {e}")
        return False, False

# Função para extrair o nome de usuário do Twitter
def extract_twitter_username(twitter_link):
    match = re.search(r"twitter\.com/([a-zA-Z0-9_]+)", twitter_link)
    if match:
        return match.group(1)
    return None

# Função para formatar a data no formato brasileiro
def format_date_brazilian(date):
    return date.strftime('%d/%m/%Y')

# Função para salvar os dados do formulário em um arquivo JSON
def save_form_data(form_data, file_path='fan_data.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    data.append(form_data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Titulo
st.title('Formulário de Fã - FURIA Minimap')

# Formulário
with st.form(key='fan_form'):
    st.header("Informações Pessoais")
    name = st.text_input('Nome completo')
    dob = st.date_input(
        'Data de Nascimento',
        min_value=datetime(1900, 1, 1),
        max_value=datetime.today(),
        value=datetime(2010, 1, 1)
    )
    cpf = st.text_input('CPF', max_chars=11, placeholder="Digite apenas números")
    if cpf and (not cpf.isdigit() or len(cpf) != 11):
        st.error("O CPF deve conter exatamente 11 números.")

    st.header("Endereço")
    cep = st.text_input("Digite seu CEP:", max_chars=8, placeholder="Apenas números")
    
    # Botão para buscar o cep
    buscar_cep = st.form_submit_button("Buscar CEP")

    street = st.text_input("Rua:", value=st.session_state.get("street", ""))
    number = st.text_input("Número:")
    complemento = st.text_input("Complemento:", placeholder="Apto, Bloco, etc.")
    neighboorhood = st.text_input("Bairro:", value=st.session_state.get("neighboorhood", ""))
    city = st.text_input("Cidade:", value=st.session_state.get("city", ""))
    state = st.text_input("Estado:", value=st.session_state.get("state", ""))

    st.header("Contato")
    phone = st.text_input('Telefone', max_chars=11, placeholder="Digite apenas números")
    email = st.text_input('Email')

    st.header("Interesses e Atividades")
    interests = st.text_area('Quais são seus interesses relacionados a esports?')
    activities = st.text_area('Quais atividades de esports você participou no último ano?')
    events = st.text_area('Quais eventos de esports você assistiu ou participou?')
    purchases = st.text_area('Compras relacionadas a esports (produtos, ingressos, etc)?')

    st.header("Documentação")
    document = st.file_uploader('Faça upload de uma imagem do seu documento (RG, CPF ou CNH)', type=['png', 'jpg', 'jpeg', 'pdf'])

    st.header("Redes Sociais")
    # Solicitar o nome de usuário do Instagram
    instagram_username = st.text_input('Informe seu nome de usuário do Instagram (opcional)')
    # Solicitar o nome de usuário do Twitter
    twitter_username = st.text_input('Informe seu nome de usuário do Twitter (sem o @)')
    # Possibilidade de pedir para o próprio fã informar as hashtags que costuma usar para falar sobre a FURIA:
    hashtags = st.text_area('Quais hashtags você costuma usar nos seus tweets? (separadas por vírgula)')

    submit_button = st.form_submit_button('Enviar')

# Fora do form: ações de botão
if buscar_cep and cep and len(cep) == 8 and cep.isdigit():
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            st.session_state["street"] = data.get("logradouro", "")
            st.session_state["neighboorhood"] = data.get("bairro", "")
            st.session_state["city"] = data.get("localidade", "")
            st.session_state["state"] = data.get("uf", "")
            st.success("Endereço preenchido automaticamente!")
        else:
            st.error("CEP não encontrado.")
    else:
        st.error("Erro ao buscar o CEP. Tente novamente.")

# Salvar os dados do formulário
if submit_button:
    formatted_dob = format_date_brazilian(dob)

    # Buscar contas relacionadas à FURIA no Instagram
    furia_related_pages = []
    if instagram_username:
        INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
        if INSTAGRAM_ACCESS_TOKEN:
            # Obter o ID do usuário real usando a API
            instagram_user_id = get_instagram_user_id(INSTAGRAM_ACCESS_TOKEN)
            if instagram_user_id:
                followed_pages = get_instagram_followed_pages(INSTAGRAM_ACCESS_TOKEN, instagram_user_id)
                furia_related_pages = [page for page in followed_pages if "furia" in page.lower()]
            else:
                st.error("Não foi possível obter o ID do usuário no Instagram.")

    form_data = {
        'Nome': name,
        'Data de Nascimento': formatted_dob,
        'CPF': cpf,
        'Endereço': {
            'CEP': cep,
            'Rua': street,
            'Número': number,
            'Complemento': complemento,
            'Bairro': neighboorhood,
            'Cidade': city,
            'Estado': state,
        },
        'Telefone': phone,
        'Email': email,
        'Interesses': interests,
        'Atividades': activities,
        'Eventos': events,
        'Compras': purchases,
        'Redes Sociais': {
            'Instagram': instagram_username,
            'FuriaRelatedPages': furia_related_pages,  # Adiciona as contas relacionadas à FURIA
            'Twitter': twitter_username,
            'Hashtags': [hashtag.strip() for hashtag in hashtags.split(",") if hashtag.strip()],
        },
    }

    save_form_data(form_data)
    st.success('Formulário enviado com sucesso!')

    if document is not None:
        # Salvar o documento enviado
        document_path = os.path.join('uploads', f"{name.replace(' ', '_')}_{document.name}")
        os.makedirs('uploads', exist_ok=True)
        with open(document_path, 'wb') as f:
            f.write(document.getbuffer())
        st.success('Documento enviado com sucesso!')

    # Salvar as contas relacionadas à FURIA em um arquivo separado
    if furia_related_pages:
        with open('furia_related_pages.json', 'w', encoding='utf-8') as f:
            json.dump({instagram_username: furia_related_pages}, f, ensure_ascii=False, indent=4)

    # Validar o documento usando AI
    name_valid, cpf_valid = validate_document(document_path, name, cpf)
    if name_valid and cpf_valid:
        st.success("Documento validado com sucesso! Nome e CPF correspondem.")
    else:
        if not name_valid:
            st.error("O nome informado não foi encontrado no documento.")
        if not cpf_valid:
            st.error("O CPF informado não foi encontrado no documento.")
