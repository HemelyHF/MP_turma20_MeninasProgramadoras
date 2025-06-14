# -*- coding: utf-8 -*-
ma = float(input()) #massa
acel_ini = float(input()) #aceleraçao inicial
contagem_voltas = 0
contador = True

aceleracao_maxima = acel_ini
while contador:
  forca= float(input())
  acel = forca/ ma
  contagem_voltas = contagem_voltas + 1
  if acel < 0:
    contador = False
  elif acel > aceleracao_maxima:
    aceleracao_maxima = acel


print("maior aceleração:", '%.3f' % aceleracao_maxima)
print("número de voltas: ", '%.0f' % contagem_voltas)
