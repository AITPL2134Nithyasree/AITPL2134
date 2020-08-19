from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

a=Tk()

#a.wm_iconbitmap("book.ico")
a.title("Untitled - Notepad")
a.geometry("700x400+100+100")
equation = StringVar()
   # input field for the expression
input_field = Entry(a, textvariable=equation)
input_field.place(height=700)

   # we are using grid position
   # for the arrangement of the widgets
input_field.grid(columnspan=4, ipadx=100, ipady=5)
   # settin the placeholder message for users
#equation.set("Enter the expression")
TextArea=Text(a,font=('arial',15))


scrollbar= Scrollbar(TextArea)
file=None


m1=Menu()
l1=Menu()
l1.add_command(label="NewFile")
l1.add_command(label="OpenFile")
l1.add_command(label="SaveFile")
l1.add_command(label="SaveAs")
l2=Menu()
l2.add_command(label="Copy")
l2.add_command(label="Paste")
l2.add_command(label="Undo")
l3=Menu()
l3.add_command(label="Word Wrap")
l3.add_command(label="Font...")
l4=Menu()
l4.add_cascade(label="Zoom")
l4.add_command(label="Statusbar")
l5=Menu()
l5.add_command(label="View Help")
l5.add_command(label="Send Feedback")
l5.add_command(label="About Notepad")

m1.add_cascade(label="File",menu=l1)
m1.add_cascade(label="Edit",menu=l2)
m1.add_cascade(label="Format",menu=l3)
m1.add_cascade(label="View",menu=l4)
m1.add_cascade(label="Help",menu=l5)
a.config(menu=m1)
a.mainloop()