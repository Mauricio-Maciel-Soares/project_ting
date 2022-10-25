def exists_word(word, instance):
    searched_data = list()

    for index in range(len(instance)):
        line_list = list()
        file = instance.search(index)

        for i, content in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in content.lower():
                line_list.append({"linha": i + 1})

        if (len(line_list) > 0):
            data = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": line_list
            }
            searched_data.append(data)

    return searched_data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
