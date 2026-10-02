#Este código pede a idade de uma pessoa para o usuário
#Depois verifica em qual faixa de idade ela se encaixa
#E mostra a categoria de votação na tela

idade = int(input("Digite a idade: "))

if idade < 16:
    categoria = "NÃO PODE VOTAR"
elif idade < 18:
    categoria = "VOTO OPCIONAL"
elif idade < 70:
    categoria = "VOTO OBRIGATÓRIO"
else:
    categoria = "VOTO OPCIONAL"

print("Resultado:", categoria)
