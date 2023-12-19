import psycopg2
import os
from flask import Flask, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

USER = os.getenv("USER")
ROOT = os.getenv("ROOT")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
BOM = os.getenv("BOM")

NUM = 0


def connect_to_postgres():
    conn = psycopg2.connect(
        user= USER,
        password=ROOT,
        host=HOST,
        port=PORT,
        database=BOM
    )

    return conn


def check(cur, num):
    cur.execute("SELECT num FROM nums WHERE num=%s", (num,))
    res = cur.fetchone()

    if res:
        return False

    return True


@app.route("/ER_1")
def error_one():
    print("Число уже есть в базе")
    return "Число уже есть в базе"


@app.route("/ER_2")
def error_two():
    print("Это число меньше, чем то что в базе")
    return "Это число меньше, чем то что в базе"


@app.route("/NXT")
def next_number():
    return str(NUM + 1)


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        conn = connect_to_postgres()
        cur = conn.cursor()

        num = request.form.get("num")

        global NUM
        NUM = int(num)

        if not check(cur, NUM):
            return redirect(url_for("ER_!"))

        if not check(cur, NUM + 1):
            return redirect(url_for("ER_2"))

        cur.execute("INSERT INTO nums VALUES (%s)", (NUM,))
        conn.commit()

        return redirect(url_for("NXT"))

    return

if __name__ == "__main__":
    app.run()