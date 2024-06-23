saldo_em_conta = 1000
extrato = []
cliente = []
saques_diarios = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_SAQUE_VALOR = 500

def criar_usuario(dicionario):
    for cliente_existente in cliente:
        if cliente_existente["CPF"] == dicionario["CPF"]:
            print("Usuário com esse CPF já existe.")
            return
    cliente.append(dicionario)
    print("Usuário criado com sucesso!")
    print(cliente)

def deposito(valor):
    global saldo_em_conta, extrato
    if valor > 0:
        saldo_em_conta += valor
        extrato.append(f'Depósito: {valor}')
        print(f'''
              Depósito de {valor} realizado com sucesso!
              Saldo disponível: {saldo_em_conta}
              ''')

def saque(valor):
    global saldo_em_conta, extrato, saques_diarios
    
    if saques_diarios >= LIMITE_SAQUES_DIARIOS:
        print(f'Você atingiu o limite de {LIMITE_SAQUES_DIARIOS} saques diários.')
        return
    
    if valor > saldo_em_conta:
        print(f'Saldo insuficiente: {saldo_em_conta}')
        return
    
    if valor > LIMITE_SAQUE_VALOR:
        print(f'Seu limite de saque por operação é R${LIMITE_SAQUE_VALOR},00')
        return
    
    saldo_em_conta -= valor
    extrato.append(f'Saque: {valor}')
    saques_diarios += 1
    print(f'''
          Saque de {valor} realizado com sucesso!
          Saldo disponível: {saldo_em_conta}
          ''')

print("Bem-vindo ao banco X".center(26,"#"))
while True:
    op = int(input('''
    Qual operação deseja fazer hoje?
    Saque: 1
    Depósito: 2
    Consultar Extrato: 3
    Criar conta: 4
    Sair: 0
    '''))
    if op == 1:
        valor = int(input("Qual o valor que deseja sacar? "))
        saque(valor)
    elif op == 2:
        valor = int(input("Qual o valor que deseja depositar? "))
        deposito(valor)
    elif op == 3:
        print("Extrato:")
        for item in extrato:
            print(item)
    elif op == 4:
        nome = input("Digite seu nome:")
        data_nascimento = input("Digite a data de nascimento:")
        cpf = input("Digite seu CPF:")
        endereco = input("Digite seu endereço:")
        dados = {"Nome": nome, "Data de Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco}
        criar_usuario(dados)
    elif op == 0:
        print("Obrigado por usar o banco X. Até a próxima!")
        break
    else:
        print("Opção inválida!")
