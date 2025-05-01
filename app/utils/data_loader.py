import json
import streamlit as st

# Função para carregar os dados de tweets
def load_data(filename="furia_tweets.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            st.info(f"Dados carregados com sucesso de {filename}.")
            return data
    except FileNotFoundError:
        st.warning(f"Arquivo {filename} não encontrado.")
        return []
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo {filename}. Verifique o formato.")
        return []

# Função para carregar os dados dos fãs
def load_fan_data(file_path='fan_data.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.warning(f"Arquivo {file_path} não encontrado.")
        return []
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo {file_path}. Verifique o formato.")
        return []