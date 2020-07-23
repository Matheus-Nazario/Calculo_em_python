num = int(input("Digite um número inteiro?"))
print("\n")
print("--"*20)

print('''Escolha uma das bases pra conversão:
[1] Converter para BINÁRIO
[2] Converter para Octal
[3] Converter para Hexagonal''')

print("--"*20)

print("\n")
opcao = int(input("Qual é a sua opção? R: "))

if opcao == 1:
    binario = bin(num)
print("O Número {} convertido para binario é {}.".format(num, binario))

else:
    Octal = oct(num)
print("O Número {} convertido para Octal é {}.".format(num, Octal))
'''
elif opcao == 3 :
    Hexagonal = hex(num)
print("O Número {} convertido para Hexagonal é {}.".format(num, Hexagonal))'''