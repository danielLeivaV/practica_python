def primo(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

numero= int(input("Numero: "))
if primo(numero):
    print("es Primo")
else:
    print("no es primo")