menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
valor_limite_saque = 500
valor_minimo_deposito = 100;
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_operacao = 0


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quantos reais você deseja depositar? "))
        limite_deposito = valor >= valor_minimo_deposito

        if limite_deposito:
            saldo += valor
            numero_operacao += 1
            mensagem = f"#{numero_operacao} Depósito: R$ {valor:.2f} \tSaldo R$ {saldo:.2f}\n"
            extrato += mensagem
            print(mensagem)
        else:
            print("Operação falhou! O valor informado é inferior ao  mínimo permitido (R$ 100,00)")

    elif opcao == "s":
        valor = float(input("Você quer sacar quantos reais: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > valor_limite_saque 

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            numero_operacao += 1
            mensagem = f"#{numero_operacao} Saque: R$ {valor:.2f}\tSaldo R$ {saldo:.2f}\n"
            extrato += mensagem
            numero_saques += 1
            print(mensagem)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
