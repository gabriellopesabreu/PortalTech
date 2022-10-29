def calculadora(numero1,numero2,operacao):
  if(operacao == "+"): return numero1 + numero2
  elif(operacao == "-"): return numero1 - numero2
  elif(operacao == "*"): return numero1 * numero2
  elif(operacao == "/") : return numero1 / numero2
  else: return 0  

print(calculadora(5,2,"2"))