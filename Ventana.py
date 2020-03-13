from tkinter import *
import re

class Ventana:
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("validador De Contraseña")
        self.frame = Frame(self.ventana, width = 1200, height = 600)
        self.frame.pack()

        self.label = Label(self.frame, text = "Validador de contraseña", font=20)
        self.label.grid(row=0, column=2)

        self.label2 = Label(self.frame, text = "Ingrese contraseña", font=15)
        self.label2.grid(row=1, column=1, padx=20, pady=20)

        self.label3 = Label(self.frame, text = "Resultado", font=15)
        self.label3.grid(row=2, column=1, padx=20, pady=20 )

        self.label5 = Label(self.frame, text = """La contraseña debe contener:
        [entre 1 y 2]mayusculas, [entre 4 y 20]minusculas,
        [ entre 2 y 10]numeros, y simbolos especiales [@#$%&/?¿<>^-]""")
        self.label5.grid(row=3, column=2, padx=20, pady=20)



        self.contraseña = StringVar() #creo una variable de tipo string
        self.cuadroTexto = Entry(self.frame, textvariable = self.contraseña)#Cuadro para ingresar la contraseña
        self.cuadroTexto.grid(row=1, column=2, padx=20, pady=20)# posicion del cuadro de texto
        self.cuadroTexto.config(justify="center", show="°")


        self.boton = Button(self.frame, text = "Validar", command = self.codigoBoton)
        self.boton.grid(row=1,column=3, padx=20, pady=20)
        self.ventana.mainloop()

    def codigoBoton(self):
        self.verificar = self.contraseña.get()
        self.validador = re.search("(?=.*[A-Z]{1,2})(?=.*[a-z]{4,20})(?=.*[0-9]{2,20})(?=.*[@#$%&/?¿<>^-])",self.verificar)
        if self.validador != None:
            self.label4 = Label(self.frame, text = "La contraseña es segura")
            self.label4.grid(row=2, column=2, padx=20, pady=20)
            self.label.after(2000 , self.label4.destroy)
        else:
            self.label4 = Label(self.frame, text = "La contraseña no es segura")
            self.label4.grid(row=2, column=2, padx=20, pady=20)
            self.label.after(2000 , self.label4.destroy)
