print("Desafio de calcular uma área de uma sala, e a quantidade de tinta necssária para pintá-la")
largura= float(input("Qual é a largura da parede da sala? \n"))
altura= float(input("Qual é a altura da parede? \n"))

area = largura* altura
#sabendo que a cada 1 litro de tinta, pinta uma área de 2m².
qn = area / 2 #quantidade mecessário por cada metro quadrado. 

print("A área da sala é {} m², para pinta-la é necessário uma quantidade de {} litros.". format(area, qn) )
