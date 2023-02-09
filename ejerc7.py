n=1
d=0
u=0
while n<6:
    n+=1
    a= int(input("introduzca una nota: "))
    if a>1:
        d=d+1
    else:
        u=u+1
print("no aprobados ", u)
print("aprobados ", d)