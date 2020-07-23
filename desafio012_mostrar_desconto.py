print("calcluar o desconta da loja")
valor = float(input("Qual é o valor do produto da loja que você desja saber o desconto? \n R$"))
#sabendo que a loja está sando 5% de desconto

desconto = valor - (valor* 5/100)

print("O valor do produto é R${}, com desconto fica R${:.2f}.".format(valor, desconto))