import multiprocessing
import time
from threading import Timer

from pynput.mouse import Listener
import threading
def _check_for_stop():
    from Control_computer_data import STOP_CONTROL
    if STOP_CONTROL == True:
        return True
def scroll_control(conn,multiple = None):
    def on_scroll(x, y, dx, dy):
        message = f'scroll;{str(dy)};'.encode('utf-8')
        print(message)
        if multiple:
            print('yes! multiple')
            for client in conn:
                client.send(message)
        else:
            conn.send(message)

    with Listener(on_scroll=on_scroll) as l:
        def stop():
            while True:
                time.sleep(1)
                should_i_stop =_check_for_stop()
                if should_i_stop:   # Listen to keyboard for period_sec seconds
                    print("STOPPING SCROLL MOUSE ")
                    l.stop()
                    return
        threading.Thread(target=stop).start()
        l.join()
