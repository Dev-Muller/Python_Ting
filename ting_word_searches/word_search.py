def exists_word(word, instance):
    results = []

    for item in range(len(instance)):
        occurrences = []
        file = instance.search(item)
        for index, line in enumerate(file["linhas_do_arquivo"], start=1):
            # ou ao inves de start=1 pode ser apenas o numero
            if word.lower() in line.lower():
                occurrences.append({"linha": index})
        if len(occurrences) > 0:
            results.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })
    return results


def search_by_word(word, instance):
    results = []

    for item in range(len(instance)):
        occurrences = []
        file = instance.search(item)
        for index, line in enumerate(file["linhas_do_arquivo"], 1):
            # ou ao inves de start=1 pode ser apenas o numero
            if word.lower() in line.lower():
                occurrences.append({"linha": index, "conteudo": line})
        if len(occurrences) > 0:
            results.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })
    return results
