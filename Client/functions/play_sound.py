import time
from pygame import mixer
from os.path import dirname, abspath
import os
from distutils.dir_util import copy_tree

father_path = dirname(dirname(abspath(__file__))) # D:\MyDrive\CODING\School Server\Client
print(father_path)
#father_path = f'{father_path}powerpointTemplates/resources/'
father_path = f'{father_path}/resources/'  #D:\MyDrive\CODING\School Server\Client\resources


data = [
    ['helicopter','helicopter.mp3'],['thanos','Thanos-snap.mp3.wav']
]

def play_sound(name_of_sound):
    mixer.init()

    for x in data:
        if x[0] == name_of_sound:
            mixer.music.load(f'{father_path}{x[1]}')
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
