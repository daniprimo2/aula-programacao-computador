    
#Exemplo 24 - Calculo do imc 
import math

print("--------------------------------")
print("       Calculo do IMC           ")
print("--------------------------------\n")

peso = float(input("Digite o peso em KG: "))
altura = float(input("Digite a altura em M: "))
imc = peso / math.pow(altura, 2)
print("\nO Valor do IMC é %.2f"%(imc))

if imc < 20:
    print("\nAbaixo do peso.")
elif imc >= 20 and imc < 25:
    print("\nPeso normal.")
elif imc >= 25 and imc < 30:
    print("\nSobrepeso.")
elif imc >= 30 and imc < 40:
    print("\nObeso.")
elif imc >= 40:
    print("\nObeso pra caralhooo.")
