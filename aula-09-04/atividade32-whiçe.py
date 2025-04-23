
print("")

contador = 1
while contador <= 10:
    print("\nAluno %d" %(contador))
    nota01 = input("\nDigite a primeira nota: ")
    nota02 = input("\nDigite a segunda nota: ")
    nota = (nota01 + nota02) / 2
    print("Nota é: ", nota)
    contador = contador + 1