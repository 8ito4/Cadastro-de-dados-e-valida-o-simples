from time import sleep
opcao = ''
nome = ''
salario = 0
email = ''
cargo = ''
novo_salario = 0
novo_cargo = ''
novo_email = ''

def aumentar_salario ():
    print ('Seu salário atual é {}'.format(salario))
    novo_salario = float(input('Digite qual salario que você deseja ganhar: '))
    while novo_salario <= salario or novo_salario < 1:
        print ('O salário não pode ser menor que o atual e não pode ser menor que 1. ')
        novo_salario = float(input('Por favor digite um novo salário: '))
    print ('Novo reajuste de salário solicitado.')
    return novo_salario

def alterar_cargo ():
    print ('Seu cargo atual é {}.'.format(cargo))
    novo_cargo = input('Digite um novo cargo: ')
    while cargo == novo_cargo:
        print ('O cargo escolhido é igual ao atual')
        novo_cargo = input('Por favor digite um novo cargo: ')
    print ('Novo cargo solicitado.')
    return novo_cargo

def alterar_email ():
    print ('Seu E-mail atual é {}'.format(email))
    novo_email = input('Digite um novo E-mail: ')
    while novo_email == email or len(novo_email) <= 5 or novo_email.count('@') < 1 or novo_email.count('.') < 1:
        print('Novo E-mail inválido!'
              'O e-mail deverá ter:\n'
              '- No mínimo 05 caracteres\n'
              '- Não poderá ser igual ao atual\n'
              '- 01 "@"\n'
              '- No mínimo 01 "."')
        novo_email = input('Por favor digite um novo E-mail: ')
    print ('Novo E-mail solicitado.')
    return novo_email

print('escolha uma opção no menu:\n'
      'a) Realizar cadastro\n'
      'b) sair')

opcao = input('Digite uma opção: ')

if opcao == 'a':
    print ('Faça seu cadastro:')
    nome = input('Digite seu nome completo: ')
    while len(nome) <= 5 or nome.count(' ') < 1:
        print ('Nome invalido\n'
               'O nome deverá ter:\n'
               '- No mínimo 05 caracteres\n'
               '- No mínimo 02 palavras')
        nome = input('Digite novamente seu nome completo: ')

    email = (input('Digite novamente o E-mail: '))
    while len(email) <= 5 or email.count('@') < 1 or email.count('.') < 1:
        print('E-mail inválido!'
              'O e-mail deverá ter:\n'
              '- No mínimo 05 caracteres\n'
              '- 01 "@"\n'
              '- No mínimo 01 "."')
        email = (input('Digite novamente o E-mail: '))

    cargo = input('Digite seu Cargo: ')
    while len(cargo) <= 1:
        print ('Cargo inválido!\n'
               'O cargo deverá conter no mínimo 02 caracteres.')
        cargo = input('Digite novamente seu Cargo: ')

    salario = float(input('Digite seu salário: '))
    while salario < 1:
        print('Número inválido, o salário não pode ser menor do que 1.')
        salario = float(input('Digite novamente seu salário: '))

    print('Cadastro feito com sucesso!')
    print('Carregando...')
    sleep(3)
    print('Dados cadastrados com sucesso!')

    while opcao != 'd':
        print('-=' * 18)
        print('Bem-vindo a central do funcionário')
        print('-=' * 18)
        print('escolha uma opção no menu:\n'
              'a) Aumentar salário\n'
              'b) Alterar cargo\n'
              'c) Alterar e-mail\n'
              'd) Sair')
        opcao = input('Digite a opção: ')
        if opcao == 'a':
            salario = aumentar_salario()
        elif opcao == 'b':
            cargo = alterar_cargo()
        elif opcao == 'c':
            email = alterar_email()
        elif opcao == 'd':
            print('Armazenando dados...')
            sleep(4)
            print('Todos os dados foram validados!')

            print('CADASTRO ATUALIZADO')

            print('Nome completo é: {}'.format(nome))
            print('Email é: {} '.format(email))
            print('Cargo é: {}'.format(cargo))
            print('Salário é: {}'.format(salario))

cadastro = nome, email, cargo, salario

if opcao == 'b':
    print('Obrigado por visitar o site, volte sempre.')

with open('desafio final.txt', 'a' ) as arquivo:
    for desafio in cadastro:
        arquivo.write(str(desafio) + '\n')
















