
import tkinter as tk
from turtle import Turtle, Screen

def draw_polygon():
    num_sides = int(entry.get())
    if num_sides < 3:
        return  # Cannot draw a polygon with less than 3 sides
    
    turtle_window = Screen()
    turtle_window.title("Polygon Drawer")
    
    turtle = Turtle()
    turtle.speed(1)
    
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)
    
    turtle_window.mainloop()

# Create Tkinter window
root = tk.Tk()
root.title("Polygon Drawer")

label = tk.Label(root, text="Enter number of sides:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Draw Polygon", command=draw_polygon)
button.pack()

root.mainloop()