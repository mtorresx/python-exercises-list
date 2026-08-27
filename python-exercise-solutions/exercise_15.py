#Este código pede o preço de um produto, a quantidade e o valor do frete
#Depois calcula o subtotal da compra
#E soma o frete para mostrar o valor total da compra

preco = float(input("Digite o preço unitário: R$ "))
quantidade = int(input("Digite a quantidade: "))
frete = float(input("Digite o valor do frete: R$ "))

subtotal = preco * quantidade
valor_total = subtotal + frete

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Valor total com frete: R$ {valor_total:.2f}")