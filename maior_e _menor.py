a = int(input("Qual é o primeiro número:"))
b = int( input("Qual é o segundo númer:"))
c = int( input("Qual é o terceiro número:"))

#maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b: 
    maior = c
#menor 

    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b: 
    menor = c
print("O Número maior é {}" .format(maior))
print("O Número menor é {}". format(menor))