import os

import requests


# Função para baixar todas as listas do GitHub
def download_all_lists_from_github():
    # Lista de tuplas contendo o nome da lista e o URL correspondente
    lists = [
        ("Política (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Pol%C3%ADtica/Pol%C3%ADtica%20(Youtube).txt"),
        ("Geração Z (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Gera%C3%A7%C3%A3o%20Z/Gera%C3%A7%C3%A3o%20Z%20(Youtube).txt"),
        ("Coaches (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Coaches/Coaches%20(Youtube).txt"),
        ("Pseudociência (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Pseudoci%C3%AAncia/Pseudoci%C3%AAncia%20(Youtube).txt"),
        ("Conteúdo Sexual (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Cont%C3%A9udo%20Sexual/Cont%C3%A9udo%20Sexual%20(Youtube).txt"),
        ("Religião (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Religi%C3%A3o/Religi%C3%A3o%20(Youtube).txt"),
        ("Games (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Games/Games%20(Youtube).txt"),
        ("Bets (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Bets/Bets%20(Youtube).txt"),
        ("TikTok Major Influencers (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Tiktok%20Major%20Influencers/Tiktok%20Major%20Influencers%20(Youtube).txt"),
        ("Notícias (Youtube)",
         "https://raw.githubusercontent.com/JSG0K/nescientia/refs/heads/main/Not%C3%ADcias/Not%C3%ADcias%20(Youtube).txt")
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