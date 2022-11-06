import sqlite3


def bd_see():
    con = sqlite3.connect("bd_olimp.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM bd_search""").fetchall()
    con.close()


def bd_sive(text_value):
    con = sqlite3.connect("bd_olimp.db")
    cur = con.cursor()
    result = cur.execute(f"""INSERT INTO bd_search(name_search) VALUES({text_value})""").fetchall()
    for elem in result:
        print(elem)
    con.close()


def bd_delete(text_value):
    con = sqlite3.connect("bd_olimp.db")
    cur = con.cursor()
    result = cur.execute(f"""DELETE from bd_search
        where name_search = {text_value}""").fetchall()
    con.close()
