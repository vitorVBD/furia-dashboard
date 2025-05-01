import requests

def get_instagram_followed_pages(access_token, user_id):
    """
    Obtém as páginas seguidas por um usuário no Instagram usando a Graph API.
    """
    try:
        url = f"https://graph.facebook.com/v16.0/{user_id}/following"
        params = {
            "access_token": access_token,
            "fields": "username"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP

        data = response.json()
        followed_pages = [item['username'] for item in data.get('data', [])]
        return followed_pages

    except requests.exceptions.RequestException as e:
        print(f"Erro ao coletar páginas seguidas no Instagram: {e}")
        return []
    
def get_instagram_user_id(access_token):
    """
    Obtém o ID do usuário autenticado no Instagram usando a Graph API.
    """
    try:
        url = "https://graph.facebook.com/v16.0/me"
        params = {
            "access_token": access_token,
            "fields": "id,username"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP

        data = response.json()
        return data.get("id")  # Retorna o ID do usuário
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o ID do usuário no Instagram: {e}")
        return None