def diurno(horas):
    jornal=5*horas
    return jornal
def nocturno(horas):
    jornal=8*horas
    return jornal
def diurno_domingo(horas):
    jornal=(5+2)*horas
    return jornal
def nocturno_domingo(horas):
    jornal=(8+3)*horas
    return jornal

print("si el dia trabajado es de lunes a sabado ingrese 1 ")
print("si el dia trabajado es domingo ingrese 2 ")
dia=int(input("ingrese codigo de dia: "))
while dia!=1 and dia!=2:
    print("Ingrese 1 si es de lunes a sabado o 2 si es domingo: ")
    dia= int(input(" "))

tipo= input("diurno o nocturno?: ")
tipo=tipo.lower()
while tipo!="diurno" and tipo!="nocturno":
    print("Ingrese correctamente diurno o nocturno : ")
    tipo= input("diurno o nocturno?: ")
    tipo=tipo.lower()

horas= int(input("Ingrese horas trabajadas: "))
while horas<=0:
    print("Ingrese un numero positivo: ")
    horas= int(input("Numero: "))
if dia==1 and tipo=="diurno":
    HT=diurno(horas)
    print(HT)

elif dia==2 and tipo=="diurno":
    HT=diurno_domingo(horas)
    print(HT)
elif dia==1 and tipo=="nocturno":
    HT=nocturno(horas)
    print(HT)
elif dia==2 and tipo=="nocturno":
    HT=nocturno_domingo(horas)
    print(HT)