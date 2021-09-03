################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
from string import ascii_lowercase as alphabet
import random
import json


class AlphabetDirFiles:
    def __init__(self, dirname):
        self._dirname = dirname
        self._create_dir()

    def _create_dir(self):
        os.makedirs(self._dirname, exist_ok=True)

    def _create_file(self, symbol):
        filename = f"{self._dirname}/{symbol}.txt"
        with open(filename, "w") as file:
            file.write(alphabet.replace(symbol, symbol.upper()))

    def create_files(self):
        for symbol in alphabet:
            self._create_file(symbol)

    def do_tanos_click(self):
        files = os.listdir(self._dirname)
        random.shuffle(files)
        for filename in files[:len(files) // 2]:
            os.remove(os.path.join(self._dirname, filename))


dirname = "alphabet"
worker = AlphabetDirFiles(dirname)
# worker._dirname = "tmp"

worker.create_files()

# worker.do_tanos_click()
