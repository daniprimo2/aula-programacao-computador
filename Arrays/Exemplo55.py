# Exemplo 55 - lista de nomes
nomes = []

for i in range(5):
    n = input("Digite o nome: ")
    nomes.append(n)

print(nomes)
print(len(nomes))

nome = input("Digite um nome para remover da lista: ")
if nome in nomes:
    nomes.remove(nome)
    print(nomes)
    print(len(nomes))
else:
    print("Nome não localizado !")
