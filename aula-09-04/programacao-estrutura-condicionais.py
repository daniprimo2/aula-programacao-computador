from Condicionais import

print("Atividade exemplo 20: ")
print("----------------------")

media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite o percentual de frequêcia do aluno: "))

if frequencia < 75:
    print("\nAluno reprovado por falta.")
else: 
    if media < 6:
        print("\nAluno reprovado por nota.")
    else:
        print("\nAluno aprovado.")



if frequencia >= 75:
    if media < 6:
        print("\nAluno reprovado por nota.")
    else:
        print("\nAluno aprovado.")
else: 
    print("\nAluno reprovado por falta.")


print("Atividade exemplo 20B [if-elif-else]")
media = float(input("Digite a média do alunno: "))
frequencia = float(input("Digite o percentual de frequencia do aluno: "))

if frequencia < 75:
    print("\nAluno reprovado por falta")
elif media < 6:
    print("\nAluno reprovado por nota")
elif 
    print("\nAluno Aprovado\n")