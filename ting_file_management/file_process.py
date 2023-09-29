from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    archive = txt_importer(path_file)
    archive_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(archive),
        "linhas_do_arquivo": archive,
    }

    if not instance.items:
        instance.enqueue(archive_process)
    else:
        if not any(item["nome_do_arquivo"] ==
                   path_file for item in instance.items):
            instance.enqueue(archive_process)

    print(archive_process, file=sys.stdout)

    # archive = txt_importer(path_file)
    # archive_process = {
    #     "nome_do_arquivo": path_file,
    #     "qtd_linhas": len(archive),
    #     "linhas_do_arquivo": archive,
    # }

    # if len(instance.items) == 0:
    #     instance.enqueue(archive_process)
    # else:
    #     for index in instance.items:
    #         if path_file != index["nome_do_arquivo"]:
    #             instance.enqueue(archive_process)

    # print(archive_process, file=sys.stdout)

    # file_name = path_file.split("/")[-1]
    # if any(item["nome_do_arquivo"] == file_name for item in instance.items):
    #     return

    # file_lines = txt_importer(path_file)

    # file_info = {
    #     "nome_do_arquivo": file_name,
    #     "qtd_linhas": len(file_lines),
    #     "linhas_do_arquivo": file_lines,
    # }

    # print(file_info, file=sys.stdout)


def remove(instance):
    if not instance.items:
        print("Não há elementos", file=sys.stdout)
    else:
        archive = instance.dequeue()
        print(f"Arquivo {archive['nome_do_arquivo']} removido com sucesso",
              file=sys.stdout)


def file_metadata(instance, position):
    try:
        archive = instance.search(position)
        print(archive, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
