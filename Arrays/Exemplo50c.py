# Exemplo 50c - atribuição e visualização de valores com método insert com listas e estrutura de repetição
nomes = []
print("O tamanho inicial da lista 'nomes' é %d" %(len(nomes)))
print("\n")
for i in range(5):
    ref = str(input("Digite um nome: "))
    nomes.insert(int(i), ref)
print("\n")
print(nomes)
print("\n")
for i in range(5):
    print(nomes[i])
