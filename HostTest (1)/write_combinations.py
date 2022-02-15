import sys
import time
import pyautogui
from pynput import keyboard
import threading
from Control_computer_data import STOP_CONTROL as should_stop
FORMAT = 'utf-8'
counter = 0
special_keybind = {
    'ctrl_l':'ctrl','alt_l':'alt','cmd':'win'
}



def _check_for_stop():
    from Control_computer_data import STOP_CONTROL
    if STOP_CONTROL == True:
        return True

def record_mouse(conn,multiple=None):
    while True:
        time.sleep(0.5)
        my_location = pyautogui.position()
        x,y = my_location[0],my_location[1]
        data = repr([x,y])
        message = f'mousecord;{data};'.encode(FORMAT)
        if multiple:
            for client in conn:
                client.send(message)
        else:
            conn.send(message)
        should_i_stop = _check_for_stop()
        if should_i_stop:
            print('Exiting record mouse')
            return




def record_combo(conn,multiple = None):
    def on_press(key):


        try:
            key = key.char
        except AttributeError:
            key = str(key)
            key = key[4:]
        for keybind_key,values in special_keybind.items():
            if key == keybind_key:
                key = values

        key = str(key)
        message = f'write;{key};'.encode(FORMAT)

        if multiple:
            for client in conn:
                client.send(message)
        else:
            conn.send(message)
    def on_release(key):
        pass

    with keyboard.Listener(on_press=on_press,on_release=on_release) as l:
        def stop():
            while True:
                time.sleep(1)
                should_i_stop =_check_for_stop()
                if should_i_stop:   # Listen to keyboard for period_sec seconds
                    print("STOPS WRITING")
                    l.stop()
                    return
        threading.Thread(target=stop).start()
        l.join()
