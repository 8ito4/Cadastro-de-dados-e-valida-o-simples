ano = 0
a = 80000
b = 200000
porcetagemA = 0.03
porcetagemB = 0.015

while a <= b:
    a = a + (a * porcetagemA)
    b = b + (b * porcetagemB)
    ano += 1

print ('vai demorar {} anos pra cidade A ultrapassar a cidade B :D'.format(ano))