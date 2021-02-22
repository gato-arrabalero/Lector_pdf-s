import tkinter as tk
import PyPDF2  # -------> modulo para manipulacion de Pdf´s
from PIL import Image,ImageTk  # ------> modulo manipulacion de imagenes e iconos ---> la bibliteca Pil funciona hasta 2.7 ver pero su contraparte es PILLOW  y funciona de la misma forma 
from tkinter.filedialog import askopenfile #------> Modulo necesario para abrir cuadros de  dialogo


root = tk.Tk() # ------->Raiz nuestra ventana principal donde caeran los widgets

#Canvas o lienzon en español sera una variable que asignaremos sera un widget asignado a nuestro root que a su vez contendra mas widgets t modificaremos su tamaño
#que a su vez recive tres parametreso la raiz que lo aloja, ancho y largo en pixeles

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan = 3, rowspan = 3)

#logo

logo = Image.open('logo.png') #------>variable para ruta = Clase Image.metodo_open(ruta de nuestra imagen)
logo = ImageTk.PhotoImage(logo) #------> variable = Clase ImageTk.metodo_PhotoImage(variable de la ruta)
logo_label = tk.Label(image = logo) #------> variable_etiqeta = Clase tkinter.metodo_label(parametro que idica que esta etiqyeta sera una imagen = variable de nuestra ruta)
logo_label.image = logo #------> variable de tal etiqueta.propiedad tipo imagen = vaiable de la ruta
logo_label.grid(column = 1, row = 0) # Metodo grid par colocarla en la ventana 

#Instrucciones

instrucciones = tk.Label(root, text = 'Seleciona desde tu computadora el PDF, del cual quieres extraer su texto')
instrucciones.grid(columnspan = 3, column = 0, row = 1)

#Funcion para que funcione el boton  de buscar

def buscar_pdf ():
    buscador_text.set('cargando ......') #--------------> Carga la neuva cadena de texto al boton que creamos 
    file = askopenfile(parent = root , mode = 'rb', title = 'Elige tu archivo PDF', filetype = [('Archivos PDF ', '*.pdf' )]) #Variable que contendra la carga del PDF para despues poder suarla 
    if file:
        leer_pdf = PyPDF2.PdfFileReader(file) #Primero leemos el mediante el metodo PdfFileReader del modulo PyPDF2 y pasandole la variable que almacena el PDF
        pagina = leer_pdf.getPage(0) #Variable pagina es para obtener la primera pagina del documento con la variable de lectura y em metodo getPage en indie 0  
        contenido_pagina = pagina.extractText() #Vaciamos la obtecion de get a una variable nueva mediante el metodo extrattext
        
        #Caja de Texto

        caja_text = tk.Text(root, height = 10, width = 50 , padx = 15 , pady = 15 )
        caja_text.insert(1.0, contenido_pagina)
        caja_text.grid (column = 1, row = 3)
        buscador_text.set('Buscar PDF .....')

        
#Boton Buscador  ------> el boton llevara una lambda con el nombre dela funcion cerada anteriormente 

buscador_text = tk.StringVar() #---------> Variable Buscador_text = del modulo tk.el_metodo_StringVar 
buscador_btn = tk.Button(root, textvariable = buscador_text, command = lambda:buscar_pdf(), height = 2, width = 15, font = 10 ) #-------> variable del boton = modulo tk.Metodo_Button(root-->donde va enpotrado, recibira _una_variable_de_tetxo = al_stringvar_que _creamos  )
buscador_text.set('Buscar PDF .....') #-------> al inicio sin accion dira el boton Buscar
buscador_btn.grid(column = 1, row = 2) #---------> Lo colocamos mediante grid

#Cuadro de texto donde va ir la extraciion 


canvas2 = tk.Canvas(root, width = 600, height = 280)
canvas2.grid(columnspan = 3,)


root.mainloop() # -------> un ciclo infinito de nuestra raiz para queno se cierre inmediatamnete al ser invocada
