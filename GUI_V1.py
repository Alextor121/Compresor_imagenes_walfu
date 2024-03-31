from PIL import Image
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import os
import cv2
import pyautogui

class ventana_compresor(ctk.CTk):
    def __init__(self):
        self.directorio_de_origen = ""
        self.directorio_de_salida = ""
        self.estado_init_reduc = 60
        self.estado_init_compress = 40

        super().__init__()
        self.geometry(self.size_window())
        self.title('Compresor imagenes WALFU')

        self.frame1 = ctk.CTkFrame(master=self)
        self.frame1.pack(side='top', fill=ctk.X)
        self.subframe11 =  ctk.CTkFrame(master=self.frame1)
        self.subframe11.pack(side='top', fill=ctk.X)
        self.titulo = ctk.CTkLabel(master=self.subframe11, text="COMPRESOR DE IMÁGENES", font=('Arial Rounded MT', 16))
        self.titulo.pack(side='left', padx=15, pady=10)
        self.marca = ctk.CTkLabel(master=self.subframe11, text="WALFU", font=('Arial Rounded MT', 16))
        self.marca.pack(side='right', padx=15, pady=10)
        # Frame 2 - sleeccion de carpeta
        self.frame2 = ctk.CTkFrame(master=self)
        self.frame2.pack(side='top', pady=5, fill=ctk.X)
        self.subframe21 = ctk.CTkFrame(master=self.frame2)
        self.subframe21.pack(side='top', fill=ctk.X)
        self.mensaje_sel_carpeta = ctk.CTkLabel(master=self.subframe21, text='Selecciona las carpetas', font=('Arial', 16))
        self.mensaje_sel_carpeta.pack(side='left', padx=(15,5), pady=(0,10))

        self.subframe22 = ctk.CTkFrame(master=self.frame2)
        self.subframe22.pack(side='top', fill=ctk.X, ipady=10)
        self.boton_origen = ctk.CTkButton(master=self.subframe22, text='CARPETA ORIGEN', command=self.sel_carp_orig)
        self.boton_origen.pack(side='left', padx=(15,2))
        self.texto_origen = ctk.CTkTextbox(master=self.subframe22, height=1)
        self.texto_origen.insert(1.0, "")
        self.texto_origen.configure(state='disabled')
        self.texto_origen.pack(side='right', padx=(2,15))

        self.subframe23 = ctk.CTkFrame(master=self.frame2)
        self.subframe23.pack(side='top', fill=ctk.X, ipady=10)
        self.boton_salida = ctk.CTkButton(master=self.subframe23, text='CARPETA SALIDA', command=self.sel_carp_sal)
        self.boton_salida.pack(side='left', padx=(15,2))
        self.texto_salida = ctk.CTkTextbox(master=self.subframe23, height=1)
        self.texto_salida.insert(1.0, "")
        self.texto_salida.configure(state='disabled')
        self.texto_salida.pack(side='right', padx=(2,15))

        # Frame 3 configuracion de parametros
        self.frame3 = ctk.CTkFrame(master=self)
        self.frame3.pack(side='top', pady=(0,5), fill=ctk.X)
        self.subframe31 = ctk.CTkFrame(master=self.frame3)
        self.subframe31.pack(side='top', fill=ctk.X)
        self.mensaje_param = ctk.CTkLabel(master=self.subframe31, text='Configuración de parámetros', font=('Arial', 16))
        self.mensaje_param.pack(side='left', padx=(15,5), pady=(0,5))

        # Selección de reducción de la imagen
        self.subframe32 = ctk.CTkFrame(master=self.frame3)
        self.subframe32.pack(side='top', fill=ctk.X, ipady=5)
        self.texto_reducc = ctk.CTkLabel(master=self.subframe32, text='Porcentaje de reducción de la imagen', font=('Arial', 14))
        self.texto_reducc.pack(side='left', padx=15)
        self.subframe33 = ctk.CTkFrame(master=self.frame3)
        self.subframe33.pack(side='top', fill=ctk.X, ipady=5)
        self.slider_reduc = ctk.CTkSlider(master=self.subframe33, from_= 0, to=99, command=self.porcent_reduc, width=300)
        self.slider_reduc.set(self.estado_init_reduc)
        self.slider_reduc.pack(side='left', padx=15)
        self.estado_slider_reduc = ctk.CTkTextbox(master=self.subframe33, height=1, width=50)
        self.estado_slider_reduc.insert(1.0, str(self.estado_init_reduc) + "%")
        self.estado_slider_reduc.configure(state='disabled')
        self.estado_slider_reduc.pack(side='right', padx=(2,15))

        # Selección de compresión de la imagen
        self.subframe34 = ctk.CTkFrame(master=self.frame3)
        self.subframe34.pack(side='top', fill=ctk.X, ipady=5)
        self.texto_compress = ctk.CTkLabel(master=self.subframe34, text='Porcentaje de compresión de la imagen', font=('Arial', 14))
        self.texto_compress.pack(side='left', padx=15)
        self.subframe35 = ctk.CTkFrame(master=self.frame3)
        self.subframe35.pack(side='top', fill=ctk.X, ipady=5)
        self.slider_compress = ctk.CTkSlider(master=self.subframe35, from_= 0, to=99, command=self.porcent_compress, width=300)
        self.slider_compress.set(self.estado_init_compress)
        self.slider_compress.pack(side='left', padx=15)
        self.estado_slider_compress = ctk.CTkTextbox(master=self.subframe35, height=1, width=50)
        self.estado_slider_compress.insert(1.0, str(self.estado_init_compress) + "%")
        self.estado_slider_compress.configure(state='disabled')
        self.estado_slider_compress.pack(side='right', padx=(2,15))

        # Botón de ejecutar
        self.frame4 = ctk.CTkFrame(master=self)
        self.frame4.pack(side='top', pady=(0,15), fill=ctk.X)
        self.subframe41 = ctk.CTkFrame(master=self.frame4)
        self.subframe41.pack(side='top', fill=ctk.X, ipady=5)
        self.mensaje_param = ctk.CTkLabel(master=self.subframe41, text='Ejecución', font=('Arial', 16))
        self.mensaje_param.pack(side='left', padx=(15,5), pady=(0,10))
        self.boton_iniciar = ctk.CTkButton(master=self.subframe41, text='COMPRIMIR', command=self.ejecutar_compress)
        self.boton_iniciar.pack(side='right', padx=(2,15))
        self.subframe42 = ctk.CTkFrame(master=self.frame4)
        self.subframe42.pack(side='top', fill=ctk.X, ipady=5)
        self.datalogger = ctk.CTkTextbox(master=self.subframe42)
        self.datalogger.insert(1.0, "")
        self.datalogger.configure(state='disabled')
        self.datalogger.pack(side='top', padx=15, pady=(0,10), fill=ctk.X)


    def size_window(self, pancho:float = 0.25, palto:float = 0.5) -> str:
        ancho, alto = pyautogui.size()
        return str(int(ancho*pancho)) + 'x' + str(int(alto*palto))

    def sel_carp_orig(self) -> None:
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Open a file dialog window
        self.directorio_de_origen = filedialog.askdirectory()
        print(self.directorio_de_origen)
        self.texto_origen.configure(state='normal')
        self.texto_origen.delete(1.0, ctk.END)
        self.texto_origen.insert(1.0, self.directorio_de_origen)
        self.texto_origen.configure(state='disabled')
        root.destroy()
    
    def sel_carp_sal(self) -> None:
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Open a file dialog window
        self.directorio_de_salida = filedialog.askdirectory()
        print(self.directorio_de_salida)
        self.texto_salida.configure(state='normal')
        self.texto_salida.delete(1.0, ctk.END)
        self.texto_salida.insert(1.0, self.directorio_de_salida)
        self.texto_salida.configure(state='disabled')
        root.destroy()

    def porcent_reduc(self, valor):
        valor = int(valor)
        self.estado_init_reduc = valor
        self.estado_slider_reduc.configure(state='normal')
        self.estado_slider_reduc.delete(1.0, ctk.END)
        self.estado_slider_reduc.insert(1.0, str(valor) + "%")
        self.estado_slider_reduc.configure(state='disabled')
    
    def porcent_compress(self, valor):
        valor = int(valor)
        self.estado_init_compress = valor
        self.estado_slider_compress.configure(state='normal')
        self.estado_slider_compress.delete(1.0, ctk.END)
        self.estado_slider_compress.insert(1.0, str(valor) + "%")
        self.estado_slider_compress.configure(state='disabled')

    def comprimir(self, direccion):
        file_name = os.path.basename(direccion)
        image_cv2 = cv2.imread(direccion)
        altura, ancho, _ = image_cv2.shape

        nancho = int((self.estado_init_reduc/100) * ancho)
        nalto = int((self.estado_init_reduc/100) * altura)
        imagen_reduc = cv2.resize(image_cv2, (nancho, nalto))
        imagen_pill = Image.fromarray(cv2.cvtColor(imagen_reduc, cv2.COLOR_BGR2RGB))
        fact2 = 100 - self.estado_init_compress
        imagen_pill.save(self.directorio_de_salida + '/COMP_' + file_name, optimize=True, quality=fact2)
        imagen_pill.close()
    
    def ejecutar_compress(self):
        files = os.listdir(self.directorio_de_origen)
        jpg_files = [file for file in files if file.endswith('.jpg')]
        for jpg_file in jpg_files:
            self.comprimir(self.directorio_de_origen + '/' + jpg_file)
            self.dataprint("Comprimida: " + jpg_file,1)
    
    def dataprint(self, texto:str, endline:int = 0) -> None:
        self.datalogger.configure(state='normal')
        self.datalogger.insert('end', texto)
        if endline:
            self.datalogger.insert('end', "\n")
        self.datalogger.configure(state='disabled')



a = ventana_compresor()
a.mainloop()
