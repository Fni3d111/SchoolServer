import requests
from bs4 import BeautifulSoup

def get_data_of_server():
    print("I AM HERE IN GET DATA SERVER")
    link = 'https://anotepad.com/notes/4y577ch2'
    r = requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find(class_='plaintext').text
    data = data.split(',')
    PORT = int(data[1])
    IP = data[0]
    return IP,PORT