nome = str(input('digite seu nome'))
while len (nome) <= 3:
    print ('nome invalido')
    nome = str(input('digite novamente'))

idade = int(input('qual sua idade?'))
while idade > 150 or idade < 0:
    print ('idade invalida')
    idade = int(input('diga novamente sua idade'))

salario = float(input('informe seu salario'))
while salario < 0:
    print ('salario invalido')
    salario=float(input('informe novamente o salario'))


sexo = str(input('Digite seu sexo:')).upper()
while sexo != 'F' and sexo != 'M':
    print ('sexo invalido')
    sexo = str(input('Digite novamente seu sexo')).upper()


ec = str(input('informe seu estado civil'))
while (ec != "s" and ec != "c" and ec != "v" and ec != "d"):
    print ('estado civil invalido')
    ec = str(input('informe novamente seu estado civil'))

print (f'seu nome é {nome}, sua idade é {idade}, seu salario é {salario}, seu sexo é {sexo} e seu estado civil é {ec}.')