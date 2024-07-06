nome = input("Informe o seu nome: ")
Agencia = 1234
Conta = 12345-6

print(f"\n----- BANCO PYTHON -----")
print(f"\nOlá {nome},")
print (f"Seja Bem-Vindo!")
print(f"\nAgência: {Agencia}")
print(f"Conta: {Conta}")


menu = """

█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█      1 - Depositar      █   
█      2 - Sacar          █
█      3 - Extrato        █
█      4 - Sair           █ 
█                         █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

ESCOLHA A OPÇÃO DESEJADA... 
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nOPERAÇÃO REALIZADA COM SUCESSO!\n")
            print("---------------------------")
            print("------ EXTRATO ------")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("---------------------------")

        else:
            print("\nOPERAÇÃO NÃO REALIZADA!\n")
            print("Erro (1A300). Valor Inválido.")

    elif opcao == "2":
        valor = float(input("Valor do Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOPERAÇÃO NÃO REALIZADA!\n")
            print("Erro (1A301). Saldo Insuficiente.")

        elif excedeu_limite:
            print("\nOPERAÇÃO NÃO REALIZADA!\n")
            print("Erro (1A302). Limite Excedido")

        elif excedeu_saques:
            print("\nOPERAÇÃO NÃO REALIZADA!\n")
            print("Erro (1A303). Limite de Saque Excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nOPERAÇÃO REALIZADA COM SUCESSO!\n")
            print("---------------------------")
            print("------ EXTRATO ------")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("---------------------------")

        else:
            print("\nOPERAÇÃO NÃO REALIZADA!\n")
            print("Erro (1A300). Valor Inválido.")

    elif opcao == "3":
        print("\n------ BANCO PYTHON ------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("\nOPERAÇÃO NÃO REALIZADA!\n")
        print("Erro (1A300). Valor Inválido.")
        print("Tente Novamente.")
