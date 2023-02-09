def suma(num1,num2):
    sum=num1+num2
    print("la suma es: ",sum)
def resta(num1,num2):
    resta=num1-num2
    print("la resta es: ", resta)
def multiplicacion(num1,num2):
    mult=num1*num2
    print("el producto es: ", mult)
def division(num1,num2):
    division=num1/num2
    print("el cociente es: ", division)
print("*Para Sumar opcion 1 \n*Para restar opcion 2 \n*Para multiplicar opcion 3 \n*Para dividir opcion 4 \n*Para salir opcion 5\n")

operacion= int(input("Indique opcion: "))
while operacion<=4:
    
    num1= int(input("Ingrese primer numero: "))
    num2= int(input("Ingrese segundo numero: "))

    if operacion==1:
        suma(num1,num2)
    elif operacion==2:
         resta(num1,num2)
    elif operacion==3:
        multiplicacion(num1,num2)
    else:
        division(num1,num2)
    operacion= int(input("Indique opcion: "))
    if operacion==5:
        print("\n ha salido del programa")
        break
