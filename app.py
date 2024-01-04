import os

depositos = []
saques = []

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = """---EXTRATO---
"""
numero_saques = 0
LIMITE_SAQUES = 3


os.system('cls')
print('SEJA BEM VINDO!')
while True:

    opcao = input(menu).casefold()

    if opcao == "d":
        os.system('cls')
        while True:
            try:
                valor = float(input('Qual valor deseja depositar? '))
                valor_ajustado = '{:_.2f}'.format(valor).replace('.', ',').replace('_', '.')
                if valor > 0:
                    os.system('cls')
                    print(f'Depósito de R$ {valor_ajustado} realizado!')
                    depositos.append(valor)
                    saldo+=valor
                    valor_alinhado = "R$"+f"{valor_ajustado}".rjust(10)
                    extrato+=f"{valor_alinhado}\n"
                    break
                else: 
                    os.system('cls')
                    print('Operação falhou! O valor deve ser maior que zero!')
            except ValueError:
                os.system('cls')
                print('Operação falhou! Por favor, insira um valor válido.')
                
    
    elif opcao == "s":
        os.system('cls')
        while True:
            try:
                valor = float(input('Qual valor deseja sacar? '))
                valor_ajustado = '{:_.2f}'.format(valor).replace('.', ',').replace('_', '.')
                if valor > saldo:
                    os.system('cls')
                    print('Operação falhou! Saldo insuficiente!')
                    break
                elif valor > limite:
                    os.system('cls')
                    print('Operação falhou! Limite insuficiente! [R$500,00 por saque]')
                    break
                elif LIMITE_SAQUES == numero_saques:
                    os.system('cls')
                    print('Operação falhou! Limite de saques atingido! [3 saques por dia]')
                    break
                else:
                    if valor > 0:
                        os.system('cls')
                        print(f'Saque de R$ {valor_ajustado} realizado!')
                        saques.append(-valor)
                        saldo-=valor
                        numero_saques+=1
                        valor_alinhado = "R$"+f"-{valor_ajustado}".rjust(10)
                        extrato+=f"{valor_alinhado}\n"
                        break
                    else: 
                        os.system('cls')
                        print('Operação falhou! O valor deve ser maior que zero!')
            except ValueError:
                os.system('cls')
                print('Operação falhou! Por favor, insira um valor válido.')

    elif opcao == "e":
        os.system('cls')
        saldo_ajustado = '{:_.2f}'.format(saldo).replace('.', ',').replace('_', '.')
        saldo_alinhado = "R$"+f"{saldo_ajustado}".rjust(10)
        if extrato == """---EXTRATO---
""":
            print('Não foram realizadas movimentações!')
        else:
            while True:
                print(extrato + f"""----SALDO----
{saldo_alinhado}""")
                try:
                    continuar = int(input('\nAperte [1] para continuar: '))
                    if continuar == 1:
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Informe uma opção válida!')
                except ValueError:
                    os.system('cls')
                    print('Por favor, insira um valor válido.')
        

    elif opcao == "q":
        os.system('cls')
        break

    else:
        os.system('cls')
        print('Operação inválida, por favor selecione novamente a operação desejada!')

print('Você saiu.')