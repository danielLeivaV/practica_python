
n=int(input("cantidad de asignaturas: "))

asignaturas=[]
for i in range(n):
    print("introduce el nombre de la materia: ",i+1)
    asignaturas.append((input()))

for i in range(len(asignaturas)):
    print("Asignatura: ",asignaturas[i])

print("introduce el nombre de la materia a eliminar: ")
remover=input()
asignaturas.remove(remover)

print("\nListas de materias: ")

for i in range(len(asignaturas)):
    print("Asignatura: ",asignaturas[i])