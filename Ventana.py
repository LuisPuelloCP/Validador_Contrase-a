from tkinter import *


ventana = Tk()
ventana.title("Validador")

frame = Frame(ventana, width = 1200, height = 600)
frame.pack()

label = Label(frame, text = "Validador de contraseña", font=20)
label.grid(row=0, column=2)

label = Label(frame, text = "Ingrese contraseña", font=15)
label.grid(row=1, column=1, pady=20)
cuadroTexto = Entry(frame)
cuadroTexto.grid(row=1, column=2, pady=20)
cuadroTexto.config(justify="center", show="°")

def codigoBoton():
    pass

boton = Button(frame, text = "Validar", command = codigoBoton)
boton.grid(row=1,column=3)



ventana.mainloop()