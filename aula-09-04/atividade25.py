    
#Exemplo 24 - Calculo do imc 
import math

print("-----------------------------------")
print("       Calculo parcelas juros      ")
print("-----------------------------------\n")

valor = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite o numero de parcelas numero inteiros: "))



if parcelas == 2:
    valor = valor * 1.03
    print("\nO valor d ecada parcela é R$ %.2F"%(valor/parcelas))
elif parcelas == 4:
    valor = valor * 1.07
    print("\nO valor d ecada parcela é R$ %.2F"%(valor/parcelas))
elif parcelas == 6:
    valor = valor * 1.09
    print("\nO valor d ecada parcela é R$ %.2F"%(valor/parcelas))
elif parcelas == 8:
    valor = valor * 1.12
    print("\nO valor d ecada parcela é R$ %.2F"%(valor/parcelas))
else:
    print("\nO número de parcelas é invalido")

