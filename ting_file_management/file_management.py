import sys
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    _, file_extension = os.path.splitext(path_file)
    if file_extension != ".txt":
        print("Formato inválido", file=sys.stderr)
        return []

    with open(path_file, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]
