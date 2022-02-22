import os
import shutil


def data_collection(path: str, name: str, format_file: str):
    """
    Создаёт структуру дерева папок и копирует файлы заданного формата
    :param path: str -- путь, где будет формироваться дерево папок
    :param name: str -- базовая папка
    :param format_file: str -- тип формата файла, которые
    :return:
    """
    way_files = {}
    folders_new = []
    for ways, folders, files in os.walk(path):
        for el in files:
            if el.endswith(f'.{format_file}'):
                template = os.path.join(*ways.split(os.sep)[-1:])
                if template not in way_files:
                    folders_new.append(os.path.join(path, name, template))

                way_files.update({os.path.join(ways, el): os.path.join(path, name, template, el)})

    if not os.path.exists(os.path.join(path, name)):
        os.mkdir(os.path.join(path, name))

    for folder in folders_new:
        if not os.path.exists(folder):
            os.mkdir(folder)

    for base, add in way_files.items():
        if not os.path.exists(add):
            shutil.copy(base, add)


data_collection('my_project', 'templates', 'html')
