contador = 1
soma = 0
resp = 's'

while (resp == 's' or resp == 'S' ):
    num = float(input("Digite o número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja continuar (S/N)? ")

media = soma / contador
print("\nA média dos números digitados é %.2f" %(media))