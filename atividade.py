#NOME DOS PARTICIPANTES
print("NOME DOS PARTICIPANTES:\nGilberto Ungaro Chiancone\nLucas Rafael Alves\nGuilherme Marques Dias\nHeberson Vinícius Oliveira Silva\nDaniel Lopes Sousa Moreira")

# Análise e Desenvolvimento de Sistemas QUESTÃO 1
print("\nAnálise e Desenvolvimento de Sistemas - Unicsul\n")

# Hobby QUESTÃO 2
hobby = str(input("Qual é seu hobby que geralmente faz no dia a dia? \n"))
print("Que legal, eu tambem gosto de {}\n".format(hobby))

# Aniversário QUESTÃO 3 E 6
dia = int(input("Qual é o DIA do seu aniversario? \n"))
mes = int(input("Agora qual é o MÊS? \n"))
from datetime import datetime
ano_atual = (datetime.today().year)
ano = int(input("Por fim, qual ano? \n"))
idade = ano_atual - ano
print("Ou seja voce é do dia {} de {} de {}, com {} anos, ou irá fazer esse ano! \n".format(dia,mes,ano,idade))

# Familia QUESTÃO 4
f1 = str(input("Digite o seu ultimo nome: \n"))
print("Ou seja você é da Familia {}\n".format(f1))

# Esporte  QUESTÃO 5
esp = str(input("Qual é o seu esporte favorito?\n"))
if esp == "" or esp.lower() == "nenhum" or esp.lower() == "nada":
    print("Que pena, fazer esportes faz bem para a saúde!! \n")
else:
    print(f"Que legal! {esp} é um otimo esporte!\n")

# Salário QUESTÃO 7
sal =  float(input("Digite um valor para um salário de um funcionário seu: R$ "))
print("Vamos supor que o seu funcionário ja esta a mais de 2 anos sem um aumento, que tal dar um aumento para ele?")
valor = float(input("Digite apenas o valor: % "))
porc = (valor / 100)*sal
sal_atual = porc + sal
print("Pronto, agora o seu funcionario recebe exatos R${}, graças a você!\n".format (sal_atual))

# Trigonometria QUESTÃO 8
import math
csombra = float(input("Digite o comprimento da sombra em metros: "))
angulo = float(input("Digite um angulo em graus: "))
altura = math.tan(math.radians(angulo))*csombra
print("A altura do prédio é: {:2f}\n".format(altura))

# Pagamento à vista QUESTÃO 9
print(str("Você acabou de entrar em uma loja e la esta escrito 10% de desconto para pagamentos à vista\n"))
vlr = float(input("Digite um valor que voce provavelmente gastaria em roupas: R$ "))
porce = (10 / 100)
desc = porce * vlr
vlr_final = vlr - desc
print("Foram descontado {}%, foi o desconto já que voce optou por pagar a vista, e o valor total seria {}, porém ira ficar {}\n".format(porce,vlr,vlr_final))

# Solicita ao usuário a distância entre as cidades (em km) QUESTÃO 10
dist = float(input("Digite a distacia em km: "))
temp = float(input("Digite quanto tempo durou a viagem em horas: "))
vel = dist/temp
print("A velocidade média da viagem foi de {}\n".format(vel))

# EQUAÇÃO 2 GRAU QUESTÃO 11
import math 
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b**2 - 4*a*c
if delta >= 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes da equação são: x1 = {raiz1:.2f}, x2 = {raiz2:.2f}")

else:
    print("As raízes não são reais.\n")

# Cotação de Dólar para Real Brasileiro QUESTÃO 12
dolar = 5.71
real = float(input("Digite um valor em Real, para que eu transforme ele em Dólar, levando em consoideração o Dólar com o valor de US$5.71: "))
vlr = real / dolar
print("O valor solicitado seria de exatos US${}\n".format(vlr))

# Taxa do garçom QUESTÃO 13
print(str("Na maioria das vezes em que você come em algum restaurante com garçons a sua volta te servindo, geralmente tem a famosa 'Taxa do garçom' que geralmente são 10% sob o valor total do pedido."))
ped = float(input("Agora digite um valor simulativo em que voce geralmente gasta em algum restaurante, e vamos incluir os 10% do garçom para vermos quanto ficaria R$ \n"))
tax = (10/100)*ped
pedf = tax + ped
print("O valor total do seu pedido, já com a taxa do garçom seria de {}\n".format(pedf))

# Conversão de temperatura QUESTÃO 14
tc = float(input("Digite um valor em Celsius, que tranformarei em Kelvin e Fahrenheit:\n"))
tf = (1.8*tc)+32
tk = tc + 273
print(str("Dessa forma, a temperatura em Celsius {}, ficará {} para °F e {} para K").format(tc,tf,tk))