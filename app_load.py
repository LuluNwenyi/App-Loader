from tkinter import *
from tkinter.ttk import * 
import tkinter.filedialog
import os, sys, subprocess

root = Tk() 
root.title("My App Runner")
root.geometry("350x400")


#app list
apps = []

#to make sure the app doesn't enter an empty value to the list
if os.path.isfile('save.txt'):
    with open('save.txt', "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] #removes the empty value
    
#to add the app
def addApp():
    
    for widget in myCanvas.winfo_children():
        widget.destroy()
        
    filename= tkinter.filedialog.askopenfilename( initialdir=".", title= "Select a File", 
    filetypes = (("executables", "*.app"), ("all files,", "*.*")))
    
    apps.append(filename)
    print(filename)
    
    for app in apps:
        label= Label(myCanvas, text= app, background= "gray")
        label.pack()
 
#to run the app

def runApps():
    for app in apps:
        subprocess.call(["open", app])
       

#background
myCanvas= Canvas(root, width=350, height=350, background= "#2242B4")
myCanvas.pack()

#buttons
myButton = Button(root, text = 'Open Files', command= addApp)
runButton = Button(root, text= "Run Apps", command= runApps)

myButton.pack(side=BOTTOM)
runButton.pack(side=BOTTOM)

root.mainloop()

#to save the apps
with open("save.txt", 'w') as f:
    for app in apps:
        f.write(app + ',')