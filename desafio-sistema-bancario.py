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
        # Depósito
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito : R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        # Saque
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente (SALDO_ATUAL = R$ {saldo:.2f}).")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite (VALOR_MÁXIMO_SAQUE = R$ 500.00).")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido (LIMITE_SAQUES = 3).")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e":
        # Extrato
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")
    elif opcao == "q":
        # Sair
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")