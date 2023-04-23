#Import required libraries
import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from PIL import Image, ImageDraw

#Create main window
root = tk.Tk()
root.title("Paint App")

#Create a canvas
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

#Create an image and draw instance
image = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(image)

#Initialize variables
x1, y1 = None, None
color = "black"
size = 5

#Define event handlers
def start_draw(event):
    global x1, y1
    x1, y1 = event.x, event.y

def continue_draw(event):
    global x1, y1
    x2, y2 = event.x, event.y
    canvas.create_line((x1, y1, x2, y2), fill=color, width=size, capstyle="round", smooth="true")
    draw.line((x1, y1, x2, y2), fill=color, width=size)
    x1, y1 = x2, y2

def choose_color():
    global color
    color = colorchooser.askcolor()[1]

def choose_size(s):
    global size
    size = s

def save_image():
    filename = "painting.png"
    image.save(filename)
    messagebox.showinfo("Paint App", f"Image saved as {filename}")

def clear_canvas():
    canvas.delete("all")
    global image, draw
    image = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(image)

#Create toolbar
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")

color_button = tk.Button(toolbar, text="Choose color", command=choose_color)
color_button.pack(side="left")

size_label = tk.Label(toolbar, text="Brush size:")
size_label.pack(side="left")

size_1_button = tk.Button(toolbar, text="1", command=lambda: choose_size(1))
size_1_button.pack(side="left")
size_5_button = tk.Button(toolbar, text="5", command=lambda: choose_size(5))
size_5_button.pack(side="left")
size_10_button = tk.Button(toolbar, text="10", command=lambda: choose_size(10))
size_10_button.pack(side="left")

clear_button = tk.Button(toolbar, text="Clear", command=clear_canvas)
clear_button.pack(side="right")

save_button = tk.Button(toolbar, text="Save", command=save_image)
save_button.pack(side="right")

#Bind event handlers
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", continue_draw)

#Start main loop
root.mainloop()
