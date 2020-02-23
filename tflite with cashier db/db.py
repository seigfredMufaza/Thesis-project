import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, item text, quantity INTEGER, price INTEGER, weight INTEGER)")
        #self.cur.execute("DELETE FROM parts")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts WHERE quantity > 0")
        rows = self.cur.fetchall()
        return rows

    def insert(self, item, quantity, price, weight):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (item, quantity, price, weight))
        self.conn.commit()
        

    def remove(self, id):
        self.cur.execute("UPDATE parts SET quantity = 0, price = 0, weight = 0 WHERE id=?", (id,))
        self.conn.commit()

    def reset_all(self):
        self.cur.execute("UPDATE parts SET quantity = 0, price = 0, weight = 0")
        self.conn.commit()

    def updateorange(self):
        self.cur.execute("UPDATE parts SET quantity = quantity + 1, price = price + 10, weight = weight + 135 WHERE id = 1")
        self.conn.commit()

    def updateapple(self):
        self.cur.execute("UPDATE parts SET quantity = quantity + 1, price = price + 10, weight = weight + 110 WHERE id = 2")
                       
        self.conn.commit()

    def updatebanana(self):
        self.cur.execute("UPDATE parts SET quantity = quantity + 1, price = price + 8, weight = weight + 120 WHERE id = 3")
                       
        self.conn.commit()

    def display_price(self):
        self.cur.execute("SELECT SUM(price) FROM parts")
        tprice= self.cur.fetchall()
        return tprice 

    def display_weight(self):
        self.cur.execute("SELECT SUM(weight) FROM parts")
        tweight= self.cur.fetchall()
        return tweight 

    def fetch_orange(self):
        self.cur.execute("SELECT * FROM parts where id = 1 AND quantity > 0")
        forange= self.cur.fetchall()
        return forange

    def fetch_apple(self):
        self.cur.execute("SELECT * FROM parts where id = 2 AND quantity > 0")
        fapple= self.cur.fetchall()
        return fapple

    def fetch_banana(self):
        self.cur.execute("SELECT * FROM parts where id = 3 AND quantity > 0")
        fbanana= self.cur.fetchall()
        return fbanana

    def __del__(self):
        self.conn.close()

    


db = Database('jsj.db')

#db.insert("APPLE", "1", "10")
#db.insert("BANANA", "1", "8")
#db.insert("ORANGE", "1", "10")