import os
from glob import glob
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import shutil
from PIL import Image, UnidentifiedImageError

class Images:
    
    def add(self):
        try:
            Tk().withdraw() 
            filename = askopenfilename() 
            image = Image.open(filename)
            shutil.copy(filename, "images")
            print("Successfully Added Image")
        except FileNotFoundError:
            print("Operation cancelled")
        except UnidentifiedImageError:
            print("Invalid Image")

    def search(self, filename):
        try:
            image = Image.open("images\\" + filename)
            image.show()
        except FileNotFoundError:
            print("Image wasn't found, try uploading it first!")

    def list(self, path):
        arr = os.listdir(path)
        for i, image in enumerate(arr):
            print((i+1), "", image)  