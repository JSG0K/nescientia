import os
from datetime import datetime, timezone


# Função para criar uma lista com as informações fornecidas
def create(platform, category, title, description, version, entries):
    # Obtém a data e hora atual em UTC
    date_now = datetime.now(timezone.utc)

    # Cria um dicionário com os dados da lista
    list_data = {
        "identifier": f'{category.capitalize()}-{platform.capitalize()}',
        "platform": platform,
        "category": category,
        "title": title,
        "description": description,
        "expires": "1 day",
        "last_modified": date_now.strftime("%d %b %Y %H:%M %Z"),
        "version": version,
        "syntax": "AdBlock",
        "number_of_entries": get_number_of_entries(entries),
        "entries": entries
    }
    return list_data


# Função para carregar uma lista a partir de um arquivo
def load(list_file):
    list_data = {}

    # Abre o arquivo para leitura
    with open(list_file, 'r') as file:
        entries = []

        # Processa cada linha do arquivo
        for line in file:
            # Processa as linhas de comentários (que começam com "! ")
            if line.startswith('! ') and ":" in line and "===" not in line:
                item = line.split(': ')[0].strip("! ").replace(" ", "_").lower()
                value = line.split(': ')[1].strip()
                list_data[item] = value
            # Processa as linhas com as entradas (que não são a linha "[Adblock Plus]")
            elif not line == "[Adblock Plus]\n" and not line == "\n" and not line.replace(" ", "") == "":
                entries.append(line)

        # Atribui as entradas da lista
        list_data["entries"] = entries

    # Atribui valores padrão caso algum campo não tenha sido definido no arquivo
    list_data.setdefault("platform", "Custom")
    list_data.setdefault("category", "Default")
    list_data.setdefault("title", "Default List Title")
    list_data.setdefault("description", "")
    list_data.setdefault("version", "v1.0")

    # Cria e retorna a lista com os dados carregados
    return create(
        list_data["platform"],
        list_data["category"],
        list_data["title"],
        list_data["description"],
        list_data["version"],
        list_data["entries"],
    )


# Função para salvar uma lista em um arquivo
def save(list_data, path):
    # Abre o arquivo para escrita
    with open(path, 'w') as file:
        # Escreve a seção de cabeçalho no arquivo
        file.write("[Adblock Plus]\n")
        file.write(
            "! Homepage: https://github.com/JSG0K/nescientia\n! License: https://github.com/JSG0K/nescientia/blob/main/LICENSE\n! Issues: https://github.com/JSG0K/nescientia/issues\n")

        # Escreve os dados da lista no formato esperado
        for key, value in list_data.items():
            if key == "entries":
                file.write("\n")
                for entry in list_data[key]:
                    file.write(entry)
            elif key != "identifier":  # Não escreve o identificador
                file.write(f'! {key.replace("_", " ").capitalize()}: {value}\n')


# Função para atualizar o cabeçalho do arquivo, incrementando a versão
def update_header(path):
    list_data = load(path)
    list_data["version"] = increase_version(list_data["version"])
    save(list_data, path)


# Função para contar o número de entradas na lista
def get_number_of_entries(entries):
    number_of_entries = 0
    # Conta as entradas que são válidas (não começam com "!" e contém "##" ou "|")
    for entry in entries:
        if not entry.startswith("!") and ("##" in entry or "|" in entry):
            number_of_entries += 1
    return number_of_entries


# Função para incrementar a versão de uma lista
def increase_version(version):
    # Divide a versão em duas partes e incrementa a segunda parte (versão secundária)
    version_number = int(version.split(".")[1].strip())
    new_version = f'{version.split(".")[0].strip()}.{version_number + 1}'
    return new_version


# Função interativa para criar uma nova lista
def interactive():
    # Solicita as informações ao usuário para criar a lista
    platform = input("Para qual plataforma será sua lista (Ex: Instagram)? ").capitalize()
    category = input("Qual é a categoria da sua lista (Ex: Finanças)? ").capitalize()
    title = input("Dê um título bem bonito para sua lista (use emojis!): ")
    description = input("Dê uma descrição bem sucinta para sua lista: ")

    print("Ótimo! Agora vamos configurar as keywords/regex para sua lista:\nDigite 'exit' para concluir.")
    entries = []
    i = 1
    while True:
        entry = input(f"Regex/Keyword ({i}): ")
        if entry.lower() == "exit":
            break

        entries.append(entry)
        i += 1

    # Define o caminho onde o arquivo será salvo
    path = os.path.join(os.getcwd(), f'lists/{category}/{category.capitalize()} ({platform}).txt')
    # Cria o diretório, caso não exista
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Cria a lista e a salva no arquivo
    list_data = create(platform, category, title, description, "v1.0", entries)
    save(list_data, path)

    print(f"Legal! Sua lista já foi criada e está acessível em: {path}")
