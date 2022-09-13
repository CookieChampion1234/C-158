from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Geometry")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()
def addition():
    number = 5
    get_input = input_box.get()
    try:
        print(number + get_input)
    except(TypeError):
        messagebox.showinfo("Error", "Cannot add two different data types strings and integers")
        
btn=Button(root, text="addition", command=addition)
btn.pack()
root.mainloop()