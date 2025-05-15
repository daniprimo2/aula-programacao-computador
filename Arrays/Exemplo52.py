# Exemplo 52 - cálculo da média de n notas
notas = []
soma = 0
n = int(input("Digite a quantidade de notas: "))
for i in range(n):
    nota = float(input("Digite a %dª nota: " %(i+1)))
    notas.append(nota)
    soma += nota
if soma == 0:
    print("A soma das notas é igual a zero") 
else:
    media = soma / n
    print("A média dos números digitados é %.2f" %(media))
    print("As notas inseridas no programa são: ", notas)
