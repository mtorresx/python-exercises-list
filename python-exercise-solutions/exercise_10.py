#Este código pede o salário fixo e o total de vendas para o usuário
#Depois calcula a comissão de 40% sobre o valor vendido
#E mostra o valor da comissão e o salário final na tela

salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = float(input("Digite o total vendido: R$ "))

comissao = total_vendas * 0.40
salario_final = salario_fixo + comissao

print(f"Valor da comissão: R$ {comissao:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")