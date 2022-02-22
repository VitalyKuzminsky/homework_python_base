import os

root = r'C:\Users\01\Desktop\GeekBrains\I_quarter\Base_Python\HW\homework_python_base\Kuzminsky_Vitaly_dz_7'
folder_main = 'my_project'
project_tree = ['settings', 'authapp', 'adminapp', 'authapp']


def unpacking_project(root_in, folders):
    """Создаёт папки для проекта из переданного адреса проекта и списка папок"""
    if folders:
        for element in folders:
            new_way = os.path.join(root_in, element)
            if not os.path.exists(new_way):
                os.mkdir(new_way)


project = os.path.join(root, folder_main)
if not os.path.exists(project):
    os.mkdir(project)
unpacking_project(project, project_tree)
