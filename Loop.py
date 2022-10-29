#Exercicio de loop

# Primeira forma

andar = 0
for i in range(20):
    andar = andar + 1
    if(andar != 13):
      print(andar)

# Segunda forma
andar = 21
while (andar > 0):
  andar = andar - 1
  if(andar != 13):
    print(andar)

# Terceira forma (como no python não possui do while, fiz o for decrescente)
andar = 21
for i in range(20,0,-1):
    andar = andar - 1
    if(andar != 13):
      print(andar)