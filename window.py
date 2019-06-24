
import tkinter as tk 
window = tk.Tk()
window.title("Bhaumik App")
window.geometry("800x800") 

# Label
prompt = tk.Label(text="Hello World. Welcome to CS50 and welcome to my app")
prompt.grid() 

#Entry Fields
entry_field = tk.Entry()
entry_field.grid()

#Button
button1 = tk.Button(text="Click Me!", bg="RED")
button1.grid()

# Text Fields
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()


window.mainloop()
