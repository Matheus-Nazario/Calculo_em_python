import math
num = float(input('Digite um número: '))

dobro = math.pow(num,2)
triplo = math.pow(num,3)
raiz= math.sqrt(num)

print('O Número que vc deseja é {:^5}.'.format(num))
print('\n')
print("O Dobro do número é: {}".format(dobro))
print('\n')
print("O Triplo do número é: {}".format(triplo))
print('\n')
print("A Raiz Quadrada do número é: {}".format(raiz))