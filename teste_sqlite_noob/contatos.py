# enconding: utf-8
import sqlite3
import os.path
con = sqlite3.connect("contatos.db")


def menu():
  print("#########################")
  print("1 - Listar contatos")
  print("2 - Inserir contatos")
  print("3 - Remover contatos")
  print("0 - Sair")
  print("#########################")

def inserir():
  cursor = con.cursor()
  print("Digite as informações do contato: ")
  nome = input("Nome: ")
  email = input("E-mail: ")
  fone = input("Fone: ")
  cursor.execute("INSERT INTO contato(nome,email,fone) VALUES('"+nome+"','"+email+"','"+fone+"')");
  con.commit()
  cursor.close()

def listar():
  cursor = con.cursor()
  cursor.execute("""
  SELECT * 
  FROM contato;
  """)
  lista = cursor.fetchall()
  for registro in lista:
    print("///////////////////////////////////")
    print("ID:      ",registro[0])
    print("Nome:    ",registro[1])
    print("E-mail:  ",registro[2])
    print("Contato: ",registro[3])
    print("///////////////////////////////////")
  cursor.close()

def remover():
  cursor = con.cursor()
  listar()
  registro = input("Informe o numero do registro que deseja remover: ")
  cursor.execute("DELETE FROM contato WHERE id='"+registro+"' ")
  con.commit()
  cursor.close()

  
opcao=1

while (opcao!=0):
  menu()
  opcao = int(input()) 
  if opcao==1:    
    listar()

  elif opcao==2:
    inserir()
  elif opcao==3:
    remover()
  elif opcao==0:
    opcao=0
  else:
    print("Opção Invalida, tente novamente")
