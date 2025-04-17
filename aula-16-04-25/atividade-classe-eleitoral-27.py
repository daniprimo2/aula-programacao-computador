idade = int(input("Digite a sua idade: "))


if idade < 16 :
    print("\nVocÊ não é eleitor.")
elif  idade >= 16 and idade < 18 or idade > 65 :
    print("\nVocê não é eleitor facultativo.")
else:
    print("\nVocê é eleitor obrigatorio")

