#Este código pede um valor em metros para o usuário
#Depois converte esse valor para centímetros e milímetros
#E mostra os resultados das conversões na tela

metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros} metros correspondem a {centimetros} centímetros")
print(f"{metros} metros correspondem a {milimetros} milímetros")