import sqlite3


class db_all():
    def bd_see(self):
        con = sqlite3.connect("db_olimp.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM db_search""").fetchall()
        for elem in result:
            print(elem)
        con.close()

    def bd_sive(self, text_value):
        con = sqlite3.connect("db_olimp.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""INSERT INTO db_search(name_search) VALUES({text_value})""").fetchall()
        for elem in result:
            print(elem)
        con.close()

    def bd_delete(self, text_value):
        con = sqlite3.connect("handler/db_site.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""DELETE from db_search
            where name_search = {text_value}""").fetchall()
        for elem in result:
            print(elem)
        con.close()

    def login(self, login):
        """преверка на ввод"""
        con = sqlite3.connect('handler/db_site.sqlite')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM bd_search')
        value = cur.fetchall()
        cur.close()
        con.close()

    def register(self, login):
        """'добовление элементов"""
        print(123)
        con = sqlite3.connect('handler/db_site.sqlite')
        cur = con.cursor()
        cur.execute(f"INSERT INTO db_search (name_search) VALUES ('{login}')")
        cur.close()
