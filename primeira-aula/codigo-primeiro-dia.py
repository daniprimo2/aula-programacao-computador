
def informacoesDoAluno(aluno):
    aluno["nome"] = input("Digite nome do aluno: ")
    aluno["cpf"] = input("Digite cpf do aluno: ")
    aluno["email"] = input("Digite email do aluno: ")
    return aluno


def coletarNotas(aluno):
    aluno["nota1"] = input("Digite a 1º nota? ")
    aluno["nota2"] = input("Digite a 2º nota? ")
    aluno["nota3"] = input("Digite a 3º nota? ")
    aluno["nota4"] = input("Digite a 4º nota? ")
    aluno["nota5"] = input("Digite a 5º nota? ")
    return aluno


def estrtuturaMenu():
    print("Digite informações do boletim")
    print("[1] - Digite informações do boletim")
    print("[2] - Carregar Alunos Salvos.")


def calculcarMedia(aluno):
    nota1 = input("Digite uma nota: ")
    nota2 = input("Digite uma nota: ")


def main():   
    aluno = {}
    nota1 = input("Digite uma nota: ")
    nota2 = input("Digite uma nota: ")

    media = (nota1+nota2)/2

    print(media)

if __name__ == "__main__":
    main()











    print("--------------------------------------------------------")
    print("Nome: ", aluno["nome"])
    print("CPF: ", aluno["cpf"])
    print("Email: ", aluno["email"])

    print("--------------------------------------------------------")
    print ("Nome: %s  CPF: %s, Email: %s " % (aluno["nome"], aluno["cpf"], aluno["email"]))

    print("--------------------------------------------------------")
    print (f"Nome: {aluno["nome"]}  CPF: {aluno["cpf"]}, Email: {aluno["email"]} ")

    print("--------------------------------------------------------")
    print("Media: %.2f"% media)
