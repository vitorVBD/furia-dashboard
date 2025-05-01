import pandas as pd
import streamlit as st
from datetime import datetime
from wordcloud import WordCloud
import json

# Importar funções necessárias
from utils.data_loader import load_data, load_fan_data
from utils.visualization import create_bar_chart, create_word_cloud, create_line_chart
from routes.auth import authenticate_twitter_v2
from services.instagram_service import get_instagram_followed_pages
from routes.auth import authenticate_instagram_graph

# Autenticar cliente do Twitter
client = authenticate_twitter_v2()

# Carregar dados
tweets = load_data("furia_tweets.json")  # Carregar tweets do arquivo JSON
fan_data = load_fan_data()

# Dashboard
st.title("🎯 Dashboard - FURIA Minimap")

# Exibir dados dos fãs
if fan_data:
    st.header("👥 Insights sobre fãs")
    st.write("Aqui estão os dados dos fãs da FURIA. Você pode visualizar todos os fãs que preencheram o form, além de outros insights.")
    df_fans = pd.DataFrame(fan_data)
    st.write("Total de fãs que preencheram o formulário:", len(df_fans))
    st.dataframe(df_fans)

    # Gráfico de distribuição por estado
    if 'Endereço' in df_fans.columns:
        state_counts = df_fans['Endereço'].apply(lambda x: x['Estado']).value_counts().reset_index()
        state_counts.columns = ['Estado', 'Quantidade']
        create_bar_chart(state_counts, 'Estado', 'Quantidade', "Distribuição de Fãs por Estado", {'Estado': 'Estado', 'Quantidade': 'Quantidade de Fãs'}, 'Quantidade')

    # Calcular a idade de cada fã
    df_fans['Idade'] = df_fans['Data de Nascimento'].apply(
        lambda dob: datetime.now().year - datetime.strptime(dob, "%d/%m/%Y").year
    )
    age_counts = df_fans['Idade'].value_counts().reset_index()
    age_counts.columns = ['Idade', 'Quantidade']
    create_bar_chart(age_counts, 'Idade', 'Quantidade', "Quantidade de Pessoas por Idade", {'Idade': 'Idade', 'Quantidade': 'Quantidade de Pessoas'}, 'Quantidade')

    # Calcular a média de idade por estado
    df_fans['Estado'] = df_fans['Endereço'].apply(lambda x: x['Estado'])
    avg_age_by_state = df_fans.groupby('Estado')['Idade'].mean().reset_index()
    avg_age_by_state.columns = ['Estado', 'Média de Idade']
    create_bar_chart(avg_age_by_state, 'Estado', 'Média de Idade', "Média de Idade por Estado", {'Estado': 'Estado', 'Média de Idade': 'Média de Idade'}, 'Média de Idade')

    # Word Cloud de interesses (extraido do formulário)
    interests = " ".join(df_fans['Interesses'].dropna().astype(str).tolist())
    create_word_cloud(interests)


# Dados extraidos do Twitter
# Exibir tweets com hashtags
if tweets:
    st.header("📊 Informações extraídas de Tweets dos fãs")
    st.write("Aqui estão os tweets extraídos dos fãs da FURIA. Você pode visualizar todos os tweets coletados, além de outros insights.")
    st.write("Total de tweets coletados:", len(tweets))
    df_tweets = pd.DataFrame(tweets)
    st.dataframe(df_tweets[['created_at', 'tweet_text', 'retweets', 'likes']])

    # Gráfico de engajamento por tweet
    avg_engagement = df_tweets[['retweets', 'likes']].mean().reset_index()
    avg_engagement.columns = ['Métrica', 'Média']
    create_bar_chart(avg_engagement, 'Métrica', 'Média', "Engajamento Médio por Tweet", {'Métrica': 'Métrica', 'Média': 'Média'}, 'Média')

    # Gráfico de engajamento por usuário
    fan_engagement = df_tweets['author_id'].value_counts().reset_index()
    fan_engagement.columns = ['Usuário', 'Quantidade de Tweets']
    create_bar_chart(fan_engagement, 'Usuário', 'Quantidade de Tweets', "Fãs Mais Engajados", {'Usuário': 'Usuário', 'Quantidade de Tweets': 'Quantidade de Tweets'}, 'Quantidade de Tweets')

    df_tweets['Data'] = pd.to_datetime(df_tweets['created_at']).dt.date
    daily_tweets = df_tweets.groupby('Data').size().reset_index(name='Quantidade')
    create_line_chart(daily_tweets, 'Data', 'Quantidade', "Evolução dos Tweets ao Longo do Tempo", {'Data': 'Data', 'Quantidade': 'Quantidade de Tweets'})

    # Identificar as palavras mais usadas nos tweets coletados
    all_words = " ".join(df_tweets['tweet_text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)
    st.image(wordcloud.to_array(), caption="Palavras Mais Usadas nos Tweets")

# Autenticar no Instagram
INSTAGRAM_ACCESS_TOKEN = st.secrets.get("INSTAGRAM_ACCESS_TOKEN")  # Adicione no arquivo .env

# Exibir contas relacionadas à FURIA no Instagram
if fan_data:
    st.header("📸 Contas no Instagram relacionadas à FURIA")

    # Carregar o arquivo JSON com as contas relacionadas à FURIA
    try:
        with open('furia_related_pages.json', 'r', encoding='utf-8') as f:
            furia_related_data = json.load(f)
    except FileNotFoundError:
        furia_related_data = {}

    for fan in fan_data:
        instagram_username = fan.get("Redes Sociais", {}).get("Instagram")
        if instagram_username:
            st.subheader(f"Contas seguidas por @{instagram_username}")
            furia_related_pages = furia_related_data.get(instagram_username, [])
            if furia_related_pages:
                st.write(f"Contas relacionadas à FURIA seguidas por @{instagram_username}:")
                st.write(furia_related_pages)
            else:
                st.write(f"Nenhuma conta relacionada à FURIA foi encontrada para @{instagram_username}.")