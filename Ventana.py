from tkinter import *


ventana = Tk()
ventana.title("Validador")

frame = Frame(ventana, width = 1200, height = 600)
frame.pack()

label = Label(frame, text = "Validador de contraseña", font=20)
label.grid(row=0, column=2)

label2 = Label(frame, text = "Ingrese contraseña", font=15)
label2.grid(row=1, column=1, padx=20, pady=20)

label3 = Label(frame, text = "Resultado", font=15)
label3.grid(row=2, column=1, padx=20, pady=20 )


contraseña = StringVar() #creo una variable de tipo string
cuadroTexto = Entry(frame, textvariable = contraseña)#Cuadro para ingresar la contraseña
cuadroTexto.grid(row=1, column=2, padx=20, pady=20)# posicion del cuadro de texto
cuadroTexto.config(justify="center", show="°")


def codigoBoton():
    verificar = contraseña.get()
    validador = re.search("(?=.*[A-Z]{1,2})(?=.*[a-z]{4,20})(?=.*[0-9]{2,10})(?=.*[@#$%&/?¿<>^-])",verificar)
    if validador != None:
        label4 = Label(frame, text = "La contraseña es segura")
        label4.grid(row=2, column=2, padx=20, pady=20)
    else:
        label4 = Label(frame, text = "La contraseña no es segura, debe contener:")
        label4.grid(row=2, column=2, padx=20, pady=20)
        label5 = Label(frame, text = "[entre 1 y 2]mayusculas, [entre 4 y 20]minusculas, \n [ entre 2 y 10]numeros, y simbolos especiales [@#$%&/?¿<>^-]")
        label5.grid(row=3, column=2, padx=20, pady=20)

boton = Button(frame, text = "Validar", command = codigoBoton)
boton.grid(row=1,column=3, padx=20, pady=20)



ventana.mainloop()