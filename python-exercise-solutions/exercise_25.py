#Este código pede o preço de um produto e a forma de pagamento
#Depois aplica desconto ou acréscimo conforme a opção escolhida
#E mostra o valor final na tela

preco = float(input("Preço: R$ "))
print("1 - Dinheiro ou Pix (10% de desconto)")
print("2 - Débito (5% de desconto)")
print("3 - Crédito à vista (sem alteração)")
print("4 - Crédito parcelado (8% de acréscimo)")
opcao = int(input("Opção: "))

if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
else:
    valor_final = None

if valor_final is None:
    print("OPÇÃO INVÁLIDA")
else:
    print(f"Valor final: R$ {valor_final:.2f}")
