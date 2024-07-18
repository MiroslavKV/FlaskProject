from pprint import pprint

from flask import Flask
from flask import render_template, url_for, abort
from data.data_db import create_table, insert_data, get_all

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.py.html")

@app.route("/some/")
def some():
    return url_for("menu_page")

@app.route("/menu/")
def menu():
    allmenu = get_all()
    return render_template('menu.py.html', pizzas=allmenu)

@app.route('/menu/')
def students(message_info=None):
    pizza = get_all()
    context = {
        "Pizza": pizza,
        "message":message_info
    }
    pprint(pizza)

    return render_template("menu.py.html", **context)

@app.route("/order/")
def order_page():
    return render_template("order.html")

@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")

@app.errorhandler(500)
def error_500(error):
    return render_template("errors/500.html")

if __name__ == "__main__":
    create_table()
    app.run(host = "localhost", port = 4441, debug = False)