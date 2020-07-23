from math import sqrt
print("Desafio que mostre o dobro, triplo e a raiz quadra.")
v1= float(input("Digite o valor que vc deseja descobrir: \n " ))

d = v1 ** 2 #dobro
t = v1 ** 3 #triplo
r = sqrt(v1) #raiz quadrada

print( "O Dobro do valor {} é {}; \n o triplo é {}; \n  a raíz quadrada é {:.3f}". format(v1, d , t , r))