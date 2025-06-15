# -*- coding: utf-8 -*-
conta = float(input())

porcentagem = int(input())

gorjeta = (porcentagem / 100) * conta

total = gorjeta + conta
total = float(total)
print('%.2f' % total)
