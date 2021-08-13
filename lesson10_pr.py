################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
from string import ascii_lowercase as alphabet
import random

def create_dir(dir_name):
    os.makedirs(dir_name, exist_ok=True)
    # try:
    #     os.mkdir(dir_name)
    # except FileExistsError:
    #     pass


def create_file(dirname, symbol):
    filename = f"{dirname}/{symbol}.txt"
    with open(filename, "w") as file:
        file.write(alphabet.replace(symbol, symbol.upper()))


def create_files(dirname):
    for symbol in alphabet:
        create_file(dirname, symbol)

def do_tanos_click(dirname):
    files = os.listdir(dirname)
    random.shuffle(files)
    # files = list(set(files))
    for filename in files[:len(files) // 2]:
        os.remove(os.path.join(dirname, filename))



dirname = "alphabet"
create_dir(dirname)
create_files(dirname)
do_tanos_click(dirname)
