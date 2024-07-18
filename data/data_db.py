from pprint import pprint
import sqlite3

db_name = "database_pizza.db"

def make_read_query(query):
    try:
        with sqlite3.connect(db_name) as conn:
            print(f"База даних {db_name} підключена")
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

        data_studs = [{"name": row[1],
                       "ingredients": row[2],
                       "price": row[3],
                       } for row in result if result]

        return data_studs

    except sqlite3.Error as e:
        print("Помилка запиту:", e)


def make_write_query(query, *args):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            print(f"Запит {query.split()[0]} виконаний з {args}")
    except sqlite3.Error as e:
        print("error", e)

def create_table():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    query = """
    CREATE TABLE IF NOT EXISTS pizzamenu (
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        price TEXT NOT NULL
    );
    """
    make_write_query(query)

def insert_data(name, ingredients, price):
    query = """
    INSERT INTO pizzamenu (name, ingredients, price)
    VALUES (?, ?, ?)
    """
    args = (name, ingredients, price)
    make_write_query(query, *args)

def get_all():
    query = """SELECT * FROM pizzamenu"""
    return make_read_query(query)

if __name__ == "__main__":
    create_table()

    data = [
        {"name": "Margherita", "ingredients": "Tomato sauce, mozzarella, basil", "price": "10$"},
        {"name": "Pepperoni", "ingredients" : "Salami, cheese, garlic", "price" : "15$"},
        {"name": "Four Chesee", "ingredients" : "Tomato sause, 4 types of chesee (blue, soft, creamy and hard)", "price" : "15$"}
    ]
    pprint(get_all())