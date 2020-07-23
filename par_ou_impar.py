num = int(input("Qual é o número que vc deseja descobiri?"))

par = num % 2

if (par == 0):
    print("O Número {} é Par.".format(num))
else:
    print("O Número {} é Ímpar.".format(num))