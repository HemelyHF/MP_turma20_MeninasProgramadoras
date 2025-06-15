# -*- coding: utf-8 -*-
alg1 = int(input())
alg2 = int(input())
alg3 = int(input())
alg4 = int(input())

if alg1 > alg2:           # 1
  numero = alg1
  a = alg2
else:
  numero = alg2
  a = alg1

if alg3 > alg4:           # 2
  number = alg3
  al = alg4
else:
  number = alg4
  al= alg3

if numero > number:    # 3
  res = numero
else:
  res = number

if a>al:            # 4
  res2 = al
else:
  res2 = a

res = str(res)
res2 = str(res2)

print('A mais velha tem ' + res)
print('A mais nova tem ' + res2)
