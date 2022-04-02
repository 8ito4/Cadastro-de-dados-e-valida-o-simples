from random import randint
from time import sleep
print ('-=' * 10)
print ('\033[1;31mJOGO DA ADIVINHAÇÃO\033[m')
print ('-=' * 10)
sleep(4)
print ('\033[1;32mComo jogar:\033[m o computador irá pensar em um número de 1 a 10 \n e você vai ter que adivinhar, preparado? Vamos la!')
sleep (7)
print ('\033[1;30;47mcomputador está pensando em um número de 1 a 10...\033[m')
sleep(4)
computador = randint(1, 10)
numero = False
resposta = 0
while not numero:
    jogador =  (int(input('Agora diga um número de 1 a 10:')))
    resposta += 1
    if jogador == computador:
        numero = True
        if numero == True:
            print('\033[4;32mPARABÉNS, VOCÊ ACERTOU COM {} TENTATIVAS!\033[m'.format(resposta))
            repetir = str(input('Deseja jogar mais uma vez? [SIM/NÃO]')).strip()
    else:
        if jogador < computador:
            print ('\033[1;31mErrou!\033[m Dica: maior um pouquinho')
        elif jogador > computador:
            print ('\033[1;31mErrou!\033[m Dica: menor um pouquinho')

while repetir in 'simSIM':
    computador = randint(1, 10)
    numero = False
    resposta = 0
    jogador = (int(input('Agora diga um número de 1 a 10:')))
    resposta += 1
    if jogador == computador:
        numero = True
        if numero == True:
            print('\033[4;32mPARABÉNS, VOCÊ ACERTOU COM {} TENTATIVAS!\033[m'.format(resposta))
        repetir = str(input('Deseja jogar mais uma vez? [SIM/NÃO]')).strip()
    else:
        if jogador < computador:
            print ('\033[1;31mErrou!\033[m Dica: maior um pouquinho')
        elif jogador > computador:
            print ('\033[1;31mErrou!\033[m Dica: menor um pouquinho')

if repetir == 'nãoNÃOnaoNAO' :
    print ('obrigado por jogar, volte sempre.')
else:
    print ('Não identificamos sua resposta, digite novamente: ')



