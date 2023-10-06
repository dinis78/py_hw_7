#  Напишите функцию группового переименования файлов. Она должна:
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

def group_rename_files(desired_name, num_digits, original_extension, final_extension, name_renge = None):
    # получение файлов в каталоге
    files = os.listdir()
    # фильтрация с расширением original_extension
    files = [file for file in files if os.path.isfile(file) and file.endswith(original_extension)]
    # счетчик
    counter = 1
    for file in sorted(files):
        filename = os.path.splitext(file)[0]
        if name_renge:
            filename = filename[name_renge[0] -1: name_renge[1]]
        # новое имя
        new_name = f'{desired_name} {counter:0{num_digits}} {final_extension}'

        # переименование
        os.rename(file, new_name)
        counter += 1

















































