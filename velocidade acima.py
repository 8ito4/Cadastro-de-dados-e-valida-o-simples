velocidade = int(input('qual velocidade o carro está correndo?'))
km = 7
multa = (velocidade-80)*km
if velocidade > 80:
    print ('você foi multado!')
    print ('voce foi multade em {} reais'.format(multa))
else:
    print ('parabens, vc anda correto')
print('ande com cuidado!')