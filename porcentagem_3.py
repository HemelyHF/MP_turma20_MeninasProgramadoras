produto = int(input())
economia = 0
for something in range(produto):
  valor = float(input())
  desconto = int(input())
  multiplica = valor * desconto
  resp = multiplica / 100
  economia = economia + resp

print('%.2f' % economia)
