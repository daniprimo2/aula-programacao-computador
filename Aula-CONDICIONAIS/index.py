


print("Atividade 1 em sala ")
print("")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Maior de idade !")
else:    
    print("Menor de idade !")
    
    
    
print("Atividade 2 em sala ")
print("")

num = int(input("Digite um numero inteiro: "))

if (num%2==0):
    print("\no numero %d é para"% (num))
    print("\no numero %d é para"% (num))
    
print("Atividade 3 em sala ")
print("")

a = int(input("Digite a infoirmação A: "))
b = int(input("Digite a infoirmação B: "))
c = int(input("Digite a infoirmação C: "))


if a > b and b < c:
    print("")
    print("B é a menor informação B")
elif b > a and a < c:
    print("")
    print("A é a menor informação A")
else :
    print("")
    print("C é a menor informação C")
    
    
    
print("Atividade 4 em sala ")
print("")

num = int(input("Digite um numero inteiro: "))

if (num%2==0):
    print("\no Números %d é par"% (num))
else:
    print("\no Números %d é impar"% (num))
    
    
print("Atividade 5 em sala ")
print("")

num1 = float(input("Digite a nota 1: "))
num2 = float(input("Digite a nota 2: "))

media = (num1 + num2) / 2

print("A medida é %2.f"% (media))

if (media >= 6.0):
    print("\no Aluno foi aprovado")
else:
    print("\no Aluno foi reprovado")