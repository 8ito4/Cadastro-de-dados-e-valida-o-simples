precoProduto = input("Qual o preço do produto? ")
valorPago = input("Qual foi o valor pago? ")

troco = float(valorPago) - float(precoProduto)

n100 = int(troco / 100)
troco = troco % 100

n50 = int(troco / 50)
troco = troco % 50

n20 = int(troco / 20)
troco = troco % 20

n10 = int(troco / 10)
troco = troco % 10

n5 = int(troco / 5)
troco = troco % 5

n2 = int(troco / 2)
troco = troco % 2

m1 = int(troco / 1)
troco = troco % 1

m50 = int(troco / 0.5)
troco = troco % 0.5

m25 = int(troco / 0.25)
troco = troco - 0.25

m10 = int(troco / 0.10)
troco = troco % 0.10

m5 = int(troco / 0.05)
troco = troco % 0.05

m01 = int(troco / 0.01)
troco = troco % 0.01

print("Quantidade de notas de 100 reais: ", n100)
print("Quantidade de notas de 50 reais: ", n50)
print("Quantidade de notas de 20 reais: ", n20)
print("Quantidade de notas de 10 reais: ", n10)
print("Quantidade de notas de 5 reais: ", n5)
print("Quantidade de notas de 2 reais: ", n2)
print("Quantidade de moedas de 1 real: ", m1)
print("Quantidade de moedas de 50 centavos: ", m50)
print("Quantidade de moedas de 25 centavos: ", m25)
print("Quantidade de moedas de 10 centavos: ", m10)
print("Quantidade de moedas de 5 centavos: ", m5)
print("Quantidade de moedas de 1 centavo: ", m01)