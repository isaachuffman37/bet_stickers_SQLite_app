import sqlite3

conn = sqlite3.connect('stickers.db')
c = conn.cursor()
# c.execute("DROP TABLE stickers")
# create the sticker table with relevant attributes
# c.execute(""" CREATE TABLE stickers(
#           name TEXT NOT NULL,
#           price REAL NOT NULL,
#           amount_in_stock INTEGER NOT NULL


#  )""")
# c.execute("DROP TABLE sales")

# c.execute("""CREATE TABLE sales(
#          sale_id INTEGER PRIMARY KEY,
#           name TEXT REFERENCES stickers(name),
#           amount_sold INTEGER NOT NULL,
#           sale_date text NOT NULL,
#           total_profit REAL
# )""")
# c.execute('''CREATE TRIGGER update_stock
#             AFTER INSERT ON sales
#             BEGIN
#                 UPDATE stickers
#                 SET amount_in_stock = amount_in_stock - NEW.amount_sold
#                 WHERE name = NEW.name;
#             END;''')


# c.execute("Delete From stickers")






def add_one_sticker():
    name = input("What is the name of the sticker? ")
    price = float(input("Price sold at: "))
    in_stock = int(input("How many are in stock?"))

    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.execute("INSERT INTO stickers VALUES(?,?,?)", (name, price, in_stock))

    conn.commit()
    conn.close()




def view_stickers_table():
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.execute("SELECT * FROM stickers")
    items = c.fetchall()
    for item in items:
        print(f"Sticker Name: {item[0]}   Price: ${item[1]}   In Stock: {item[2]}")

    conn.commit()
    conn.close()




def add_one_sale():
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()
    sale_id = input("What is the sale ID you want to assign it? ")
    visibility = input("Would you like to see the stickers table?(y/n)").lower()
    if visibility == 'y':
        view_stickers_table()
    name = input("What is the exact name of the sticker? ")
    amount_sold = int(input("What is the total amount sold?"))
    sale_date = input("What is the date that you made this sale?(mm/dd/yyyy) ")

    c.execute("INSERT into sales VALUES(?,?,?,?, (SELECT price FROM stickers WHERE name == ?) * ?)", (sale_id, name, amount_sold, sale_date, name, amount_sold))

    conn.commit()
    conn.close()




def view_sales_table():
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.execute("SELECT * FROM sales")
    items = c.fetchall()
    print()
    for item in items:
        print(f" Sale Id: {item[0]}     Sticker Name: {item[1]}     Amount Sold: {item[2]}     Date: {item[3]}     Revenue: ${item[4]}")

    conn.commit()
    conn.close()


def get_limited_revenue_info(limit):
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.execute(""" SELECT stickers.name, stickers.amount_in_stock, stickers.price, SUM(sales.amount_sold),SUM(sales.total_profit) AS total_profit
              FROM sales
              JOIN stickers ON sales.name = stickers.name
              GROUP BY stickers.name
              ORDER by total_profit DESC""")
    items = c.fetchmany(limit)
    for item in items:
        print(f" Sticker: '{item[0]}'   In Stock: {item[1]}    Price: {item[2]}   Total Sold: {item[3]}    Total Revenue: {item[4]}")




def get_all_revenue_info():
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.execute(""" SELECT stickers.name, stickers.amount_in_stock, stickers.price, SUM(sales.amount_sold),SUM(sales.total_profit) AS total_profit
              FROM sales
              JOIN stickers ON sales.name = stickers.name
              GROUP BY stickers.name
              ORDER by total_profit DESC""")
    items = c.fetchall()
    for item in items:
        print(f" Sticker: '{item[0]}'   In Stock: {item[1]}    Price: {item[2]}   Total Sold: {item[3]}    Total Revenue: {item[4]}")

def update_stock_amount(name, amount):
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()
    
    c.execute(""" Update stickers 
                SET amount_in_stock = amount_in_stock + ?
                WHERE name = ?""",(amount,name))
    conn.commit()
    conn.close()

def delete_sticker(name):
    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.execute("""DELETE FROM stickers
                WHERE name = ?""", (name,))
    conn.commit()
    conn.close()


def add_many_stickers(list):

    conn = sqlite3.connect('stickers.db')
    c = conn.cursor()

    c.executemany("INSERT INTO stickers VALUES(?,?,?)", (list))
    conn.commit()
    conn.close()




conn.commit()
conn.close()


