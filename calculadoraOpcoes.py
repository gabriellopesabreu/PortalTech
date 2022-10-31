def calculadora(numer1, number2):
 opcao = ""
 while opcao != 0:
   print('''
   1: Soma
   2: Subtração
   3: Multiplicação
   4: Divisão
   0: Sair''')
   opcao = input("Qual a opção desejada? ")
   if(opcao == "1"):
    print(number1 + number2)
   elif(opcao == "2"):
    print(number1 - number2)
   elif(opcao == "3"):
    print(number1 * number2)
   elif(opcao == "4"):
    print(number1 / number2)
   elif(opcao == "0"):
    return("Saindo do programa")
   else:
    print("Opção inválida. Tente novamente")


print(calculadora(number1,number2))