contador = 1
soma = 0
resp = 'n'



def validacao(resp):
    if resp == 's':
        return False
    elif resp == 'S':
        return False
    else:
        return True
    


while (validacao(resp)):
    num = float(input("Digite o número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja encerrar (S/N)? ")

media = soma / contador
print("\nA média dos números digitados é %.2f" %(media))

