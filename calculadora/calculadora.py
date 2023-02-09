from tkinter import *

vtn =Tk()
vtn.title("Calculadora")
vtn.geometry('250x200')
vtn.configure(background='black')
def suma():
    suma=int(txt1.get()) +int(txt2.get())
    return resultado.set(suma)

def resta():
    resta=int(txt1.get()) -int(txt2.get())
    return resultado.set(resta)
def multiplicacion():
    multiplicacion=int(txt1.get()) *int(txt2.get())
    return resultado.set(multiplicacion)
def division():
    division=int(txt1.get()) /int(txt2.get())
    return resultado.set(division)
    
def cerrar():
    vtn.destroy()

resultado=StringVar()

lbl1= Label(vtn,text='Primer Numero', bg='black', fg='white')
lbl1.grid(row=1,column=1)
txt1=Entry(vtn)
txt1.grid(row=1,column=2)

lbl2= Label(vtn,text='Segundo Numero', bg='black', fg='white')
lbl2.grid(row=2,column=1)
txt2=Entry(vtn)
txt2.grid(row=2,column=2)
lbl3= Label(bg='black')
lbl3.grid(row=3,column=1)

btnsuma=Button(vtn,text='+',bg='grey',fg='black', width=11, command=suma)
btnsuma.grid(row=4,column=1)

btnresta=Button(vtn,text='-',bg='grey',fg='black', width=11, command=resta)
btnresta.grid(row=4,column=2)

btnmultiplicacion=Button(vtn,text='*',bg='grey',fg='black', width=11, command=multiplicacion)
btnmultiplicacion.grid(row=5,column=1)

btndivision=Button(vtn,text='/',bg='grey',fg='black', width=11, command=division)
btndivision.grid(row=5,column=2)

lbl4= Label(bg='black')
lbl4.grid(row=6,column=1)

lblres= Label(vtn,bg='white', fg='black', width=30, textvariable=resultado)
lblres.grid(row=7,column=1, columnspan=2)

lbl5= Label(bg='black')
lbl5.grid(row=8,column=1)

btncerrar=Button(vtn,text='cerrar',bg='red',fg='black', width=30, command=cerrar)
btncerrar.grid(row=9,column=1, columnspan=2)

vtn.mainloop()