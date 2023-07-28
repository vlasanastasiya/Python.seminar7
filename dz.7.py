# задание № 4. Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choices, randint
from string import ascii_lowercase, digits

def make_files(extension: str, min_name: int = 6, max_name: int = 30, min_size: int = 256, max_size: int = 4896, count: int = 42) -> None:
    for _ in range(count):
         name = ''.join(choices(ascii_lowercase + digits, k=randint(min_name, max_name)))
         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
         with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    make_files('bin', count = 1)

# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи

def make_file_2(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


if __name__ == '__main__':
     data = {'txt': 2, 'jpg': 3}
make_file_2(data)


# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён

from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits
from os import chdir

def make_files(extension: str, min_name: int = 6, max_name: int = 30, min_size: int = 256, max_size: int = 4896, count: int = 42) -> None:
    for _ in range(count):
         print(Path.cwd())
         while True:
             name = ''.join(choices(ascii_lowercase + digits, k=randint(min_name, max_name)))
             if not Path(f'{name},{extension}').is_file():
                 break
         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
         with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

def file_generate(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)
    for extension, count in kwargs.items():
        make_files(extension=extension, count=count, min_name=1, max_name=1)

if __name__ == '__main__':
    file_generate('C:/Users/selec/OneDrive/Рабочий стол/Файл', bin=2, jpg=2)


# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os

def rename_func(first_name, rank, source_ext, target_ext, range=None):
    list_of_files = [f.split(source_ext[0] for f in os.listdir('.')
                             if os.path.isfile(f) and f.endswith(source_ext))]
    if not list_of_files:
        print("Таких файлов нет")
        return
    for i, file in enumerate(file, 1):
        if range:
            start, end = range
            name = file[start - 1:end]
            new_name = name + first_name + f"{i:0{rank}}" + target_ext
            os.rename(f'{file}{source_ext}', new_name)
            print(f"rename file {file} in {new_name}")


rename_func("_new", 6, ".txt, ".doc", range=[3, 6])




