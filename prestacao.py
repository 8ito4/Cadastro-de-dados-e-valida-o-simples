casa = int(input('qual valor da casa?'))
salario = int(input('qual salario?'))
ano = int(input('quantos anos deseja pagar?'))

prestacao = casa / (ano * 12)
porcento = salario * 0.30

if prestacao > porcento:
    print ('emprestimo negado')
else:
    print ('emprestimo aprovado')

