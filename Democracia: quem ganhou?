# -*- coding: utf-8 -*-
quant_votos = int(input()) #democracia
cand1 = 0
cand2 = 0
branco = 0
nulo = 0

for something in range(quant_votos):
  votos = str(input())
  if votos == "Y":
    cand1 = cand1 + 1

  elif votos == "X":
    cand2 = cand2 + 1

  elif votos == "N":
    nulo = nulo + 1

  elif votos == "B":
    branco = branco + 1

print("X", cand2)
print("Y", cand1)
print("Brancos e nulos", branco + nulo)

if cand1 > cand2:
  resposta = 'vitoria: Y'
elif cand2 > cand1:
  resposta = 'vitoria: X'
else:
  resposta = 'empate!'

print(resposta)
