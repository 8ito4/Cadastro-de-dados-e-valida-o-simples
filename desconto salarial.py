salario = float(input('informe o salario a ser descontado:'))

if salario < 500:
    print ('o desconto será de', salario * 0.15)
elif salario >= 500 and salario <= 1000:
    print ('o desconto será de',salario * 0.10)
else:
    print ('o desconto será de',salario * 0.05)