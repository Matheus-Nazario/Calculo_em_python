casa = float(input("Qyal é o valor da casa? R$"))
salario = float(input("Qyal é o seu salario?R$"))
anos = int(input("Quantos anos vai pagar?"))

prestacao = casa / (anos * 12)

minimo = salario * 30/100

if prestacao <= minimo:
    print("Concedido")
else:
    print("Não concedido") 
