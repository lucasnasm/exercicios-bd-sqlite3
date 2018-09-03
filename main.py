#Chamada de funções
from funcoesBd import *

#Inicio FLAGS
FLAG_LOOP = True
FLAG_MSG = "***-Opção invalida, tente novamente-***"
#Fim FLAGS

opcao=10


while (FLAG_LOOP):
  try:
    menuApresentacao()
    opcao = int(input("Informe uma opção para iniciar: \n"))
  except KeyboardInterrupt:
    print("")
    print(" Ops! Para sair utilize a opção 0 ;)")
    print("")
  except ValueError:
    print("")
    print("Não entendi, digite uma das opções do menu para iniciar")
    print("")
  else:
    if(opcao==0):
      con.close()
      break
    while(opcao!=0):
      if (opcao==1):
        if(menuClientes()):
          break
      elif (opcao==2):
        if(menuProdutos()):
          break
      elif (opcao==3):
        if (menuVendas()):
          break
      else:
        print(FLAG_MSG)
        break
