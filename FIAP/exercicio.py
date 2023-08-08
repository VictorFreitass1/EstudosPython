# Pergunta o valor da hora e o número de horas trabalhadas no mês
valor_hora = float(input("Informe o valor ganho por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcula os descontos
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

# Calcula o salário líquido
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

# Exibe os resultados
print("+ Salário Bruto : R$ {:.2f}".format(salario_bruto))
print("- IR (11%) : R$ {:.2f}".format(imposto_renda))
print("- INSS (8%) : R$ {:.2f}".format(inss))
print("- Sindicato (5%) : R$ {:.2f}".format(sindicato))
print("= Salário Líquido : R$ {:.2f}".format(salario_liquido))
