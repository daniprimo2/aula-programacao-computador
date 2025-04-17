

num = int(input("Digite um número inteiro: "))

for i in range(11):
    print("%d * %d = %d"%(num, i, num*i))

print("///////////////////")
    
for i in range(1,11,1):
    for j in range(11):
        print("%d * %d = %d"%(i, j, i*j))


soma = 0

for i in range(1, 11, 1):
    numero = int(input("Digite o %d° numero inteiro: "%(i)))
    soma = soma + numero


print("Valores somados foram %d"%(soma))