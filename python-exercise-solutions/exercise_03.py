#Este código pede um número inteiro para o usuário
#Depois calcula o número que vem antes e o que vem depois
#E mostra o antecessor, o número digitado e o sucessor na tela

valor = int(input("Digite um número inteiro: "))

anterior = valor - 1
proximo = valor + 1

print("Número anterior:", anterior)
print("Número digitado:", valor)
print("Próximo número:", proximo)