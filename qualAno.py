#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

nome = str(input("Digite o seu nome completo "))
numeroCorreto = False

while (numeroCorreto == False):
  print("Digite o seu ano de nascimento")
  nascimento = int(input())
  try:
    if(nascimento > 1922 and nascimento <2021):
      numeroCorreto = True
      calculo = 2022 - nascimento
      print("Seu nome é {} e você tem ou terá {} em 2022".format(nome, calculo))
    else:
      print("Não é um ano válido")
  except:
    print("Caracter inválido, por favor digite um número par")