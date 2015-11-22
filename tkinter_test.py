from Tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="white")
two = Label(root, text="Two", bg="green", fg="black")
three = Label(root, text="Three", bg="cyan", fg="white")

one.pack()
two.pack(fill=X)
three.pack(side=LEFT, fill=Y)

root.mainloop()