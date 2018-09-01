# enconding: utf-8
import sqlite3
con = sqlite3.connect("dados.db")
cursor = con.cursor()

nome = input("Nome: ")
email = input("E-mail: ")
fone = input("Fone: ")
cursor.execute("INSERT INTO contato(nome,email,fone) VALUES('"+nome+"','"+email+"','"+fone+"')");

con.commit()

cursor.close()
