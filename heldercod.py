from time import sleep

n1 = ''
opção = 0
nome = ''
email = ''
cargo = ''
salario = 0
dados = (opção, nome, email, cargo, salario)

while opção != 6:
    print('''\033[30;mMENU PRINCIPAL:
     [1] Realizar cadastro''')
    if nome !='':
        print('     [2] Aumentar salario')
        print('     [3] Alterar cargo')
        print('     [4] Alterar e-mail')
        print('     [5] Alterar nome')
    print('     [6] Sair')
    opção = int(input('>>>>Qual é sua opção? '))


    if opção == 1:
        while len(nome) <=3 or nome.count(' ') < 1:
            nome = (input('Nome completo: '))
            if len(nome) <=3:
                print('\033[31mERROR: É necessário ter no minimo 4 caracteres.\033[30;m')
            if nome.count(' ') < 1:
                print('\033[31mERROR: É necessário ter no mínimo duas palavras.\033[30;m')

        while len(email) <=3 or email.count('@') < 1 or email.count('.') < 1:
            email = (input('E-mail: '))
            if len(email) <= 3:
                print('\033[31mERROR: É necessário ter no minimo 3 caracteres.\033[30;m')
            if email.count('@') < 1:
                print('\033[31mERROR: É necessário ter um "@".\033[30;m')
            if email.count('.') < 1:
                print('\033[31mERROR: É necessário ter um ".".\033[30;m')


        cargo = (input('Cargo: '))

        while salario <= 0:
            salario = float(input('Salário: '))
            if salario <= 0:
                print('\033[31mERROR: digite apenas numeros maior que R$0,00.\033[30;m')
            print('Cadastrando no sistema...')
            sleep (2)
            print('Pronto, cadastro feito com sucesso!!!')
            sleep (2)


    elif opção == 2:
        print('Salario antigo: R${:.2f}'.format(salario))
        salario = float(input('Novo salário: '))
        while salario <= 0:
            if salario <= 0:
                print('\033[31mERROR: É necessário ser maior que R$0,00.\033[30;m')
            salario = float(input('Salário: '))
        print('Atualizando...')
        sleep (2)
        print('Atualizado com sucesso!')
        sleep (2)

    elif opção == 3:
        print('Cargo anterior: {}'.format(cargo))
        cargo = input('Digite seu novo cargo: ')
        print('Atualizando...')
        sleep(2)
        print('Atualizado com sucesso!')
        sleep(2)

    elif opção == 4:
        print('E-mail antigo: {}'.format(email))
        email = (input('Digite seu novo e-mail: '))
        while len(email) <= 3 or email.count('@') < 1 or email.count('.') < 1:
            if len(email) <= 3:
                print('\033[31mERROR: É necessário ter no minimo 3 caracteres.\033[30;m')
            if email.count('@') < 1:
                print('\033[31mERROR: É necessário ter um "@".\033[30;m')
            if email.count('.') < 1:
                print('\033[31mERROR: É necessário ter um ".".\033[30;m')
        print('Atualizando...')
        sleep(2)
        print('Atualizado com sucesso!')
        sleep(2)

    elif opção == 5:
        print('Nome antigo: {}'.format(nome))
        nome = (input('Novo nome completo: '))
        while len(nome) <=3 or nome.count(' ') < 1:
            if len(nome) <=3:
                print('\033[31mERROR: É necessário ter no minimo 4 caracteres.\033[30;m')
            if nome.count(' ') < 1:
                print('\033[31mERROR: É necessário ter no mínimo duas palavras.\033[30;m')
        print('Atualizando...')
        sleep(2)
        print('Atualizado com sucesso!')
        sleep(2)


    elif opção == 6:
        print('\033[40mFinalizando...\033[30;m')
        sleep (2)

    else:
        print('\033[31mDigite uma opção válida. Tente novamente.\033[30;m')
    print('=-=' * 10)

cadastro = nome, email, cargo, salario

print('\033[40mSessão finalizada. Volte sempre.\033[30;m')

with open('helder.txt', 'a' ) as arquivo:
    for desafio in cadastro:
        arquivo.write(str(desafio) + '\n')