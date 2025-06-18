# Cálculo Salarial com Python
import sys

if __name__ == "__main__":
    # Verifica se o argumento foi fornecido
    if len(sys.argv) < 2:
        print("Uso: python calculo_salarial.py nome_arquivo_teste.txt")
        sys.exit(1)

    # Pega o nome do arquivo passado como argumento
    teste = sys.argv[1]

    with open(teste, "r", encoding="utf-8") as f:
        valor_salario = float(f.readline())
        valor_beneficios = float(f.readline())

    #valor_salario = float(input("Entre com o valor do salario: "))
    #valor_beneficios = float(input("Entre com o valor dos benefícios: "))
    if valor_salario >= 0 and valor_salario <= 1100:
        valor_imposto = 0.05 * valor_salario
    elif valor_salario >=1100.01 and valor_salario <= 2500.00:
        valor_imposto = 0.10 * valor_salario
    elif valor_salario > 2500.00:
        valor_imposto = 0.15 * valor_salario
    saida = valor_salario - valor_imposto + valor_beneficios
        
    print(f"Salário bruto: R$ {valor_salario:.2f}. Impostos: R$ {valor_imposto:.2f}. Benefícios: R$ {valor_beneficios:.2f}. Líquido: R$ {saida:.2f}")