print("Atividade exemplo 20: ")
print("----------------------")

media - float(input("Digite a média do aluno: "))
frequencia - float(input("Digite o percentual de frequêcia do aluno: "))

if frequencia < 75:
    print("\nAluno reprovado por falta.")
else: 
    if media < 6:
        print("\nAluno reprovado por nota.")
    else:
        print("\nAluno aprovado.")