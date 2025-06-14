dinheiro = input()
dinheiro = float(dinheiro)
gasto = 0
contador = 0
while gasto < dinheiro:
      produto = float(input())
      economia = int(input())
      multiplicaçao = produto * economia
      divisao = multiplicaçao / 100
      liquido = produto - divisao
      gasto += liquido
      if gasto > dinheiro:
        gasto -= liquido
        break
      else:
        contador += 1

print('%.2f' % gasto)
print(contador)

*.python linguist-detectable=true
