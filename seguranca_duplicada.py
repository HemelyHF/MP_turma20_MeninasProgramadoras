# -*- coding: utf-8 -*-
digitos = int(input())
something = ''
senha = 'true'

for nada in range(digitos):
  algo = input()
          
  if algo in something:
    senha = 'false'

  something = something + algo
          
if senha == 'false':
    print("ERRO")
else:
  print("OK")
