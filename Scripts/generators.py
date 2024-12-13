def youtube(keywords):
    # Lista que irá armazenar as entradas geradas
    entries = []

    # Dicionário contendo os elementos do YouTube e seus respectivos comentários
    youtube_elements = {
        '#related ytd-compact-video-renderer': 'Videos in related bar',
        'ytd-shelf-renderer': 'Shorts',
        'ytd-video-renderer': 'Videos in general',
        'ytd-rich-item-renderer': 'Shorts',
        'ytd-channel-renderer': 'Channel',
        'ytd-reel-shelf-renderer': 'Shorts'
    }

    # Itera sobre cada palavra-chave fornecida
    for keyword in keywords:
        # Itera sobre os elementos e comentários do dicionário
        for element, comment in youtube_elements.items():
            # Adiciona o comentário sobre o tipo de conteúdo
            entries.append(f'!{comment}\n')

            # Cria a entrada do AdBlock com base no elemento e na palavra-chave
            # A entrada é formatada para remover o conteúdo que contém a palavra-chave
            entries.append(f'youtube.com##{element}:has-text({keyword}):remove()\n')

    # Retorna a lista de entradas geradas
    return entries