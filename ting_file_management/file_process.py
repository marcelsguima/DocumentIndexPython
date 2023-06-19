from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)

    list_data = [
        instance.search(i)["nome_do_arquivo"] for i in range(len(instance))
    ]

    if path_file not in list_data:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }

        instance.enqueue(file_data)
        sys.stdout.write(str(file_data))


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return None

    data = instance.dequeue()
    print(
        f"Arquivo {data['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout
    )


def file_metadata(instance, position):
    if not instance or position < 0 or position >= len(instance):
        sys.stderr.write("Posição inválida")
        return None

    data = instance.search(position)
    print(data)
    return data
