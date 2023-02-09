from tkinter import *

vtn =Tk()
vtn.title("Calculo de Divisas")
vtn.geometry('250x200')
vtn.configure(background='black')
def dolar():
    dolar=int(txt1.get()) /7100
    return resultado.set(dolar)

def pesosArg ():
    pesosArg=int(txt1.get()) /25
    return resultado.set(pesosArg)
def realBrasil():
    realBrasil=int(txt1.get()) /1300
    return resultado.set(realBrasil)
def euro():
    euro=int(txt1.get()) /7500
    return resultado.set(euro)
    
def cerrar():
    vtn.destroy()

resultado=StringVar()

lbl1= Label(vtn,text='Moneda en Guarani', bg='black', fg='white')
lbl1.grid(row=1,column=1)
txt1=Entry(vtn)
txt1.grid(row=1,column=2)



btndolar=Button(vtn,text='Dollar',bg='green',fg='white', width=11, command=dolar)
btndolar.grid(row=3,column=1)

btnpeso=Button(vtn,text='Peso Argentino',bg='blue',fg='white', width=11, command=pesosArg)
btnpeso.grid(row=4,column=1)

btnReal=Button(vtn,text='Real Brasilero',bg='brown',fg='white', width=11, command=realBrasil)
btnReal.grid(row=5,column=1)

btneuro=Button(vtn,text='Euro',bg='light blue',fg='black', width=11, command=euro)
btneuro.grid(row=6,column=1)

btncerrar=Button(vtn,text='cerrar',bg='red',fg='black', width=10, command=cerrar)
btncerrar.grid(row=9,column=1, columnspan=2)

lblres= Label(vtn,bg='white', fg='black', width=30, textvariable=resultado)
lblres.grid(row=8,column=2)
lbl2= Label(vtn,text='cambio de moneda', bg='black', fg='white')
lbl2.grid(row=8,column=1)

vtn.mainloop()