print("Ordem de precedência")
n1= float( input ("Didigite um valor: \n" ))
n2= float( input ("Digite um outro valor: \n"))

m = n1 * n2 # mutipicação 
e = n1**n2 #exponenciação
d = n1 / n2 #divisão 
di = n1 // n2 #divisião inteira 
r = n1 % n2 #resto 
s = n1 + n2 #soma
ss = n1 - n2 #subtração 

print (" A multplicação é {}; \n Exponenciação é {}; \n Divisão é {:.3f}" .format(m, e , d ), end=" ")
print("Divisão inteira é {}; \n resto é {}; \n Soma é {}; \n Subtração é {}.". format( di, r, s, ss ))

