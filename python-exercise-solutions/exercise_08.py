#Este código pede o preço de um produto para o usuário
#Depois calcula um desconto de 10% sobre esse valor
#E mostra o preço original, o desconto e o preço final na tela

preco = float(input("Digite o valor do produto: R$ "))

desconto = preco * 0.10
valor_final = preco - desconto

print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto de 10%: R$ {desconto:.2f}")
print(f"Preço final: R$ {valor_final:.2f}")