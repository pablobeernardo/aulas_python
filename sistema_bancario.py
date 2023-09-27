import textwrap

def menu():
    menu = '''\n
======================== MENU ========================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova Conta
[lc]\tListar Contas
[nu]\tNova Usuário
[q]\tSair
=======================================================
'''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f'\nDeposito: R$ {valor:.2f}\n'
        print('Deposito realizado com sucesso')

    else:
        print('Valor invalido')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_valor_saque, numero_saques, LIMITE_SAQUES): 
    if valor > 0 and valor <= limite_valor_saque and numero_saques < LIMITE_SAQUES:
        saldo = saldo - valor
        extrato = extrato + f'\nSaque: R$ {valor:.2f}\n'
        numero_saques = numero_saques + 1
        print('Saque realizado com sucesso')

    elif valor > limite_valor_saque:
        print('Valor de saque maior que o limite')

    elif numero_saques >= LIMITE_SAQUES:
        print('Limite de saques atingido')

    else:
        print('Valor invalido')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, / , * , extrato):
    print('=== Extrato ===')
    print(f'Saldo: R$ {saldo:.2f}')
    print(extrato)
    print('===============')


def criar_usuario(usuarios):
    cpf = input('Digite o CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Usuario já existe')
        return 
    
    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento: (dd/mm/aaaa) ')
    endereco = input('Digite o endereco: (logradouro, numero - bairro - cidade/estado) ')

    usuarios.append({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco})
    print('=== Usuário cadastrado com sucesso ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if len(usuarios_filtrados) > 0 else None
   
def criar_conta(agencia, numero_conta, usuarios): 
    cpf = input('Digite o CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n === Conta criada com sucesso ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario} 

    print('Usuario não encontrado, fluxo interrompido') 

def listar_contas(contas):
    print('=== Contas ===')
    for conta in contas:
        linha = f'''\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))    

def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    limite_valor_saque = 500
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor_deposito = float(input('Digite o valor do deposito: '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == 's':
            valor_saque = float(input('Digite o valor do saque: '))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite_valor_saque=limite_valor_saque, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == 'nu':
            criar_usuario(usuarios)    

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print('Conta criada com sucesso')

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Opcao invalida')

if __name__ == '__main__':
    main()



    