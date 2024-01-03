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

    opcao = input(menu).lower()

    if opcao == "d":
        os.system('cls')
        while True:
            try:
                valor = float(input('Qual valor deseja depositar? '))
                if valor > 0:
                    os.system('cls')
                    print(f'Depósito de R$ {valor:.2f} realizado!')
                    depositos.append(valor)
                    saldo+=valor
                    valor_alinhado = "R$"+f"{valor:.2f}".rjust(10)
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
                        print(f'Saque de R$ {valor:.2f} realizado!')
                        saques.append(-valor)
                        saldo-=valor
                        numero_saques+=1
                        valor_alinhado = "R$"+f"-{valor:.2f}".rjust(10)
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
        saldo_alinhado = "R$"+f"{saldo:.2f}".rjust(10)
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