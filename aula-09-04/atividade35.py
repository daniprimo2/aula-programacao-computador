
from random import *


print("\nAtividade do jogo")


num = randint(0,10)
i = 0
controle = 0

while (controle == 0):
    i += 1
    x = int(input("Digite um número inteiro: "))
    if num == x:
        print("\nParabéns, você acertou o numero em %d tentativas \n\n" %(i))
        controle = 1
    elif num > x:
        print("\nO número gerado é maior que %d" %(x))
    elif num < x:
        print("\nO número gerado é menor que %d" %(x))


for d in range(10):
    if int(d) == 5:
        break
    print("O número do laço é %d" %(int(d)))


interator = 0
while (interator <= 5):
    d = range(1,10)
    interator = int(d)
    print("O número do laço é ", interator)

num = controle

convertidoInt = int(num)
convertidoFloat = float(num)
convertidoString = str(num)

print("Idade convertido ", convertidoInt)
print("Idade convertido ", convertidoFloat)
print("Idade convertido ", convertidoString, " dsad")
