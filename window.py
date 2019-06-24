
import tkinter as tk 
window = tk.Tk()
window.title("Sample App")
window.geometry("800x800") 

# Label
prompt = tk.Label(text="Hello! Learn about Tkinter module to make GUI.")
prompt.grid() 

#Entry Fields
entry_field = tk.Entry()
entry_field.grid()

#Button
button1 = tk.Button(text="Click Me!", bg="BLUE")
button1.grid()

# Text Fields
text_field = tk.Text(master=window, height=90, width=90)
text_field.grid()


window.mainloop()
