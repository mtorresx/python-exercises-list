#Este código pede o salário atual para o usuário
#Depois define o percentual de reajuste conforme a faixa salarial
#E mostra o percentual, o valor do aumento e o novo salário

salario = float(input("Salário atual: R$ "))

if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f"Percentual aplicado: {percentual}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
