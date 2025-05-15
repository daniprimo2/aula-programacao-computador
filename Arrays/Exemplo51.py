# Exemplo 51 - cálculo da média de quantidade indeterminada de números
num = []
soma = 0
while True:
    valor = float(input("Digite um número: "))
    if valor < 0:
        print("Número inválido")
        continue
    elif valor == 0:
        break
    num.append(valor)
    soma += valor
if len(num) == 0:
    print("Nenhum número válido foi inserido") 
else:
    media = soma / len(num)
    print("A média dos números digitados é %.2f" %(media))
    print("Os números inseridos no programa são: ", num)
