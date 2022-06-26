import sqlite3
def CREATETable():
    con=sqlite3.connect("op.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INT,price REAL)")
    con.commit()
    con.close()
def INSERTtable(item,quantity,price):
    con=sqlite3.connect("op.db")
    cur=con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    con.commit()
    con.close()
def view():
    con = sqlite3.connect("op.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM store')
    data=cur.fetchall()
    con.close()
    return data
CREATETable()
print('Enter total enteries')
n=int(input())
for i in range(n):
    print('Add Name, Quantity and price respectively')
    n=input()
    m=int(input())
    o=float(input())
    INSERTtable(n,m,o)
print(view())

