from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_txt = txt_importer(path_file)
    std_out = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_txt),
        "linhas_do_arquivo": file_txt
    }

    if std_out not in instance.data:
        instance.enqueue(std_out)
        print(std_out, file=sys.stdout)


def remove(instance):
    if len(instance.data) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        removed = instance.dequeue()["nome_do_arquivo"]
        print(f'Arquivo {removed} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
