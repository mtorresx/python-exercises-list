#Este código pede o número de um mês e um ano para o usuário
#Depois verifica quantos dias o mês possui (considerando ano bissexto)
#E mostra a quantidade de dias, ou mês inválido

mes = int(input("Mês: "))
ano = int(input("Ano: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("31 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dias")
elif mes == 2:
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        print("29 dias")
    else:
        print("28 dias")
else:
    print("MÊS INVÁLIDO")
