from tkinter import *  #Esta libreria nos permite ayuda a crear las ventanas

raiz = Tk() # con esto creo una nueva ventana
raiz.title("Ventana de prueba") # Añade un titulo a la ventana
#raiz.resizable(True,True) # width, heigh parametros. Permite controlar la extencion de la ventana
raiz.iconbitmap("password.ico") # permite cambiar el icono de la ventana
#raiz.geometry("650x350") #controla el tamaño inicial de la pantalla
raiz.config(bg = "blue") # color de fondo

frame = Frame()
#frame.pack(side = TOP) # ubica la posicion del frame
frame.pack()
frame.config(bg = "red")
frame.config(width = "650", height = "350")
raiz.mainloop() # esto es como un bucle infinito que permite ejecutar la ventana colocarlo siempre de ultimo  
