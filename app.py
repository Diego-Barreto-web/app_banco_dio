import os

usuarios = []
lista_cpf = []
contas = {}
numero_conta = 0
i=1

def verifica_ncebl(verifica):
    while True:
        if len(verifica.strip().capitalize()) < 3:
            os.system('cls')
            print('O nome deve ter mais de 3 ou mais caracteres!')
            verifica = input('Informe corretamente: ').strip().capitalize()
            continue
        else:
            break
    return verifica.strip().capitalize()   

def verifica_cpf(verifica):
    while True:
        try:
            cpf_sem_pontos = verifica.replace('.', '').replace('-', '').replace(' ', '')
            if len(cpf_sem_pontos)==11 and cpf_sem_pontos.isnumeric():
                verifica = cpf_sem_pontos
                break
        except ValueError:
            os.system('cls')
            verifica = input('Digite seu CPF corretamente (apenas números com ou sem pontos): ')
            continue
        else:
            os.system('cls')
            verifica = input('Digite seu CPF corretamente (apenas números com ou sem pontos): ')
            continue
    return verifica

def verifica_numero(verifica):
    while True:
        if verifica.isnumeric():
            break
        else:
            os.system('cls')
            verifica = input('Informe o dia corretamente: ')
            continue
    return verifica

def cadastrar_usuario(cpfs_users):
    nome = input('Informe seu nome: ')
    nome = verifica_ncebl(nome)
    
    os.system('cls')
    dia_nascimento = input('Informe o dia de nascimento (xxxx): ')
    dia_nascimento = verifica_numero(dia_nascimento)
    mes_nascimento = input('Informe o mês de nascimento (xxxx): ')
    mes_nascimento = verifica_numero(mes_nascimento)
    ano_nascimento = input('Informe o ano de nascimento (xxxx): ')
    ano_nascimento = verifica_numero(ano_nascimento)
    data_de_nascimento = '{}/{}/{}'.format(dia_nascimento, mes_nascimento, ano_nascimento)

    os.system('cls')
    cpf = input('Informe o CPF (pode conter a ponutação): ')
    cpf = verifica_cpf(cpf)
    cpfs_users = cpf


    os.system('cls')
    logradouro = input('Informe o logradouro: ')
    logradouro = verifica_ncebl(logradouro)

    numero = input('Informe o número da casa: ')

    bairro = input('Informe o bairro: ')
    bairro = verifica_ncebl(bairro)

    cidade = input('Informe a cidade: ')
    cidade = verifica_ncebl(cidade)

    estado = input('Informe o estado: ')
    estado = verifica_ncebl(estado)
    os.system('cls')

    endereço_completo = '{}, {} - {} - {} {}'.format(logradouro, numero, bairro, cidade, estado)
    
    return {'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'logradouro': logradouro, 'numero': numero, 'bairro': bairro, 'cidade': cidade, 'estado': estado, 'endereço_completo': endereço_completo}, cpfs_users

def criar_conta_corrente(cpf):
    if cpf in lista_cpf[:]:
        # indice_usuario = lista_cpf.index(cpf)
        return True
    else:
        return False
    
def saque_deposito(operacao, num, l):
    os.system('cls')
    while True:
        try:
            if num == 1:
                valor = float(input('Qual valor deseja depositar? '))
            elif num == 2:
                valor = float(input('Qual valor deseja sacar? '))
                if contas.get(conta)[int(numero_da_conta)-1][l] >= contas.get(conta)[int(numero_da_conta)-1]['limite diario']:
                    os.system('cls')
                    print('Limite de saques excedido!')
                    break
                elif valor > contas.get(conta)[int(numero_da_conta)-1]['limite saque']:
                    os.system('cls')
                    print('Seu limite de saque é de R${:,.2f}'.format(contas.get(conta)[int(numero_da_conta)-1]['limite saque']))
                    break
                if valor > contas.get(conta)[int(numero_da_conta)-1]['saldo']:
                    os.system('cls')
                    print('Saldo insuficiente!')
                    break
            valor_ajustado = '{:_.2f}'.format(valor).replace('.', ',').replace('_', '.')
            if valor > 0:
                os.system('cls')
                contas.get(conta)[int(numero_da_conta)-1][operacao].append(valor)
                if num == 1:
                    print(f'Depósito de R$ {valor_ajustado} realizado!')
                    contas.get(conta)[int(numero_da_conta)-1]['saldo'] += valor
                    valor_alinhado = "R$"+f"{valor_ajustado}".rjust(10)
                elif num == 2: 
                    print(f'Saque de R$ {valor_ajustado} realizado!')
                    contas.get(conta)[int(numero_da_conta)-1]['saldo'] -= valor
                    valor_alinhado = "R$"+f"-{valor_ajustado}".rjust(10)
                    contas.get(conta)[int(numero_da_conta)-1][l] += 1
                contas.get(conta)[int(numero_da_conta)-1]['extrato']+=f"{valor_alinhado}\n"
                break
            else: 
                os.system('cls')
                print('Operação falhou! O valor deve ser maior que zero!')
        except ValueError:
            os.system('cls')
            print('Operação falhou! Por favor, insira um valor válido.')

def verificar_existencia_conta(i):
    if(criar_conta_usuario not in contas):
        contas[criar_conta_usuario] = [{'número': i, 'agencia': '0001', 'saques': [], 'depositos': [], 'extrato': '', 'saldo': 0, 'limite diario': 3,'limite usado': 0, 'limite saque': 500}]
        os.system('cls')
        print('Conta criada com sucesso!')
    else: 
        contas[criar_conta_usuario].append({'número': i, 'agencia': '0001', 'saques': [], 'depositos': [], 'extrato': '', 'saldo': 0, 'limite diario': 3, 'limite usado': 0, 'limite saque': 500})
        os.system('cls')
        print('Conta criada com sucesso!')



while True:
    print('SEJA BEM VINDO!')
    print("""------------------------
[1] Cadastrar Usuário
[2] Criar Conta Corrente
[3] Entrar na Conta
[4] Excluir Usuário
[5] Excluir Conta
[6] Sair
------------------------    """)
    opcao = int(input())

    if opcao == 1:
        # criar usuario
        os.system('cls')
        usuario = [cadastrar_usuario(lista_cpf)]
        print('Usuário criado com sucesso!')
        continue
    elif opcao == 2:
        # criar conta corrente
        os.system('cls')
        lista_cpf.append(usuario[0][-1])
        usuarios += usuario[0][:-1]

        criar_conta_usuario = input('informe o cpf: ')
        criar_conta_corrente(criar_conta_usuario)
        if criar_conta_corrente(criar_conta_usuario) == True:
            verificar_existencia_conta(i)
            i+=1
            print(contas)
            input()
        else:
            print('Usuário não existente!')
            print(criar_conta_usuario)
            continue
    elif opcao == 3:
        # contas.get(conta)
        os.system('cls')
        conta = input('Informe o cpf da conta que deseja entrar: ')
        if conta in contas:
            indice_usuario = lista_cpf.index(conta)
            print('Seja bem vindo, {}!'.format(usuarios[indice_usuario]['nome']))
            if len(contas.get(conta)) > 1: 
                n = 1
                for cont in range (len(contas.get(conta))):
                    print('[{}] - Saldo: {}'.format(n, contas.get(conta)[cont]['saldo']))
                    n+=1
                numero_da_conta = input('Selecione a conta: ')
            os.system('cls')
            print('Número da conta: {}'.format(contas.get(conta)[int(numero_da_conta)-1]))
            print(contas.get(conta)[int(numero_da_conta)-1])
            while True:
                print("""------------------------
[1] Depositar
[2] Sacar
[3] Extrato                      
[4] Sair
------------------------    """)
                opcao = int(input())
                if opcao == 1:
                    os.system('cls')
                    saque_deposito('depositos', opcao, 'limite usado')
                elif opcao == 2:
                    os.system('cls')
                    saque_deposito('saques', opcao, 'limite usado')
                elif opcao == 3:
                    os.system('cls')
                    print('----------EXTRATO----------')
                    print(contas.get(conta)[int(numero_da_conta)-1]['extrato'])
                    print('-----------SALDO-----------')
                    print("R$"+f"{contas.get(conta)[int(numero_da_conta)-1]['saldo']}\n".rjust(10))
                if opcao == 4:
                    os.system('cls')
                    break
        else:
            print('Conta não cadastrada!')
    elif opcao == 6:
        os.system('cls')
        break
    else: 
        os.system('cls')
        print('Opção inválida!')
        continue
print('Finalizou')



# depositos = []
# saques = []

# menu = """
# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# """

# saldo = 0
# limite = 500
# extrato = """---EXTRATO---
# """
# numero_saques = 0
# LIMITE_SAQUES = 3


# os.system('cls')
# print('SEJA BEM VINDO!')
# while True:

#     opcao = input(menu).casefold()

#     if opcao == "d":
        # os.system('cls')
        # while True:
        #     try:
        #         valor = float(input('Qual valor deseja depositar? '))
        #         valor_ajustado = '{:_.2f}'.format(valor).replace('.', ',').replace('_', '.')
        #         if valor > 0:
        #             os.system('cls')
        #             print(f'Depósito de R$ {valor_ajustado} realizado!')
        #             depositos.append(valor)
        #             saldo+=valor
        #             valor_alinhado = "R$"+f"{valor_ajustado}".rjust(10)
        #             extrato+=f"{valor_alinhado}\n"
        #             break
        #         else: 
        #             os.system('cls')
        #             print('Operação falhou! O valor deve ser maior que zero!')
        #     except ValueError:
        #         os.system('cls')
        #         print('Operação falhou! Por favor, insira um valor válido.')
                
    
#     elif opcao == "s":
#         os.system('cls')
#         while True:
#             try:
#                 valor = float(input('Qual valor deseja sacar? '))
#                 valor_ajustado = '{:_.2f}'.format(valor).replace('.', ',').replace('_', '.')
#                 if valor > saldo:
#                     os.system('cls')
#                     print('Operação falhou! Saldo insuficiente!')
#                     break
#                 elif valor > limite:
#                     os.system('cls')
#                     print('Operação falhou! Limite insuficiente! [R$500,00 por saque]')
#                     break
#                 elif LIMITE_SAQUES == numero_saques:
#                     os.system('cls')
#                     print('Operação falhou! Limite de saques atingido! [3 saques por dia]')
#                     break
#                 else:
#                     if valor > 0:
#                         os.system('cls')
#                         print(f'Saque de R$ {valor_ajustado} realizado!')
#                         saques.append(-valor)
#                         saldo-=valor
#                         numero_saques+=1
#                         valor_alinhado = "R$"+f"-{valor_ajustado}".rjust(10)
#                         extrato+=f"{valor_alinhado}\n"
#                         break
#                     else: 
#                         os.system('cls')
#                         print('Operação falhou! O valor deve ser maior que zero!')
#             except ValueError:
#                 os.system('cls')
#                 print('Operação falhou! Por favor, insira um valor válido.')

#     elif opcao == "e":
#         os.system('cls')
#         saldo_ajustado = '{:_.2f}'.format(saldo).replace('.', ',').replace('_', '.')
#         saldo_alinhado = "R$"+f"{saldo_ajustado}".rjust(10)
#         if extrato == """---EXTRATO---
# """:
#             print('Não foram realizadas movimentações!')
#         else:
#             while True:
#                 print(extrato + f"""----SALDO----
# {saldo_alinhado}""")
#                 try:
#                     continuar = int(input('\nAperte [1] para continuar: '))
#                     if continuar == 1:
#                         os.system('cls')
#                         break
#                     else:
#                         os.system('cls')
#                         print('Informe uma opção válida!')
#                 except ValueError:
#                     os.system('cls')
#                     print('Por favor, insira um valor válido.')
        

#     elif opcao == "q":
#         os.system('cls')
#         break

#     else:
#         os.system('cls')
#         print('Operação inválida, por favor selecione novamente a operação desejada!')

# print('Você saiu.')