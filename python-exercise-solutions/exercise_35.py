#Este código pede a idade e se a pessoa é estudante para o usuário
#Depois verifica se ela tem direito à meia-entrada (desconto não acumulativo)
#E mostra o valor do ingresso na tela

preco_ingresso = 30.00

idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

if idade < 12 or estudante == "SIM" or idade >= 60:
    valor = preco_ingresso * 0.5
else:
    valor = preco_ingresso

print(f"Valor do ingresso: R$ {valor:.2f}")
