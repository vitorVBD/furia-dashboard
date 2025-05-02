<p align="center">
  <img src="./assets/Furia_Esports_logo.png" alt="FURIA logo" width="150" /> <br />
  <b>FURIA Minimap</b> <br />
  <sub><sup><b>(FURIA-DASHBOARD)</b></sup></sub> <br />
</p>

<p align="center">
  Este projeto é uma aplicação interativa desenvolvida para coletar, analisar e exibir dados relacionados aos fãs da FURIA Esports, suas interações nas redes sociais e insights sobre quem acompanha o cenário competitivo de esports. A aplicação utiliza Python, Streamlit e APIs de redes sociais como Twitter e Instagram.
</p>

<p align="center">
  This project is an interactive application designed to collect, analyze, and display data related to FURIA Esports fans, their social media interactions, and insights about who is engaged in competitive esports scene. The application uses Python, Streamlit, and social media APIs like Twitter and Instagram.
</p>

---

<details> <summary>🇧🇷 Detalhes do Projeto (Português)</summary>

## Resumo do Projeto

O **FURIA Minimap** é uma aplicação web que permite coletar e visualizar dados sobre os fãs da FURIA Esports. Ele analisa interações no Twitter e Instagram, exibe insights demográficos e comportamentais, e permite a criação de gráficos e relatórios interativos.

---

## Estrutura do Projeto

### Principais Arquivos

- **`dashboard.py`**: Interface principal para exibição de dados e insights.
- **`fan_form.py`**: Formulário para coleta de informações dos fãs.
- **`instagram_service.py`**: Funções para integração com a API do Instagram.
- **`twitter_service.py`**: Funções para integração com a API do Twitter.
- **`data_loader.py`**: Funções para carregar dados de arquivos JSON.
- **`visualization.py`**: Funções para criar gráficos interativos.

---

## Funcionalidades

- **Coleta de Dados**:
  - Informações demográficas e interesses dos fãs.
  - Interações no Twitter e Instagram.
- **Análise de Dados**:
  - Gráficos de engajamento por estado, idade e hashtags.
  - Word Cloud de interesses e hashtags.
- **Integração com Redes Sociais**:
  - Coleta de tweets e contas seguidas no Instagram relacionadas à FURIA.
- **Dashboard Interativo**:
  - Visualização de dados em tempo real.

---

## Tecnologias e Ferramentas Utilizadas

- **Python**: Linguagem principal para backend e análise de dados.
- **Streamlit**: Framework para criação de dashboards interativos.
- **Tweepy**: Biblioteca para integração com a API do Twitter.
- **Instagram Graph API**: API oficial para integração com o Instagram.
- **Pandas**: Manipulação e análise de dados.
- **Matplotlib e Plotly**: Criação de gráficos interativos.
- **WordCloud**: Geração de nuvens de palavras.

---

## Instruções de Uso

### Pré-requisitos

- Python 3.10+ instalado.
- Chaves de API configuradas no arquivo `.env`.

### Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/furia-dashboard.git
   cd furia-dashboard
   ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Crie e Configure o arquivo `.env` na raiz do projeto com suas chaves de API:
    ```bash
    # Twitter API
    # https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
    TWITTER_API_KEY=your_api_key
    TWITTER_API_KEY_SECRET=your_api_key_secret
    TWITTER_BEARER_TOKEN=your_bearer_token
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

    # Instagram API
    # https://developers.facebook.com/docs/instagram-basic-display-api/getting-started
    INSTAGRAM_APP_ID=seu_app_id
    INSTAGRAM_APP_SECRET=seu_app_secret
    INSTAGRAM_ACCESS_TOKEN=seu_access_token
    ```

4. Inicie, preencha e salve o formulário:
    ```bash
    streamlit run fan_form.py
    ```

5. Inicie o aplicativo:
    ```bash
    streamlit run app/dashboard.py
    ```

---

## Exemplos de Uso

### Formulário de Fãs:
Preencha o formulário em `fan_form.py` para coletar informações dos fãs.

### Dashboard:
Acesse o dashboard em `app/dashboard.py` para visualizar insights e gráficos.

### Integração com Redes Sociais:
Veja as contas relacionadas à FURIA seguidas no Instagram e tweets com hashtags específicas.

---

</details>

<details> <summary>🇺🇸 Project Details (English)</summary>

## Project Summary

The **FURIA Minimap** is a web application that collects and visualizes data about FURIA Esports fans. It analyzes interactions on Twitter and Instagram, displays demographic and behavioral insights, and allows the creation of interactive charts and reports.

---

## Key Files

- **`dashboard.py`**: Main interface for data visualization and insights.
- **`fan_form.py`**: Form to collect fan information.
- **`instagram_service.py`**: Functions for Instagram API integration.
- **`twitter_service.py`**: Functions for Twitter API integration.
- **`data_loader.py`**: Functions to load data from JSON files.
- **`visualization.py`**: Functions to create interactive charts.

---

## Features

### Data Collection:
- Demographic and interest information from fans.
- Interactions on Twitter and Instagram.

### Data Analysis:
- Engagement charts by state, age, and hashtags.
- Word Cloud of interests and hashtags.

### Social Media Integration:
- Collect tweets and Instagram accounts related to FURIA.

### Interactive Dashboard:
- Real-time data visualization.

---

## Technologies and Tools Used

- **Python**: Main language for backend and data analysis.
- **Streamlit**: Framework for creating interactive dashboards.
- **Tweepy**: Library for Twitter API integration.
- **Instagram Graph API**: Official API for Instagram integration.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib and Plotly**: Interactive chart creation.
- **WordCloud**: Word cloud generation.

---

## Usage Instructions

### Prerequisites
- Python 3.10+ installed.
- API keys configured in the `.env` file.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/furia-dashboard.git
   cd furia-dashboard
   ```

2. Create a virtual environment and install the dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Create and Configure the `.env` file with your API keys in the root file:
    ```bash
    # Twitter API
    # https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
    TWITTER_API_KEY=your_api_key
    TWITTER_API_KEY_SECRET=your_api_key_secret
    TWITTER_BEARER_TOKEN=your_bearer_token
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

    # Instagram API
    # https://developers.facebook.com/docs/instagram-basic-display-api/getting-started
    INSTAGRAM_APP_ID=seu_app_id
    INSTAGRAM_APP_SECRET=seu_app_secret
    INSTAGRAM_ACCESS_TOKEN=seu_access_token
    ```

4. Start, fill out, and save the form:
    ```bash
    streamlit run fan_form.py
    ```

5. Start the application:
    ```bash
    streamlit run app/dashboard.py
    ```

---

## Examples of Use

### Fan Form:
Fill out the form in `fan_form.py` to collect fan information.

### Dashboard:
Access the dashboard in `app/dashboard.py` to view insights and charts.

### Social Media Integration:
See Instagram accounts related to FURIA and tweets with specific hashtags.

</details>

---

## Licence

This software is licensed under the terms of the MIT License.

---

<div align="center">

Developed by Vitor Bittencourt ☕

</div> 