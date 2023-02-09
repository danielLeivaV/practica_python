base = int(input('Introduce la base imponible de la factura: '))
iva=10/100
def aplica_iva(base, iva):
     base = base * iva
     return base 
print("iva= ",aplica_iva(base,iva))