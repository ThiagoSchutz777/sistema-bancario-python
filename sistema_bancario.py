menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        
        else:
            print("ERRO! VALOR INVÁLIDO!")     

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$"))

        exedeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite

        exedeu_Saque = numero_saques >= LIMITE_SAQUES

        if exedeu_saldo:
            print("ERRO! SALDO INSUFICIENTE!")

        elif exedeu_limite:
            print("ERRO! VALOR EXEDEU O LIMITE DE SAQUE DE R$500 POR SAQUE")

        elif exedeu_Saque:
            print("ERRO! VOCÊ EXEDEU O LIMITE DIÁRIO DE SAQUES!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
    
        else:
            print("ERRO! VALOR É INVALIDO!")

    elif opcao == "e":
        print("\n============EXTRATO============")
        print("Não foram relizadas movimentações:" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "q":
        break
    
    else:
        print("ERRO! POR FAVOR SELECIONE UMA DAS OPÇÕES")