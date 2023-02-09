i=0
m=0
M=0
c=0
while i<10:
    x=int(input("ingrese un numero "))
    if x < 0:
        m+=1
    elif x > 0:
        M+=1
    else:
        c+=1
    i+=1
print("-----------------"'\n')
print("numeros positivos ",M)
print("numeros negativos ", m)
print("ceros ", c)    
    