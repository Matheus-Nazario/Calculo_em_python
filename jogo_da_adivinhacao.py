#importamos primeiro o numero aleatorio pra a máquina escolher um número
from random import randint

print("-="*20) #mutplicamos 20x a string -=
print("Vou pensar em número de 0 a 10, tente advinhar....")
print("-="*20)
computador = randint(0, 10) #depois que importamos escrevos para pra máquina escolher de 0 a 10

num_usuario = int(input("Qual é o número que pensei?")) #usuario escreve

if (computador == num_usuario):
    print("Parábens, vc conseguiu acerta!")
else:
    print("Errou, o número assetivo é {}".format(computador))
    