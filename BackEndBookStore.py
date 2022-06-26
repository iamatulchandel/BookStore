import sqlite3
def CREATETable():
    con=sqlite3.connect("Books")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Books (Title TEXT,Author TEXT,Year INTEGER, ISBN INTEGER)")
    con.commit()
    con.close()
def INSERTtable(TItle,Author,Year,ISBN):
    con=sqlite3.connect("Books")
    cur=con.cursor()
    cur.execute("INSERT INTO Books VALUES(?,?,?,?)",(TItle,Author,Year,ISBN))
    con.commit()
    con.close()
def view():
    con = sqlite3.connect('Books')
    cur = con.cursor()
    cur.execute('SELECT * FROM Books')
    data=cur.fetchall()
    con.close()
    return data
def SEARCHEntry(Title,Author,Year,ISBN):
    con = sqlite3.connect("Books")
    cur = con.cursor()
    cur.execute("SELECT * FROM Books where Title=? OR Author=? OR Year=? OR ISBN=?",(Title,Author,Year,ISBN))
    data = cur.fetchall()
    con.close()
    return data
def UPDATEentry(Title,Author,Year,ISBN):
    con = sqlite3.connect("Books")
    cur = con.cursor()
    cur.execute("UPDATE Books SET Author=? , Year=? , ISBN=? where Title=?", (Author, Year, ISBN,Title))
    con.commit()
    con.close()
def DELETEentry(Title):
    con = sqlite3.connect("Books")
    cur = con.cursor()
    cur.execute("DELETE FROM Books where Title=?",(Title,))
    con.commit()
    con.close()

CREATETable()

