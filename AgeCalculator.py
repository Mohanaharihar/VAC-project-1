import tkinter 
from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.title('Age Calculator')
root.geometry("600x300")


def age():
	if my_entry.get():
		
		current_year = datetime.now().year
		
		your_age = current_year - int(my_entry.get())
		
		messagebox.showinfo("Your Age", f"Your Age Is: {your_age}")

	else:
		
		messagebox.showerror("Error", "You forgot to enter your age!")

my_label = Label(root, text="Enter Your Birth Year", font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calculate My Age!", font=("Helvetica", 18), command=age)
my_button.pack(pady=20)



root.mainloop()
