import os
import pandas as pd
from dotenv import load_dotenv
import json

# Carregar variáveis de ambiente
load_dotenv()

# Bearer Token
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Função para salvar tweets filtrados no arquivo JSON
def save_filtered_tweets(tweets, filename):
    try:
        # Carregar tweets existentes no arquivo
        existing_tweets = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                existing_tweets = json.load(file)

        # Adicionar novos tweets ao arquivo
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_tweets + tweets, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar tweets no arquivo {filename}: {e}")

# Coleta de tweets de um perfil específico
def collect_tweets_with_hashtags(client, username, hashtags, max_results=10):
    try:
        # Buscar o usuário pelo nome de usuário
        user = client.get_user(username=username)
        if not user.data:
            raise ValueError(f"Usuário {username} não encontrado.")

        user_id = user.data.id

        # Buscar tweets do usuário
        tweets = client.get_users_tweets(
            id=user_id,
            max_results=max_results,
            tweet_fields=["created_at", "public_metrics", "text"]
        )

        tweet_data = []
        if tweets.data:
            for tweet in tweets.data:
                # Filtrar tweets que contenham as hashtags
                if any(f"#{hashtag.lower()}" in tweet.text.lower() for hashtag in hashtags):
                    tweet_data.append({
                        "tweet_id": tweet.id,
                        "created_at": tweet.created_at,
                        "tweet_text": tweet.text,
                        "retweets": tweet.public_metrics['retweet_count'],
                        "likes": tweet.public_metrics['like_count']
                    })

        # Salvar os tweets filtrados no arquivo JSON
        save_filtered_tweets(tweet_data, "furia_tweets.json")

        return tweet_data[:max_results]  # Retornar no máximo 'max_results' tweets
    except Exception as e:
        print(f"Erro ao processar tweets para o usuário {username}: {e}")
        return []
    
def save_filtered_tweets(tweets, filename):
    try:
        # Carregar tweets existentes no arquivo
        existing_tweets = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                existing_tweets = json.load(file)

        # Adicionar novos tweets ao arquivo
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_tweets + tweets, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar tweets no arquivo {filename}: {e}")

# Coleta de tweets de múltiplos fãs
def collect_tweets_from_fans(client, fan_data, hashtags, max_results=10):
    engagement_data = []
    for fan in fan_data:
        username = fan.get("Twitter")
        if username:
            # Coletar tweets com hashtags específicas
            tweets = collect_tweets_with_hashtags(client, username, hashtags, max_results=max_results)
            if tweets:
                df_tweets = pd.DataFrame(tweets)
                total_retweets = df_tweets['retweets'].sum()
                total_likes = df_tweets['likes'].sum()
                engagement_data.append({
                    'Perfil': f"@{username}",
                    'Total Retweets': total_retweets,
                    'Total Likes': total_likes,
                    'Tweets': tweets
                })
    return engagement_data