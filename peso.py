maior = 0
menor = 0
for p in range (1, 6):
    peso = float (input('o peso da {} pessoa'.format((p))))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ('maior peso lido foi de {} kg'.format(maior))
print ('menor peso lido foi de {} kg'.format(menor))