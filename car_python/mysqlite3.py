import sqlite3
#="create table elvis (id int, cognome text, nome text)"
#cc=input("scrivi cognome: ")
#nn= input("scrivi nome: ")
#x= "insert into elvis (cognome , nome ) values (? , ?)"
#y= [cc, nn]
x= "select * from elvis"
conn = sqlite3.connect("archivio.db")
cur=conn.cursor()
#cur.execute(x)
cur.execute(x)
vedere = cur.fetchall()
print(vedere)
conn.commit()
conn.close()

