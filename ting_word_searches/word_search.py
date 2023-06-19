def exists_word(word, instance):
    words = []

    for data in range(len(instance)):
        file_info = instance.search(data)
        file_name = file_info["nome_do_arquivo"]
        file_lines = file_info["linhas_do_arquivo"]

        total_words = []
        for current, line in enumerate(file_lines):
            if word.lower() in line.lower():
                total_words.append({"linha": current + 1})

        if total_words:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": total_words,
            }
            words.append(result)
    return words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
