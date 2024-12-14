import os

import requests


# Função para baixar todas as listas do GitHub
def download_all_lists_from_github():
    # Lista de tuplas contendo o nome da lista e o URL correspondente
    lists = [
        ("Política (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Pol%C3%ADtica/Pol%C3%ADtica%20(YouTube).txt"),
        ("Geração Z (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Gera%C3%A7%C3%A3o%20Z/Gera%C3%A7%C3%A3o%20Z%20(YouTube).txt"),
        ("Coaches (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Coaches/Coaches%20(YouTube).txt"),
        ("Pseudociência (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Pseudoci%C3%AAncia/Pseudoci%C3%AAncia%20(YouTube).txt"),
        ("Conteúdo Adulto (YouTube)",
         "https://github.com/JSG0K/nescientia/blob/main/Conte%C3%BAdo%20Adulto/Conte%C3%BAdo%20Adulto%20(YouTube).txt"),
        ("Religião (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Religi%C3%A3o/Religi%C3%A3o%20(YouTube).txt"),
        ("Games (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Games/Games%20(YouTube).txt"),
        ("Bets (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Bets/Bets%20(YouTube).txt"),
        ("TikTok Major Influencers (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/TikTok%20Major%20Influencers/TikTok%20Major%20Influencers%20(YouTube).txt"),
        ("Notícias (YouTube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Not%C3%ADcias/Not%C3%ADcias%20(YouTube).txt")
    ]

    # Itera sobre cada lista para baixar
    for list_name, list_url in lists:
        # Extrai a categoria a partir do nome da lista
        category = list_name.split(" (")[0].strip()

        # Cria o caminho para salvar o arquivo
        list_path = os.path.join(os.getcwd(), f"lists/{category}/{list_name}.txt")

        # Cria o diretório para salvar o arquivo, se não existir
        os.makedirs(os.path.dirname(list_path), exist_ok=True)

        # Faz o download do conteúdo da URL
        try:
            response = requests.get(list_url)

            # Verifica se a requisição foi bem-sucedida (status code 200)
            if response.status_code == 200:
                # Salva o conteúdo no arquivo
                with open(list_path, "w") as file:
                    file.write(response.text)
                print(f"Lista {list_name} baixada com sucesso!")
            else:
                # Caso a requisição falhe, exibe o código de erro
                print(f"Falha ao baixar a lista {list_name}. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Trata exceções de rede ou problemas com a requisição
            print(f"Erro ao tentar baixar a lista {list_name}. Detalhes do erro: {e}")