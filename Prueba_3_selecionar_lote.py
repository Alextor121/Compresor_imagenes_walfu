from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os
import cv2

def comprimir(direccion, factor_tam):
    file_name = os.path.basename(direccion)
    image_cv2 = cv2.imread(direccion)
    altura, ancho, _ = image_cv2.shape

    nancho = int(factor_tam * ancho)
    nalto = int(factor_tam * altura)
    imagen_reduc = cv2.resize(image_cv2, (nancho, nalto))
    imagen_pill = Image.fromarray(cv2.cvtColor(imagen_reduc, cv2.COLOR_BGR2RGB))
    fact2 = 70
    imagen_pill.save('data/salidas1/'+ 'COMP_' + file_name, optimize=True, quality=fact2)
    imagen_pill.close()


# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file dialog window
folder_path = filedialog.askdirectory()
folder_name = os.path.basename(folder_path)

files = os.listdir(folder_path)
jpg_files = [file for file in files if file.endswith('.jpg')]

print("List of .jpg files:")
for jpg_file in jpg_files:
    comprimir(folder_path + '/' + jpg_file, 0.6)
    print(jpg_file)