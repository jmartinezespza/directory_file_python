import os
import errno
from distutils.dir_util import copy_tree

import logging

particular_dir_path = '/Users/jhonny/odoo/odoo16/odoo/addons'
global_dir_path = '/Users/jhonny/odoo/odoo16/enterprise_demo/odoo-16.0+e.20230816/odoo/addons'
global_file_name = "global_dir_names.txt"
particular_file_name = "particular_dir_names.txt"
diff_file_name = "diff_dir_names.txt"

def get_diff_dir_name_list(global_dir_name_list, particular_dir_name_list):
    global_list = global_dir_name_list
    particular_list = particular_dir_name_list
    for name in particular_list:
        try:
            global_list.remove(name)
        except ValueError:
            print("No existe el directorio %s"%name)
    return global_list

def create_names_list_file(names_list, file_name):
    names_list = ["\n%s"%name for name in names_list]
    with open(file_name, 'w') as fp:
        fp.writelines(names_list)

def copy_directory_diff(source_dir, to_copy_list):
    try:
        os.mkdir('diff')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    n = 0
    for name in to_copy_list:
        n += 1
        print("(%s) Copiando %s ..."%(n, name))
        copy_tree("%s/%s"%(source_dir, name), "./diff/%s"%name)

def main():
    print("Directorio global: %s"%global_dir_path)
    global_dir_path_input = input("Ingrese la ruta completa (presione enter para mantener el valor por defecto): \n") or global_dir_path
    # global_dir_path_input = global_dir_path
    print("Directorio particular: %s"%particular_dir_path)
    particular_dir_path_input = input("Ingrese la ruta completa (presione enter para mantener el valor por defecto): \n") or particular_dir_path
    # particular_dir_path_input = particular_dir_path

    global_dir_name_list = [name for name in os.listdir(global_dir_path_input) if os.path.isdir("%s/%s"%(global_dir_path_input, name))]
    particular_dir_name_list = [name for name in os.listdir(particular_dir_path_input) if os.path.isdir("%s/%s"%(particular_dir_path_input, name))]
    # print("Listado: %s"%global_dir_name_list)

    create_names_list_file(global_dir_name_list, global_file_name)
    create_names_list_file(particular_dir_name_list, particular_file_name)

    diff_dir_name_list = get_diff_dir_name_list(global_dir_name_list, particular_dir_name_list)
    create_names_list_file(diff_dir_name_list, diff_file_name)

    print("Se crearon los siguientes archivos:\n")
    print(os.path.abspath(global_file_name))
    print(os.path.abspath(particular_file_name))
    print(os.path.abspath(diff_file_name))

    copy_directory_diff(global_dir_path_input, diff_dir_name_list)

if __name__ == "__main__":
    main()