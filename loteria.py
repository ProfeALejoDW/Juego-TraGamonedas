import tkinter as tk     #  para generar objetos 
from tkinter import PhotoImage  # para llamar imagenes 
from PIL import Image, ImageTk  # para generar o cargar imagenes 
import random  # generar a azar
import os  # activa rutas y protocolos 


# de donde obtengo la informacion 
# donde guardo la informacion 
# donde se va a ver 
# donde se va a generar el aviso  " GANo o PERDIO "
# como controlo  cuando esta activo o apagado 
 
# acomodemos el espacio de trabajo 
ruta_imagen = r"C:\Users\ASUS\Desktop\Loteria\imagenes\imagenes"
imagenes = []   # el arreglo sirve para guardar multiples valores temporales 
columnas = [0, 0, 0]  # genera los lugares donde van a salir las cosas 
label = []   # esto se genera cuando quiero utilizar una etiqueta varias veces 
girando =  True # servira para controlar el juego 

# LLamado de imagenes
def llamar_imagenes():
    lista = []
    
    for archivo in os.listdir(ruta_imagen):  # realiza el barrido para las imagenes 
        if archivo.endswith(".png"):  # comando endswing llama a todo lo que termine en un tipo de archivo especifico  
             ruta = os.path.join(ruta_imagen, archivo)   # invoca a las imagenes de las rutas especificas 
             img = Image.open(ruta).resize ( (100,100))  # abre la imagen y le cambia de tamño 
             lista.append(ImageTk.PhotoImage(img))  # agrega el nuevo elemento en cada pasada 
    return lista

# funcion para el GIRO 

def iniciar_giro():
    global girando
    girando = True
    boton_girar.config(state=tk.DISABLED)
    boton_detener.config(state=tk.NORMAL)        
    resultado_label.config (text=" ")
    animar()
    
# animar las imagenes para el movimiento     
def animar():
    if girando:
        for i in range(3):
            columnas[i] = random.randint(0, len(imagenes) - 1 )     # llama a la posicion dentro de las columnas         
            label[i].config(image=imagenes[columnas[i]])        # genera las imagenes que va llamando en las posiciones contraoladas por columna 
        ventana.after(20, animar)                   
    
def detener_giro():
    global girando
    girando = False
    boton_girar.config(state=tk.NORMAL)
    boton_detener.config(state=tk.DISABLED)
    
    if columnas[0] == columnas[1] == columnas[2]:
        resultado_label.config(text="GANASTE ")
    else:
        resultado_label.config(text=" Perdiste")
   
   
# Interfaz 
ventana = tk.Tk()
ventana.title ( "Tragamonedas") 
ventana.geometry("400x400")
ventana.config(bg="black")
 
imagenes = llamar_imagenes()

# mostrar las imagenes iniciales 

for i in range(3):
    lbl = tk.Label(ventana, image=imagenes[0], bg="black") 
    lbl.grid ( row=0, column=i, padx=10, pady=40)
    label.append(lbl)

# boton girar     
boton_girar = tk.Button(ventana, text="Girar" , font="Arial", bg="green" , fg="white", command=iniciar_giro)    
boton_girar.grid(row=1, column= 0 , columnspan=3, pady=10)        

# boton detener         
boton_detener= tk.Button(ventana, text= "Detener" , font="Arial", bg="red",fg="white" , command=detener_giro )
boton_detener.grid(row=2 , column=0 , columnspan=3)

# label de resultado 
resultado_label= tk.Label( ventana, text= " " ,font="Arial", fg= "yellow" ,bg="black")
resultado_label.grid(row=3, column=0 , columnspan=3, pady=10)

        
ventana.mainloop()  
    








