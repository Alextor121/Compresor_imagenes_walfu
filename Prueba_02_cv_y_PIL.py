from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os
import cv2

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file dialog window
file_path = filedialog.askopenfilename()
file_name = os.path.basename(file_path)

image_cv2 = cv2.imread(file_path)

altura, ancho, canales = image_cv2.shape

factor = 0.5

nancho = int(factor * ancho)
nalto = int(factor * altura)

imagen_reduc = cv2.resize(image_cv2, (nancho, nalto))


imagen_pill = Image.fromarray(cv2.cvtColor(imagen_reduc, cv2.COLOR_BGR2RGB))

fact2 = 60

imagen_pill.save('data/salidas/' + str(fact2) + ' ' + file_name, optimize=True, quality=fact2)
imagen_pill.close()

