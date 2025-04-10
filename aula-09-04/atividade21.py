#Tipo de diaria, quantidade de dias 

print("--------------------------------")
print("      Tipo de Diaria            ")
print("--------------------------------\n")

print("[S] - Diária Simples.")
print("[D] - Diária Duplox.")
print("[T] - Diária Triplo.\n")

opcao = input("Digite a opção desejada: ")

if opcao == 's' or opcao == 'S':
    diaria =  int(input("Quantidade de dias: "))
    print("\nTipo da diária é Simples.\n O Valor a ser pago é: %.2f"%(diaria * 255.5)) 
elif opcao == 'd' or opcao == 'D':
    diaria =  int(input("Quantidade de dias: "))
    print("\nTipo da diária é Duplo.\n O Valor a ser pago é: %.2f"%(diaria * 305.5)) 
elif opcao == 't' or opcao == 'T':    
    diaria =  int(input("Quantidade de dias: "))
    print("\nTipo da diária é Triplo.\n O Valor a ser pago é: %.2f"%(diaria * 360.5)) 
else : 
    print("\nOpção inválida") 


def buscarQuantidadeDias():
    return int(input("Quantidade de dias: "))


#Exemplo 22 - hospedagem com desconto Tipo de diaria, quantidade de dias 

print("--------------------------------")
print("      Tipo de Diaria            ")
print("--------------------------------\n")
print("                       c/desconto.")

print("[S] - Diária Simples.")
print("[D] - Diária Duplox.")
print("[T] - Diária Triplo.\n")

opcao = input("Digite a opção desejada: ")
desconto = float(input("Digite a porcentagem {%} de desconto"))

if opcao == 's' or opcao == 'S':
    diaria =  int(input("Quantidade de dias: "))
    print("\nTipo da diária é Simples.\n O Valor a ser pago é: %.2f"%(diaria * 255.5)) 
elif opcao == 'd' or opcao == 'D':
    diaria =  int(input("Quantidade de dias: "))
    print("\nTipo da diária é Duplo.\n O Valor a ser pago é: %.2f"%(diaria * 305.5)) 
elif opcao == 't' or opcao == 'T':    
    diaria =  int(input("Quantidade de dias: "))
    print("\nTipo da diária é Triplo.\n O Valor a ser pago é: %.2f"%(diaria * 360.5)) 
else : 
    print("\nOpção inválida") 



#Exemplo 23 - hospedagem com desconto Tipo de diaria, quantidade de dias 

print("----------------------------------------------")
print("       Digite três Numeros inteiros           ")
print("----------------------------------------------\n")

n1 = input("Digite o primeiro números: ")
n2 = input("Digite o segundo números: ")
n3 = input("Digite o terceiro números: ")

if n1 > n2 and n1 > n3:
    print("\nO Primeiro número é o maior")
elif n2 > n1 and n2 > n3:
    print("\nO Segundo número é o maior")
elif n3 > n1 and n3 > n2:
    print("\nO Terceiro número é o maior")

