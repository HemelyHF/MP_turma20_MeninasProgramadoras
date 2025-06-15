# -*- coding: utf-8 -*-
entrada = int(input())

contador = 0
resto = 0
soma = 0

while entrada >= resto:
  compra = int(input())
  soma = soma + compra
 
  if soma <= entrada:
   resto = entrada - soma
   contador = contador + 1

  else:
    resto = float(resto)
    break

if contador == 0:
  resto = entrada

print("Número de itens", contador)
print("Saldo:", '%.2f' % resto)
