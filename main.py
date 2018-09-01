#Chamada de funções
from funcoesBd import *

#Inicio FLAGS
FLAG_LOOP = True
FLAG_MSG = "***-Opção invalida, tente novamente-***"
#Fim FLAGS

opcao=10


while (FLAG_LOOP):
  menuApresentacao()
  opcao = int(input("Informe uma opção para iniciar: \n"))
  if(opcao==0):
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

 
   
