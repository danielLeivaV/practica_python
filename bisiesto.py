def bisiesto(num):
    False
    if num%4==0 and num%400==0 and num%100==0:
         return True
    elif num%4==0 and num%100!=0:
        return True


numero= int(input("Numero: "))
if bisiesto(numero):
    print("es bisiesto")
else:
    print("no es bisiesto")