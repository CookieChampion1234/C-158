from tkinter import*
root=Tk()
root.title("Geometry Error")

try:
    root.geometry("600")
except:
    print("Bad geometry error, must have 2 dimensions not 1!")
    
root.mainloop()
