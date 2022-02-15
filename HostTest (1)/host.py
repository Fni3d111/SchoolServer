import socket
import time
from Control_computer_data import STOP_CONTROL
from write_simple_sentences import get_sentece
from Control_computer_data import STOP_CONTROL
from write_combinations import record_combo,record_mouse
from scroll_mouse_detect import scroll_control
from detect_mouse_clicks import detect_mouse_clicks
HEADER = 64
FORMAT = 'utf-8'
import multiprocessing
#from allfiles.create_permanent import add_to_list_permanent
import threading
from Control_computer_data import run
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 30111
permanent_computers = []
data = (SERVER,PORT)
print(data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(data)
s.listen(5)
print(f"[LISTENING] Server is listening on {data} ")

computers_list = []

def send_message_to_specific_computer(message,id):
    print(message)
    message = message.encode(FORMAT)
    print(computers_list)
    for x in computers_list:
        print(f"SERIAL NUMBER IS {x['serial_number']}")
        if x['serial_number'] == id:
            print('Should send')
            x['conn'].send(message)

def Register(conn):
    room = conn.recv(2048).decode(FORMAT)
    name = conn.recv(2048).decode(FORMAT)
    return room,name

def control_compuetr(computers):
    message = input("What is the message?")
    for x in computers:
        x['conn'].send(message.encode(FORMAT))
def send_message_to_everyone():
    message = input("What do you want to send to everyone?")
    message = message.encode(FORMAT)

    for x in computers_list:
        x['conn'].send(message)


def Computer_Control(conn=None):
    run('false')
    id_of_computer = input("ENTER ID OF COMPUTER")
    for computer in computers_list:
        if int(id_of_computer) == computer['serial_number']:
            target_conn = computer['conn']

    detect_mouse_clicks_thread = threading.Thread(target=detect_mouse_clicks,args=(target_conn,))
    detect_mouse_clicks_thread.start()
    print('yes')
    record_combo_thread = threading.Thread(target=record_combo,args=(target_conn,))
    record_combo_thread.start()


    record_mouse_thread = threading.Thread(target=record_mouse,args=(target_conn,))
    record_mouse_thread.start()

    scroll_mouse_thread = threading.Thread(target=scroll_control,args=(target_conn,))
    scroll_mouse_thread.start()


    while True:
        try:
            detector = input('Would you like to stop? to stop enter yes')
            if detector == 'yes':
                break
        except:
            print('not yet')
    print('should stop')
    run('stop')

    scroll_mouse_thread.join()
    record_mouse_thread.join()
    record_combo_thread.join()
    detect_mouse_clicks_thread.join()


def Computer_Control_for_everyone():
    list_of_conn = []
    for computer in computers_list:
        list_of_conn.append(computer['conn'])
    print(list_of_conn)
    detect_mouse_clicks_thread = threading.Thread(target=detect_mouse_clicks,args=(list_of_conn,True))
    detect_mouse_clicks_thread.start()
    print('yes')
    record_combo_thread = threading.Thread(target=record_combo,args=(list_of_conn,True))
    record_combo_thread.start()


    record_mouse_thread = threading.Thread(target=record_mouse,args=(list_of_conn,True))
    record_mouse_thread.start()

    scroll_mouse_thread = threading.Thread(target=scroll_control,args=(list_of_conn,True))
    scroll_mouse_thread.start()


    while True:
        try:
            detector = input('Would you like to stop? to stop enter yes')
            if detector == 'yes':
                break
        except:
            print('not yet')
    print('should stop')
    run('stop')

    scroll_mouse_thread.join()
    record_mouse_thread.join()
    record_combo_thread.join()
    detect_mouse_clicks_thread.join()


def send_messages_detection():
    while True:
        try:
            code  = input('what code?')

            if int(code) == 1:
                print('everyone')
                send_message_to_everyone()
            if int(code) == 7:
                Computer_Control()
                print('Hi i am done, continue')
            if int(code) == 999:
                for computer in computers_list:
                    print(f'Computer Name: {computer["name"]}, The room is {computer["room"]}')
            if int(code) == 10:
                threading.Thread(target=Computer_Control_for_everyone())
            if int(code) == 11:
                list_of_conn = []
                for computer in computers_list:
                    list_of_conn.append(computer['conn'])
                sec = input("ENTER WHAT IS THE REPETITION IN SECONDS")
                background = input("ENTER THE NAME OF THE BACKGROUNDS AND SEPERATE WITH ; ")
                backgrounds = background.split(';')
                print(background)
                backgrounds = repr(backgrounds)
                break_check = input("IF YOU WANT TO BREAK ENTER yes")
                if break_check == 'yes':
                    break
                message = f'auto change background;{sec};{backgrounds}'
                message = message.encode(FORMAT)
                for client in list_of_conn:
                    client.send(message)
            if int(code) == 12:
                list_of_conn = []
                for computer in computers_list:
                    list_of_conn.append(computer['conn'])
                message = 'stop auto change'.encode(FORMAT)
                for client in list_of_conn:
                    client.send(message)





        except ValueError as e:
            print(str(e))


def add_computer_to_database(info):
    computers_list.append(info)
    return info
def renmove_conn(conn):
    for x in computers_list:
        if x['conn'] == conn:
            print('yes it is')
            computers_list.remove(x)

def receive_messages(computer_info):
    while True:
        msg = computer_info['conn'].recv(2048).decode(FORMAT)
        print(msg)
        if msg == "!DISS":
            for computer in computers_list:
                if computer['conn']==computer_info['conn']:
                    computers_list.remove(computer)
                    return

serial_numbers = []


threading.Thread(target=send_messages_detection).start()


def main():
    while True:
        conn, addr = s.accept()

        print(f"Hi {addr}")
        serial_number = None
        for x in range(250):
            if x not in serial_numbers:
                serial_number = x
                serial_numbers.append(x)
            if serial_number:
                break
        room,name = Register(conn)
        computer = {
            'name':name,
            'room':room,
            'conn':conn,
            'addr':addr,
            'serial_number':serial_number
        }
        print(computer)
        add_computer_to_database(computer)
        threading.Thread(target=receive_messages,args=(computer,)).start()
        time.sleep(5)
if __name__ == '__main__':
    #multiprocessing.Process(target=send_messages_detection).start()

    main()
