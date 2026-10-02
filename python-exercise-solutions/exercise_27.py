#Este código pede o peso e a altura para o usuário
#Depois calcula o IMC e verifica em qual faixa ele se encaixa
#E mostra o IMC e a classificação na tela

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"IMC: {imc:.1f}")
print("Classificação:", classificacao)
