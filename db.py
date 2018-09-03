# enconding: utf-8
#Importando a biblioteca SQLITE
import sqlite3

def criar_db():
  #Abrindo a conexao com o arquivo dados.db
  con = sqlite3.connect("pdv_mercado.db")
  #Cria o cursor
  cursor = con.cursor()
  #Comando sql
  cursor.execute("""
	CREATE TABLE produto(
	  id INTEGER PRIMARY KEY,
	  descricao VARCHAR(100),
	  valor NUMERIC(10,2),
	  quantidade INT
	);
  """)
  cursor.execute("""
	CREATE TABLE cliente(
	  id INTEGER PRIMARY KEY,
	  nome VARCHAR(100),
	  telefone VARCHAR(20)
	);
  """)
  cursor.execute("""
	CREATE TABLE venda(
	  id INTEGER PRIMARY KEY,
	  id_cliente INT,
	  id_produto INT
	);
  """)
  #Fechando a conexao
  con.close()
