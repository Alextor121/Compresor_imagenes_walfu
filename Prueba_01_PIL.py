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

# Input image file
input_image = Image.open(file_path)

# Compress image
for a in range(100,0,-2):
    q = a
    input_image.save('data/salidas/' + str(q) + ' ' + file_name, optimize=True, quality=q)

# Close input image
input_image.close()

