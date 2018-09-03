# enconding: utf-8
from db import *
from pathlib import Path

path_db = Path("pdv_mercado.db")
if(path_db.exists()):
  con = sqlite3.connect("pdv_mercado.db")
else:
  criar_db()
  print("Banco criado com sucesso")
  con = sqlite3.connect("pdv_mercado.db")


def menuApresentacao():
  print("Informe uma opção para começar: ")
  print("#"+"\033[31m"+"(1)"+"\033[0;0m"+" - Menu Clientes  \033[0;0m")
  print("#"+"\033[31m"+"(2)"+"\033[0;0m"+" - Menu Produtos  \033[0;0m")
  print("#"+"\033[31m"+"(3)"+"\033[0;0m"+" - Menu Vendas    \033[0;0m")
  print("#"+"\033[31m"+"(0)"+"\033[0;0m"+" - Sair   \033[0;0m")


def menuClientes():
  print("-------------------------------------------------------------------------------------------------------------------")
  print("|\033[31m"+"(1)"+"\033[0;0m"+" - Listar Clientes | \033[31m"+"(2)"+"\033[0;0m"+" - Cadastrar Cliente | \033[31m"+"(3)"+"\033[0;0m"+" - Atualizar Cliente | \033[31m"+"(4)"+"\033[0;0m"+" - Remover Cliente | \033[31m"+"(0)"+"\033[0;0m"+" - Voltar |")
  print("-------------------------------------------------------------------------------------------------------------------")

  op_cliente = int(input("Informe uma opção para iniciar: \n"))
  if (op_cliente==1):
    listar("T_C")
  elif(op_cliente==2):
    inserir("T_C")
  elif(op_cliente==3):
    verificaId("T_C")
  elif(op_cliente==4):
    remover("T_C")
  elif(op_cliente==0):
    return True
  else:
    print("Opção Invalida")


def menuVendas():
  print("------------------------------------------------------------")
  print("|\033[31m"+"(1)"+"\033[0;0m"+" - Listar Vendas | \033[31m"+"(2)"+"\033[0;0m"+" - Realizar Venda | \033[31m"+"(0)"+"\033[0;0m"+"\033[0;0m"+" - Voltar |")
  print("------------------------------------------------------------")

  op_vendas= int(input("Informe uma opção para iniciar: \n"))
  if (op_vendas==1):
    listar("T_V")
  elif(op_vendas==2):
    vendas()
  elif(op_vendas==0):
    return True
  else:
    print("Opção Invalida")


def menuProdutos():
  print("-------------------------------------------------------------------------------------------------------------------")
  print("|"+"\033[31m"+"(1)"+"\033[0;0m"+" - Listar Produtos | \033[31m"+"(2)"+"\033[0;0m"+" - Cadastrar Produto | \033[31m"+"(3)"+"\033[0;0m"+" - Atualizar Produto | \033[31m"+"(4)"+"\033[0;0m"+" - Remover Produto | \033[31m"+"(0)"+"\033[0;0m"+" - Voltar |")
  print("-------------------------------------------------------------------------------------------------------------------")
  op_prod = int(input("Informe uma opção para iniciar: \n"))
  if (op_prod==1):
    listar("T_P")
  elif(op_prod==2):
    inserir("T_P")
  elif(op_prod==3):
    verificaId("T_P")
  elif(op_prod==4):
    remover("T_P")
  elif(op_prod==0):
    return True
  else:
    print("Opção Invalida")


def inserir(seletor_menu):
    if (seletor_menu == "T_P"):
      cursor = con.cursor()
      print("Digite as informações do produto: ")
      descricao = input("Descrição: ")
      valor = input("Valor: ")
      quantidade = input("Quantidade: ")
      sql_produto = "INSERT INTO produto(descricao,valor,quantidade) VALUES(?,?,?)"
      cursor.execute(sql_produto, (descricao,valor,quantidade));
      con.commit()
      cursor.close()
      print("Produto inserido com sucesso!!!")
    elif(seletor_menu == "T_C"):
      cursor = con.cursor()
      print("Digite as informações do cliente: ")
      nome = input("Nome Completo: ")
      telefone = input("telefone: ")
      sql_cliente = "INSERT INTO cliente(nome,telefone) VALUES(?,?)"
      cursor.execute(sql_cliente, (nome,telefone));
      con.commit()
      cursor.close()
      print("Clinte inserido com sucesso!!!")
    else:
      print("Opção Desconhecida")


def verificaId(seletor_menu):
  cursor = con.cursor()
  if(seletor_menu=="T_P"):
    listar(seletor_menu)
    id_prod = input("Informe o numero do produto: \n")
    cursor.execute("SELECT id FROM produto WHERE id=?", (id_prod,))
    consulta = cursor.fetchone()
    if not consulta:
        print("Produto não encontrado, tente novamente")
    else:
      listar(seletor_menu)
      atualizar(id_prod,seletor_menu)
  elif(seletor_menu=="T_C"):
    listar(seletor_menu)
    id_cli = input("Informe o numero de registro do cliente: \n")
    cursor.execute("SELECT id FROM cliente WHERE id=?", (id_cli,))
    consulta = cursor.fetchone()
    if not consulta:
      print("Cliente não encontrado, tente novamente")
    else:
      atualizar(id_cli,seletor_menu)


def atualizar(id_reg,seletor_menu):
  cursor = con.cursor()
  if (seletor_menu == "T_P"):
    print("Informe o novo nome do produto: ")
    descricao = input("Descrição: ")
    print("Informe o novo valor ")
    valor = input("Valor: ")
    cursor.execute("UPDATE produto SET descricao=?, valor=? WHERE id=?", (descricao,valor,id_reg))
    con.commit()
    cursor.close()
    print("Produto atualizado com sucesso!!!")
  elif(seletor_menu == "T_C"):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cursor.execute("UPDATE cliente SET nome=?, telefone=? WHERE id=?", (nome,telefone,id_reg))
    con.commit()
    cursor.close()
    print("Cliente atualizado com sucesso!!!")
  else:
    print("Operação Invalida")


def listar(seletor_menu):
  cursor = con.cursor()
  if (seletor_menu == "T_P"):
    sql_produto = "SELECT * FROM produto"
    cursor.execute(sql_produto)
    lista = cursor.fetchall()
    for registro in lista:
      print("-------------")
      print("ID: ",registro[0])
      print("Descricao: ",registro[1])
      print("Valor: ",registro[2])
      print("Quantidade: ",registro[3])
      print("-------------")
    cursor.close()

  elif (seletor_menu == "T_C"):
    sql_cliente = "SELECT * FROM Cliente"
    cursor.execute(sql_cliente)
    lista = cursor.fetchall()
    for registro in lista:
      print("-------------")
      print("ID: ",registro[0])
      print("Nome: ",registro[1])
      print("Telefone: ",registro[2])
      print("-------------")
    cursor.close()
  elif (seletor_menu == "T_V"):
    sql_cliente = "SELECT nome,descricao FROM cliente,produto,venda WHERE cliente.id=venda.id_cliente AND produto.id=venda.id_produto"
    cursor.execute(sql_cliente)
    lista = cursor.fetchall()
    for registro in lista:
      print("-------------")
      print("Nome: ",registro[0])
      print("Produto Comprado: ",registro[1])
      print("-------------")
    cursor.close()
  else:
    print("Opção Desconhecida")


def remover(seletor_menu):
  listar(seletor_menu)
  cursor = con.cursor()
  if (seletor_menu == "T_P"):
    id_remover = input("Informe o numero do produto que deseja remover: ")
    cursor.execute("DELETE FROM produto WHERE id=?",(id_remover))
    con.commit()
    cursor.close()
  elif (seletor_menu == "T_C"):
    id_remover = input("Informe o numero de registro do cliente que deseja remover: ")
    cursor.execute("DELETE FROM cliente WHERE id=?",(id_remover))
    con.commit()
    cursor.close()
  else:
    print("Função Invalida")


def vendas():
  cursor = con.cursor()
  listar("T_P")
  id_produto = input("Informe o numero de registro Produto: ")
  listar("T_C")
  id_cliente = input("Informe o numero de registro do cliente: ")
  cursor.execute("INSERT INTO venda (id_cliente,id_produto) VALUES(?,?)", (id_cliente,id_produto))
  cursor.execute("UPDATE produto SET quantidade=quantidade-1 WHERE id=?", (id_produto))
  con.commit()
  cursor.close()
  print("Venda realizada com sucesso")
