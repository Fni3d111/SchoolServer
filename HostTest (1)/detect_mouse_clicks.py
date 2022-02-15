import time
import pynput.mouse
from pynput.mouse import Listener
import sys
import threading
FORMAT = 'utf-8'

def _check_for_stop():
    from Control_computer_data import STOP_CONTROL
    if STOP_CONTROL == True:
        return True

def detect_mouse_clicks(conn,multiple=None):
    def is_clicked(x, y, button, pressed):
        print('clicked')
        if pressed:
            if button == pynput.mouse.Button.left:
                button = 'left'
            else:
                button = 'right'
            message = f'mouseClick;{button};'.encode(FORMAT)
            if multiple:
                for client in conn:
                    client.send(message)
            else:
                conn.send(message)
    with Listener(on_click=is_clicked) as l:
        def stop():
            while True:
                time.sleep(1)
                should_i_stop =_check_for_stop()
                if should_i_stop:   # Listen to keyboard for period_sec seconds
                    print("STOPPING MOUSE CLICK DETECT")
                    l.stop()
                    return
        threading.Thread(target=stop).start()
        l.join()
