def factorial(num):
    fact=1
    num=num+1
    for i in range(1,num):
        fact=fact*i
    print(fact)
numero= int(input("Numero: "))
while numero<0:
    print("Ingrese un numero positivo o cero: ")
    numero= int(input("Numero: "))
factorial(numero)
