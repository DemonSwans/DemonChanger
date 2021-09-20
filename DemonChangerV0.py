import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
filepath = filedialog.askopenfilenames(title='DemonChanger')
path = os.getcwd() +"\ "
print("Podaj nową nazwe dla zaznaczonych plików:")
newname = input()
i= 1
for file in filepath: 
    name, ext = os.path.splitext(file)
    os.rename(file,path+newname+"["+str(i)+"]"+ext)
    i=i+1
print("Zmieniono wszystkie nazwy zaznaczonych plików na "+newname)
