ano = int(input('Qual é o ano?'))

bissexto = ano % 4

if (bissexto == 0): 
    print("O Ano é bissexto")
else:
    print("O Ano não é bi2ssexto")