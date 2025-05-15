# Exemplo 54 - cálculo média de n alunos
medias = []
nomes = []

x = int(input("Digite a quantidade de alunos: "))
for i in range(x):
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    media = (n1 + n2) / 2
    medias.append(media)
    nomes.append(nome)

n = int(input("Digite o número do aluno que deseja exibir: "))
if medias[n] >= 6.0:
    print("O(a) aluno(a) %s foi aprovado(a) com a média %.2f" %(nomes[n], medias[n]))
else:
    print("O(a) aluno(a) %s foi reprovado(a) com a média %.2f" %(nomes[n], medias[n]))
