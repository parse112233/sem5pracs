from tkinter import *
import math
root = Tk()

C = Canvas(root, bg="white", height=850, width=850)

x1,y1 = 292, 142
x2,y2 = 394, 76
x3,y3 = 394, 109
x4,y4 = 495, 109
x5,y5 = 495, 177
x6,y6 = 394, 177
x7,y7 = 394, 209

C.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7, fill="red")


C.pack()
mainloop()