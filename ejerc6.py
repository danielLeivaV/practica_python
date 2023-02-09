n=1
while True:
    n= int(input("introduzca un numero: "))
    if n<0 :
        print("el numero es negativo")
        break
    print("el cuadrado de ", n, " es " ,n**2)