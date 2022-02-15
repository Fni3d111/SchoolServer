from os.path import dirname, abspath
import ctypes
import requests
import time
father_path = dirname(dirname(abspath(__file__))) # D:\MyDrive\CODING\School Server\Client
print(father_path)
path = f'{father_path}/photos'
should_work_auto_change = True


def change_should_work_auto_change(start=None,stop=None):
    global should_work_auto_change
    if start:
        should_work_auto_change = True
    if stop:
        should_work_auto_change = False
def change_background(photo):
    photo_path = f'{path}/{photo}.jpg'
    print(photo_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0,  photo_path, 0)


def download_photos(name_of_photo,link):
    photo_path = f'{path}/{name_of_photo}.jpg'

    response = requests.get(link)

    file = open(f'{photo_path}', "wb")
    file.write(response.content)
    file.close()
    return
def auto_change_background(backgrounds,sec):
    global should_work_auto_change
    print('IN FUNCTION')
    while should_work_auto_change == True:
        for x in backgrounds:
            change_background(x)
            time.sleep(sec)
    print("DONE CLOSING THREAD")
