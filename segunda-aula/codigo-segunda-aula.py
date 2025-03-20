
def exercicioQuatroCalculadora():
     a = int(input("Digite o 1º numero? "))
     b = int(input("Digite o 2º numero? "))
     print("A soma dos numeros é", (a+b))
     print("A Subtracao dos numeros é", (a-b))
     print("A Multiplicacao dos numeros é", (a*b))
     print("A Divisao dos numeros é", (a/b))
     print("A resto dos numeros é", (a%b))

def calculadorMedia():
     a = float(input("Digite o 1º Numero: "))
     b = float(input("Digite o 2º Numero: "))
     print("A média dos números %.2f"%  ((a + b)/2))

def conversao():
    t1 = input("Digite primeiro numero: ")
    t2 = input("Digite segundo numero: ")
    n1 = int(t1)
    n2 = int(t2)
    print(n1+n2)

def informacao():
        varNome = input("Nome: ")
        varIdade = int(input("Idade: "))

        print("--------------------------------------------------------")

        print("Nome do aluno: %s"% varNome)
        print("Idade do aluno: ", varIdade)


        print("--------------------------------------------------------")

def selecao(valor):
     if valor == 1:
        return exercicioQuatroCalculadora()
     elif valor == 2:
        return conversao()
     elif valor == 3:
          calculadorMedia()
          

def calculoInversao():
     num = int(input("Digite um numero com três digitos: "))
     d1 = num // 100
     d2 = num % 100 // 10
     d3 = num % 10
     inverso = d3 * 100 + d2 * 10 + d1
     print("O inverso do número digitando é ", inverso)

def calculoQuatroInversao():
     num = int(input("Digite um numero com quatro digitos: "))
     d1 = num // 100
     d2 = num % 100 // 10
     d3 = num % 10
     inverso = d3 * 100 + d2 * 10 + d1
     print("O inverso do número digitando é ", inverso)


def infoSelecao():
     print("[1] - Exe3rci")
     print("[1] - ")

if __name__ == "__main__":
    calculoInversao()





