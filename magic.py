#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


def compile_run():  
    ''' 
    py turn to pyc
    '''  
    compileall.compile_dir(r'./')


def change_name(path, parent_path):
    #print('In change_name')
    #print(path, parent_path)
    for file in os.listdir(path):
        #print(type(file))

        new_names = file.split('.')
        #print(new_names)
        if len(new_names) > 2:
            if new_names[2] == 'pyc':
                new_file_name = '{}.{}'.format(new_names[0],new_names[2])
                print('new:', new_file_name)
                os.rename(os.path.join(path,file), os.path.join(path, new_file_name))
                try:
                    shutil.move(os.path.join(path, new_file_name), parent_path)
                except Exception as e:
                    print(e)
                    pass


def find_pyc(path):
    for file in os.listdir(path):
        path_dir = os.path.join(path, file)
        if os.path.isdir(path_dir):
            #print(path_dir)
            if file == '__pycache__':
                print('change:', path_dir)
                change_name(path_dir, path)
            else:
                #print('deep in:', path_dir)
                find_pyc(path_dir)


if __name__ == '__main__':  
    # if without pyc run this
    # compile_run()
    find_pyc(os.getcwd())
    print('All has done.')
