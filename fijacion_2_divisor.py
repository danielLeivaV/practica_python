def div(num):
    max=int(1+num/2)
    divisor=[]
    
    for i in range(1,max):
        if num%i==0:
            divisor.append(i)
    divisor.append(num)
    print(divisor)

numero= int(input("Numero: "))
while numero<=0:
    print("Ingrese un numero mayor a cero: ")
    numero= int(input("Numero: "))
div(numero)
