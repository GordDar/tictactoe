import time
import random
from tkinter import *
from tkinter import messagebox

tk = Tk()
app_running = True

size_canvas_x = 600
size_canvas_y = 600


def on_closing():
    global app_running
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app_running = False
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Игра крестики-нолики")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0,0, size_canvas_x, size_canvas_y, fill='white')
canvas.pack()
tk.update()

size_x = 3
size_y = size_x
step_x = size_canvas_x // size_x
step_y = size_canvas_y // size_y


def draw_table():
    for i in range(0, size_x + 1):
        canvas.create_line(0, i * step_y, size_canvas_x, i * step_y)
    for i in range(0, size_y + 1):
        canvas.create_line(i * step_x, 0, i * step_x, size_canvas_y)

points = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
list_ids = []
draw_table()

class Point():
    def __init__(self, x,y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return str(self.__class__)+': '+str(self.__dict__)

def draw_point(x, y,type):
    size = 25
    color='black'
    id =0
    if type==0:
        color = 'red'
        id = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(x * step_x+size, y * step_y+size, x * step_x + step_x-size, y * step_y + step_y-size, fill='white')
        list_ids.append(id)
        list_ids.append(id2)
    if type==1:
        color='blue'
        id = canvas.create_rectangle(x * step_x, y * step_y+step_y//2-step_y//10, x * step_x+step_x, y * step_y + step_y//2+step_y//10, fill=color)
        id2 = canvas.create_rectangle(x * step_x+step_x//2-step_x//10, y * step_y, x * step_x+step_x//2+step_x//10, y * step_y + step_y, fill=color)
        list_ids.append(id)
        list_ids.append(id2)
    # id=canvas.create_oval(x*step_x, y*step_y, x*step_x+step_x, y*step_y+step_y, fill=color)


def add_to_points(event):
    # print(event.num, event.x, event.y)
    global points
    type=0
    if event.num==3:
        type=1
    if points[event.x//step_x][event.y//step_y]==-1:
        points[event.x//step_x][event.y//step_y]= type
        draw_point(event.x//step_x, event.y//step_y, type)
        if check_winner(type):
            print("Победитель!", type)
            points = [[10,10,10], [10,10,10], [10,10,10]]
    # print(' '.join(map(str, points)))


canvas.bind_all("<Button-1>", add_to_points)
canvas.bind_all("<Button-3>", add_to_points)



def button_press():
    global list_ids
    global points
    for i in list_ids:
        canvas.delete(i)
    list_ids = []
    points = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

button = Button(tk, text='Нажми меня! Начать игру заново', command =button_press)
button.pack()

def check_winner(winner):
    for j in range(0, size_y):
        win=True
        for i in range(0, size_x):
            if points[j][i] != winner:
                win=False
        if win:
            return True
    for j in range(0, size_y):
        win=True
        for i in range(0, size_x):
            if points[i][ j] != winner:
                win=False
        if win:
            return True
    win = True
    for i in range(0, size_y):
        if points[i][i] != winner:
            win=False
    if win:
        return True
    j = size_y-1
    win=True
    for i, j in zip(range(0, size_x), range(size_y-1, -1, -1)):
        if points[i][j] != winner:
            win=False
            j = j-1
    if win:
        return True


while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep((0.005))
