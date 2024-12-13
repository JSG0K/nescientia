import os
import list
import downloader


def main():
    # Exibe o menu de opções para o usuário
    option = int(input('''
    O que deseja fazer?:
    1 - Baixar todas as listas atualizadas do GitHub.
    2 - Criar uma nova lista.
    3 - Atualizar o cabeçalho das listas existentes.

    Escolha uma opção (1, 2 ou 3): '''))

    # Verifica a opção escolhida pelo usuário
    if option == 1:
        # Chama a função para baixar todas as listas do GitHub
        downloader.download_all_lists_from_github()

    elif option == 2:
        # Chama a função para criar uma nova lista
        list.interactive()

    elif option == 3:
        # Solicita o caminho da lista ou a escolha de 'TODOS' para atualizar todas as listas
        answer = input(
            "Onde está localizada a sua lista (Path)?\n* Responda 'TODOS' para atualizar todas as listas no diretório 'lists'.\n\n: ")

        if answer.lower() in ['todos', 'todas']:
            # Se o usuário escolher 'TODOS', itera por todas as listas no diretório 'lists'
            path = os.path.join(os.getcwd(), "lists/")

            # Percorre todos os arquivos e diretórios dentro de 'lists' e atualiza o cabeçalho de cada lista .txt
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.txt'):
                        file_path = os.path.join(root, file)
                        # Chama a função para atualizar o cabeçalho de cada lista
                        list.update_header(file_path)

            # Mensagem informando que as listas foram atualizadas com sucesso
            print("As listas foram atualizadas com sucesso!")

        else:
            # Se o usuário fornecer um caminho específico, atualiza o cabeçalho da lista fornecida
            path = os.path.join(answer)
            # Chama a função para atualizar o cabeçalho da lista fornecida
            list.update_header(path)
            print("Lista atualizada com sucesso!")

    else:
        # Se o usuário escolher uma opção inválida, exibe uma mensagem de erro
        print("Opção inválida, tente novamente.")


# Bloco try/except para capturar a interrupção do teclado (Ctrl + C) em qualquer lugar do código
if __name__ == "__main__":
    try:
        main()  # Chama a função principal onde o programa é executado

    except KeyboardInterrupt:
        # Trata a interrupção do teclado (Ctrl + C)
        print("\nExecução interrompida pelo usuário. Saindo...")
        # Aqui você pode incluir qualquer outro comportamento desejado antes de encerrar, como salvar o estado ou limpar recursos.