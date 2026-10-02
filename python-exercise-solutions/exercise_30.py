#Este código pede o valor do imóvel, o salário e o prazo em anos
#Depois calcula a prestação mensal e o limite de 30% do salário
#E mostra se o empréstimo foi aprovado ou negado

valor_imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Prazo (anos): "))

meses = anos * 12
prestacao = valor_imovel / meses
limite = salario * 0.30

print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")

if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")
