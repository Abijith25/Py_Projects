import tkinter as tk
from turtle import Turtle, Screen
 
def move_forward():
    distance = int(forward_entry.get())
    turtle.forward(distance)

def move_backward():
    distance = int(backward_entry.get())
    turtle.backward(distance)

def turn_left():
    angle = int(left_entry.get())
    turtle.left(angle)

def turn_right():
    angle = int(right_entry.get())
    turtle.right(angle)

# Create Tkinter window
root = tk.Tk()
root.title("MAKING SKETCHES")

# Create Turtle window
turtle_screen = Screen()
turtle_screen.title("SHAPE DESIGN")
turtle = Turtle()
turtle.speed(1)

# Labels and entries for movement

#   FORWARD LABEL
forward_label = tk.Label(root, text="Forward:")
forward_label.grid(row=0, column=0)

#   FORWARD ENTRY
forward_entry = tk.Entry(root)
forward_entry.grid(row=0, column=1)
forward_entry.insert(0,0)

#   FORWARD BUTTON
forward_button = tk.Button(root, text="Move Forward", command=move_forward)
forward_button.grid(row=0, column=2)

#   BACKWARD LABEL
backward_label = tk.Label(root, text="Backward:")
backward_label.grid(row=1, column=0)

#   BACKWARD ENTRY
backward_entry = tk.Entry(root)
backward_entry.grid(row=1, column=1)
backward_entry.insert(0,0)

#   BACKWARD BUTTON
backward_button = tk.Button(root, text="Move Backward", command=move_backward)
backward_button.grid(row=1, column=2)

#   LEFT LABEL
left_label = tk.Label(root, text="Left:")
left_label.grid(row=2, column=0)

#   LEFT ENTRY
left_entry = tk.Entry(root)
left_entry.grid(row=2, column=1)
left_entry.insert(0,0)

#   LEFT BUTTON
left_button = tk.Button(root, text="Turn Left", command=turn_left)
left_button.grid(row=2, column=2)

#   RIGHT LABEL
right_label = tk.Label(root, text="Right:")
right_label.grid(row=3, column=0)

#   RIGHT ENTRY
right_entry = tk.Entry(root)
right_entry.grid(row=3, column=1)
right_entry.insert(0,0)

#   RIGHT BUTTON
right_button = tk.Button(root, text="Turn Right", command=turn_right)
right_button.grid(row=3, column=2)

root.mainloop()
