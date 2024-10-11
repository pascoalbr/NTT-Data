# Desafio - Criando um Sistema Bancário com Python

MENU = """

#######  Menu  ########
|                     |
|    (d) Depósito     |
|    (s) Saque        |
|    (e) Extrato      |
|    (q) Sair         |
|                     |
#######################

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        saques_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Operação não realizada! Você não possui saldo suficiente.")

        elif limite_excedido:
            print("Operação não realizada! O valor digitado excede o limite de saque.")

        elif saques_excedido:
            print("Operação não realizada! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n**************** EXTRATO ****************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione uma operação válida.")

     
