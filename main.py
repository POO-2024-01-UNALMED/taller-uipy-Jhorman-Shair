from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x260")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=100, padx=1, pady=1)

def comprobar_numeros(lista):
    try:
        for x in lista:
            p=float(x)
    except ValueError:
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), "Error")
            return False
    return True
        
def igual():
    operacion=pantalla.get()
    if len(operacion.split("+"))==2:
        lista=operacion.split("+")
        prueba=comprobar_numeros(lista)
        if prueba:
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), float(lista[0])+float(lista[1]))
    elif len(operacion.split("/"))==2:
        lista=operacion.split("/")
        prueba=comprobar_numeros(lista)
        if prueba:
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), float(lista[0])/float(lista[1]))
    elif len(operacion.split("-"))==2:
        lista=operacion.split("-")
        prueba=comprobar_numeros(lista)
        if prueba:
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), float(lista[0])-float(lista[1]))
    elif len(operacion.split("*"))==2:
        lista=operacion.split("*")
        prueba=comprobar_numeros(lista)
        if prueba:
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), float(lista[0])*float(lista[1]))
    else:
        pantalla.delete(0,pantalla.get().__len__()+1)
        pantalla.insert(pantalla.get().__len__(), "Error")
    pantalla.insert(pantalla.get().__len__(), "´")

def numero1():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(),"1")

def numero2():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(),"2")

def numero3():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "3")

def numero4():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "4")

def numero5():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "5")

def numero6():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "6")

def numero7():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "7")

def numero8():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "8")

def numero9():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "9")
    
def insertar_division():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "/")

def insertar_suma():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "+")

def insertar_resta():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "-")

def insertar_multiplicacion():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "*")

def insertar_punto():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]=="´":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), ".")
    

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=numero1).grid(row=1, column=0, padx=0, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=numero2).grid(row=1, column=1, padx=0, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero3).grid(row=1, column=2, padx=0, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero4).grid(row=2, column=0, padx=0, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero5).grid(row=2, column=1, padx=0, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero6).grid(row=2, column=2, padx=0, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero7).grid(row=3, column=0, padx=0, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero8).grid(row=3, column=1, padx=0, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero9).grid(row=3, column=2, padx=0, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=igual).grid(row=4, column=0, columnspan=2, padx=0, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=insertar_punto).grid(row=4, column=2, padx=0, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=insertar_suma).grid(row=1, column=3, padx=0, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=insertar_resta).grid(row=2, column=3, padx=0, pady=1)
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=insertar_multiplicacion).grid(row=3, column=3, padx=0, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=insertar_division).grid(row=4, column=3, padx=0, pady=1)

root.mainloop()