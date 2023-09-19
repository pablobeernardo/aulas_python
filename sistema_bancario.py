menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

'''

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu) 

    if opcao == 'd':
        valor_deposito = float(input('Digite o valor do deposito: '))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato = extrato + f'\nDeposito: R$ {valor_deposito:.2f}\n'
        else:
            print('Valor invalido')
    
    elif opcao == 's':
        valor_saque = float(input('Digite o valor do saque: '))
        if valor_saque > 0 and valor_saque <= limite_valor_saque and numero_saques < LIMITE_SAQUES:
            saldo = saldo - valor_saque
            extrato = extrato + f'\nSaque: R$ {valor_saque:.2f}\n'
            numero_saques = numero_saques + 1

        elif valor_saque > limite_valor_saque:
            print('Valor de saque maior que o limite')

        elif numero_saques >= LIMITE_SAQUES:
            print('Limite de saques atingido')

        else:
            print('Valor invalido')

    elif opcao == 'e':
        print(f'Extrato: {extrato}')
        print("")
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == 'x':
        break

    else:
        print('Opcao invalida')




