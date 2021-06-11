# All the imports
from tkinter import *
import requests


# Let's start with the design of the GUI
root = Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.config(bg="#C2EFEB")

value = IntVar()

# Label for currency code
label_curr = Label(root, text="Your Currency Code", font=("Garuda", 15))
label_curr.config(bg="#ECFEE8")
label_curr.pack()

# Entry for currency code
entry_curr = Entry(root, text="Currency Code", font=("Garuda", 15))
entry_curr.pack()

# Label for currency value
label_val = Label(root, text="Your Currency Value", font=("Garuda", 15))
label_val.config(bg="#ECFEE8")
label_val.pack()

# Entry for currency value
entry_val = Entry(root, text="Value", font=("Garuda", 15))
entry_val.pack()


def convert_curr():
    url = "https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/" + entry_curr.get()
    information = requests.get(url).json()
    output = int(entry_val.get()) * information["conversion_rates"]["USD"]
    output_val.config(text=output)


# Output value
output_val = Label(root, text="Output", font=("Garuda", 15))
output_val.config(bg="#ECFEE8")
output_val.pack()


label_out = Label(root, text="(To USD)", font=("Garuda", 15))
label_out.config(bg="#ECFEE8")
label_out.pack()


convert_btn = Button(root, command=convert_curr, text="Convert", font=("Garuda", 15), width=10)
convert_btn.config(bg="#ECFEE8")
convert_btn.pack()


root.mainloop()
