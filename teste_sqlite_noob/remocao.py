# enconding: utf-8
import sqlite3
con = sqlite3.connect("dados.db")
cursor = con.cursor()

cursor.execute("""
	SELECT * 
	FROM contato;
""")
lista = cursor.fetchall()

#Listar registros
for registro in lista:
	print(registro[0],registro[1],registro[2],registro[3])

#Apagar passando id
registro = input("Digite o id")

cursor.execute("DELETE FROM contato WHERE id='"+registro+"' ")

con.commit()

cursor.close()