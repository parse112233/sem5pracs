from tkinter import *
import math
root = Tk()

C = Canvas(root, bg="white", height=850, width=850)

a1, a2 = 126, 154
b1, b2 = 395, 154
c1, c2 = 395, 454
d1, d2 = 126, 454

C.create_polygon( a1,a2,b1,b2,c1,c2,d1,d2,fill="blue")

angle = int(input("Enter an angle: "))

xsh1 = -a1 + a2 * math.tan(math.radians(angle))
xsh2 = -d1 + d2 * math.tan(math.radians(angle))

C.create_polygon( xsh1,a2,xsh2,b2,c1,c2,d1,d2,fill="red")

C.pack()
mainloop()