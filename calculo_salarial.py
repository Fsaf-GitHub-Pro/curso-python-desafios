# Cálculo Salarial com Python

valor_salario = float(input("Entre com o valor do salario: "))
valor_beneficios = float(input("Entre com o valor dos benefícios: "))
if valor_sario >= 0 and valor_salario <= 1100:
    valor_imposto = 0.05 * valor_salario
elif valor_salario >=1100.01 and valor_salario <= 2500.00:
    valor_imposto = 0.10 * valor_salario
elif valor_salario > 2500.00:
    valor_imposto = 0.15 * valor_salario
saida = valor_salario - valor_imposto + valor_beneficios
print(f"{saida:.2f}")