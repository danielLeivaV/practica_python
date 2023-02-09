my_list=[]
for i in range(20):
    my_list.append(int(input("introduce el numero :")))

print("\nLista de numeros: ",my_list)
pos=0
mayor=0
for i in my_list:
   pos=pos+1
   if i>mayor:
    mayor=i
    posMayor=pos
print("El numero mayor de la lista es:",mayor)
print("La posicion es: ",posMayor)