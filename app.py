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
    while True:
        if cpf in lista_cpf[:]:
            os.system('cls')
            print('CPF já cadastrado!')
            if deseja_continuar() == True:
                cpf = input('Informe o CPF (pode conter a ponutação): ')
                continue
            else: 
                cpf = '0'
                break
        else:
            cpf = verifica_cpf(cpf)
            cpfs_users = cpf
            break
    
    if cpf != '0':
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
        return {'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'logradouro': logradouro, 'numero': numero, 'bairro': bairro, 'cidade': cidade, 'estado': estado, 'endereço_completo': endereço_completo}, True, cpfs_users
    else: 
        return {'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf}, False, cpfs_users

def criar_conta_corrente(cpf):
    if cpf in lista_cpf[:]:
        # indice_usuario = lista_cpf.index(cpf)
        return True
    else:
        return False
    
def excluir_conta_corrente():
    del contas.get(conta)[int(numero_da_conta)-1]

def menu_conta():
    while True:
        print("""------------------------
[1] Depositar
[2] Sacar
[3] Transferir
[4] Extrato                      
[5] Sair
------------------------    """)
        opcao = int(input())
        if opcao == 1:
            os.system('cls')
            print('Opção depósito escolhida.')
            if deseja_continuar() == True:
                os.system('cls')
                saque_deposito('depositos', opcao, 'limite usado')
            else: 
                os.system('cls')
                print('O depósito não foi realizado!')
        elif opcao == 2:
            os.system('cls')
            print('Opção saque escolhida.')
            if deseja_continuar() == True:
                os.system('cls')
                saque_deposito('saques', opcao, 'limite usado')
            else:
                os.system('cls')
                print('O saque não foi realizado')
        elif opcao == 3:
            transferencia()
        elif opcao == 4:
            os.system('cls')
            print('----------EXTRATO----------')
            print(contas.get(conta)[int(numero_da_conta)-1]['extrato'])
            print('-----------SALDO-----------')
            print("R$"+f"{contas.get(conta)[int(numero_da_conta)-1]['saldo']}\n".rjust(10))
        elif opcao == 5:
            os.system('cls')
            break
        else:
            print('Conta não cadastrada!')
    
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

def transferencia():
    os.system('cls')
    valor = float(input('Informe o valor que deseja transferir: '))
    if valor > 0:
        if valor <= contas.get(conta)[int(numero_da_conta)-1]['saldo']:
            valor_ajustado = '{:_.2f}'.format(valor).replace('.', ',').replace('_', '.')
            conta_beneficente = input('Informe o CPF da conta que receberá o dinheiro: ')
            conta_beneficente = verifica_cpf(conta_beneficente)
            if conta_beneficente in lista_cpf[:]:
                listar_contas_transferir(conta_beneficente)
                conta_transferencia = int(input())
                contas.get(conta)[int(numero_da_conta)-1]['saldo'] -= valor
                contas.get(conta)[int(numero_da_conta)-1]['transferências'].append(valor_ajustado)
                valor_alinhado = "R$"+f"-{valor_ajustado}*".rjust(10)
                contas.get(conta)[int(numero_da_conta)-1]['extrato']+=f"{valor_alinhado}\n"

                contas.get(conta_beneficente)[int(conta_transferencia)-1]['saldo'] += valor
                contas.get(conta_beneficente)[int(conta_transferencia)-1]['depositos'].append(valor_ajustado)
                valor_alinhado = "R$"+f"-{valor_ajustado}*".rjust(10)
                contas.get(conta_beneficente)[int(conta_transferencia)-1]['extrato']+=f"{valor_alinhado}\n"
            else:
                print('Conta inexistente!')
    else: 
        print('Operação não concluida! Saldo insuficiente!')


def verificar_existencia_conta(i):
    if(criar_conta_usuario not in contas):
        contas[criar_conta_usuario] = [{'número': i, 'agencia': '0001', 'saques': [], 'depositos': [], 'transferências': [], 'extrato': '', 'saldo': 0, 'limite diario': 3,'limite usado': 0, 'limite saque': 500}]
        os.system('cls')
        print('Conta criada com sucesso!')
    else: 
        contas[criar_conta_usuario].append({'número': i, 'agencia': '0001', 'saques': [], 'depositos': [], 'transferências': [], 'extrato': '', 'saldo': 0, 'limite diario': 3, 'limite usado': 0, 'limite saque': 500})
        os.system('cls')
        print('Conta criada com sucesso!')

def excluir_usuario(usuario):
    indice = lista_cpf.index(usuario)
    usuarios.pop(indice)
    lista_cpf.pop(indice)
    del contas[usuario]

def listar_contas(conta):
    indice_usuario = lista_cpf.index(conta)
    print('Seja bem vindo, {}!'.format(usuarios[indice_usuario]['nome'])) 
    n = 1
    for cont in range (len(contas.get(conta))):
        print('[{}] - Saldo: {}'.format(n, contas.get(conta)[cont]['saldo']))
        n+=1

def listar_contas_transferir(conta):
    indice_usuario = lista_cpf.index(conta)
    print('Informe a conta de, {} que receberá a transferência!'.format(usuarios[indice_usuario]['nome'])) 
    n = 1
    for cont in range (len(contas.get(conta))):
        print('[{}] - Saldo: {}'.format(n, contas.get(conta)[cont]['saldo']))
        n+=1

def deseja_continuar():
    while True:
        print("""Deseja continuar?
              
[1] Continuar
[2] Voltar""")
        d_continuar = int(input())
        try: 
            if d_continuar == 1:
                return True
            elif d_continuar == 2:
                return False
        except ValueError:
            os.system('cls')
            print('Informe a opção corretamente!')



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
        if usuario[0][1] == False :
            os.system('cls')
            print('Usuário não cadastrado!\nEsse CPF já havia sido cadastrado!')
        else: 
            usuarios += usuario[0][:-2]
            lista_cpf.append(usuario[0][-1])
            print('Usuário criado com sucesso!')
            print(usuario[0][-1])
            print(usuarios)
    elif opcao == 2:
        # criar conta corrente
        os.system('cls')

        criar_conta_usuario = input('informe o cpf: ')
        criar_conta_usuario = verifica_cpf(criar_conta_usuario)
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
        conta = verifica_cpf(conta)
        if conta in contas:
            listar_contas(conta)
            numero_da_conta = input('Selecione a conta: ')
            os.system('cls')
            print('Número da conta: {}'.format(contas.get(conta)[int(numero_da_conta)-1]))
            print(contas.get(conta)[int(numero_da_conta)-1])
            menu_conta()  

    elif opcao == 4:
        usuario = input('Informe o cpf do usuário que deseja excluir: ')
        usuario = verifica_cpf(usuario)
        if usuario in lista_cpf:
            os.system('cls')
            excluir_usuario(usuario)
        else:
            os.system('cls')
            print('Usuário não cadastrado!')

    elif opcao == 5:
        conta = input('Informe o cpf da conta que deseja entrar: ')
        conta = verifica_cpf(conta)
        if conta in contas:
            listar_contas(conta)
            numero_da_conta = input('Selecione a conta que deseja excluir: ')
            os.system('cls')
            print('Número da conta: {}'.format(contas.get(conta)[int(numero_da_conta)-1]))
            print(f'Conta de número {contas.get(conta)[int(numero_da_conta)-1]["número"]} excluida!')
            excluir_conta_corrente()
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



#----------------------------------Primeira Atividade----------------------------------

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