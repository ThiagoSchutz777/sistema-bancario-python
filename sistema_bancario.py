def menu(): 
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
            
    else:
        print("ERRO! VALOR INVÁLIDO!")

    return saldo, extrato       

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
            
        excedeu_limite = valor > limite

        excedeu_Saque = numero_saques >= limite_saques

        if excedeu_saldo:
                print("ERRO! SALDO INSUFICIENTE!")

        elif excedeu_limite:
                print("ERRO! VALOR EXEDEU O LIMITE DE SAQUE DE R$500 POR SAQUE")

        elif excedeu_Saque:
                print("ERRO! VOCÊ EXEDEU O LIMITE DIÁRIO DE SAQUES!")

        elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
        else:
                print("ERRO! VALOR É INVALIDO!")

        return saldo, extrato        

def exibir_extrato(saldo, /, *, extrato):
    print("\n============EXTRATO============")
    print("Não foram relizadas movimentações:" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("================================") 

def criar_usuario(usuarios):
        cpf = input("DIGITE O SEU CPF(SOMENTE OS NUMEROS): ")
        usuario = filtrar_usuario(cpf, usuarios)
        
        if usuario:
            print("\nESTE USUÁRIO JÁ EXISTE")
            return
        
        nome = input("DIGITE SEU NOME COMPLETO: ")
        data_nascimento = input("DIGITE SUA DATA DE NASCIMENTO (NESTE FORMATO DD-MM-AAAA): ")
        endereco = input("DIGITE O SEU ENDEREÇO(logradouro, nro - bairro - cidade/sigla do estado): ")

        usuarios.append({"nome" : nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
        
        print("USUÁRIO CRIADO!")
     
def filtrar_usuario(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
        cpf = input("INFORME O SEU CPF: ")
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
              print("\nCONTA CRIADA COM SUCESSO")
              return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        print("USUÁRIO NÃO ENCONTRADO, FALHA AO CRIAR CONTA!") 

def main():    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato) 

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$"))

            saldo, extrato = sacar(
                 saldo = saldo,
                 valor = valor,
                 extrato = extrato,
                 limite = limite,
                 numero_saques = numero_saques,
                 limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
             criar_usuario(usuarios) 

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)       

        elif opcao == "q":
            break
        
        else:
            print("ERRO! POR FAVOR SELECIONE UMA DAS OPÇÕES")

main()              