from tkinter import *
root = Tk()

C = Canvas(root, bg="white", height=250, width=250)

input("Enter something")


x=180
y=50
p=140
q=110

C.create_text(150, 40, text="Oval before translation",)
oval = C.create_oval(x, y, p, q, fill="blue")
tx = 300
ty = 300
C.create_text(150, 80, text="Oval after translation")
C.create_oval(x+tx, y+ty, p+tx, q+ty, fill="pink")

C.create_rectangle(x,y,p,q)

C.pack()
mainloop()