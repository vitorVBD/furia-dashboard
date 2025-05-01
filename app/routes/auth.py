import os
import tweepy
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Bearer Token
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Função para autenticar na API do Twitter (API v2)
def authenticate_twitter_v2():
    if not BEARER_TOKEN:
        raise ValueError("Bearer Token não configurado. Verifique o arquivo .env.")
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    return client

# Carregar variáveis de ambiente
INSTAGRAM_APP_ID = os.getenv("INSTAGRAM_APP_ID")
INSTAGRAM_APP_SECRET = os.getenv("INSTAGRAM_APP_SECRET")
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")

# Autenticar no Instagram usando a Graph API
def authenticate_instagram_graph():
    if not INSTAGRAM_ACCESS_TOKEN:
        raise ValueError("Access Token do Instagram não configurado. Verifique o arquivo .env.")
    return INSTAGRAM_ACCESS_TOKEN