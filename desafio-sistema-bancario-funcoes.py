# Modularizar o código
# Adicionar duas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).
# Saque: argumentos apenas por nome (keywork only); saldo, valor, extrato, limite, numero_saques, limite_saques; retorna saldo e extrato.
# Depósito: argumentos apenas por posição (positional only); saldo, valor, extrato; retorna saldo e extrato.
# Extrato: argumentos por posição (saldo) e argumentos nomeados (extrato).
# Novas funções: criar_usuario, criar_conta_corrente, listar_contas, etc.
# Lista de usuários: nome, data de nascimento, cpf (único, somente números), endereço (logradouro, número - bairro - cidade/estado).
# Lista de contas correntes: agência ("0001"), número da conta (sequencial, iniciando de 1) e usuário; usuário pode ter mais de uma conta, mas uma conta pertence a um único usuário.

import textwrap


def menu():
    menu = """\n
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")    
    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print(f"\n@@@ Operação falhou! Você não tem saldo suficiente. (SALDO_ATUAL = R$ {saldo:.2f}) @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. (VALOR_MÁXIMO_SAQUE = R$ 500.00) @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. (LIMITE_SAQUES = 3) @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("@@@ Operação falhou! O valor informado é inválido. @@@")
    return slado, extrato
    

def exibir_extrato(saldo, /, *, extrato):
    # Extrato
    print("\n================== EXTRATO ==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================================")
    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@"
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Infomre a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    
    print("\n=== Usuário criado com sucesso! ===")
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    print("\b@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}           
        """
        print("=" *100)
        print(textwrap.dedent(linha))
    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()        
        if opcao == "d":
            # Depósito
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            # Saque
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
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
        elif opcao == "lc":
            listar_contas(contas) 
        elif opcao == "q":
            # Sair
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    

main()




