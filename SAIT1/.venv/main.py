from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
conection = sqlite3.connect(r".venv\bazadannixsaita.db", check_same_thread=False)
cursor = conection.cursor()


@app.route("/")
def into ():
    return render_template("main.html")


@app.route("/goods")
def inlo ():
    return render_template("goods.html")

@app.route("/goods/pc")
def pc ():
    cursor.execute("SELECT * FROM Computers")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)

@app.route("/goods/headphones")
def hd ():
    cursor.execute("SELECT * FROM headphones")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)


@app.route("/goods/Klaws")
def Klaaws ():
    cursor.execute("SELECT * FROM Klaws")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)


@app.route("/goods/mishki")
def mishki ():
    cursor.execute("SELECT * FROM mishki")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)


@app.route("/goods/phones")
def Phones ():
    cursor.execute("SELECT * FROM Phones")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)


@app.route("/goods/mikrofons")
def mikro ():
    cursor.execute("SELECT * FROM mikrofons")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)


@app.route("/goods/laptops")
def laptops ():
    cursor.execute("SELECT * FROM laptops")
    result = cursor.fetchall()
    return render_template("goods.html", result = result)


if __name__ == "__main__":
    app.run(debug=True) 
