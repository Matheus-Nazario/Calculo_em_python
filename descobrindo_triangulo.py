seg_a = float(input("Qual é o segmento do A?"))
seg_b = float(input("Qual é o segmento do B?"))
seg_c = float(input("Qual é o segmento do c?"))

if ((seg_a + seg_b)> seg_c or (seg_a + seg_c)> seg_b or (seg_b + seg_c)> seg_a ):
   print("Triangulo")
else:
   print("não Triangulo")