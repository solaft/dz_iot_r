import socket # модукль для работы с сокетами
import psycopg2  # молудль для работы с PostgreSQL 
from threading import Thread # подключаем модуль многопоточности

# соединяемся с сервером
conn = psycopg2.connect(database="Userdb", user="username1",
    password="rootroot987", host="localhost", port=5432)

cur = conn.cursor() # устанавливаем соединение с БД
new_socket = socket.socket()
new_socket.bind(('127.0.0.1', 5000))

new_socket.listen(1)

print("Сервер запущен!")

conn1, add1 = new_socket.accept()
print("Клиент запущен!")
cursor.execute('SELECT number FROM numbers')

# В БД состоит из таблицы с перечнем введеных чисел

# ___________
# id|numbers|
#  1|   77  |
#  2|   88  |
#____________

db = cursor.fetchall()
i=1; # переменная для счета индексов списка чисел в БД
def acceptor1():
    while True:
        a = int(conn1.recv(1024))+1
        if a in db:
            ans="Ошибка! Число есть в базе!".encode("utf-8")
        else:
            if a == db[i-1]:
                ans="Ошибка! Меньшее число есть в базе!".encode("utf-8")   
            else :
                db.append(a)
                ans = str(a).encode("utf-8")
        i=i+1
        conn1.send(ans)
        
tread1 = Thread(target=acceptor1)

tread1.start()
