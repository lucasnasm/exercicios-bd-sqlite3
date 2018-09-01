# enconding: utf-8
import sqlite3
con = sqlite3.connect("dados.db")
cursor = con.cursor()
cursor.execute("""
	SELECT * 
	FROM contato;
""")
lista = cursor.fetchall()

for registro in lista:
	print(registro[0],registro[1],registro[2],registro[3])


cursor.close()