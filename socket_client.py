#Подключаем зависимости
import socket
from threading import Thread
#Создаём новый сокет
client_socket = socket.socket()
#Заставляем его подключиться к серверному сокету
client_socket.connect(("127.0.0.1", 5000))
#Создаём ф-и отправки и получения сообщений
def sender():
    while True:
      #Читаем строку с клавиатуры
        a = input("Введите число :")
        #Отправляем её, предварительно закодировав
        client_socket.send(a.encode("utf-8"))
def reciver():
    while True:
      #Получаем строку от сервера
        b = client_socket.recv(1024)
       #Печатаем, предварительно раскодировав
        print(b.decode("utf-8"))
#Создаём по отдельному потоку для каждой функции
tread1 = Thread(target=sender)
tread2 = Thread(target=reciver)
#Потоки запушены, клиент готов получать и отправлять сообщения
tread1.start()
tread2.start()