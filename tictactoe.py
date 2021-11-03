from tkinter import *
import random, time

game=[None]*9
lol = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
matriza=lol(game, 3)
game_left=list(range(9))
turn=0
win=False

def push(b):
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text='X', bg='white', state='disabled')
    game_left.remove(b)
    if b==4 and turn==0:
        t = random.choice(game_left)
    elif b!=4 and turn==0:
        t=4
    if turn>0:
        t=8-b
        if t not in game_left:
            t= random.choice(game_left)
    game[t] = '0'
    game_left.remove(t)
    time.sleep(0.5)
    buttons[t].config(text='0', bg='white', state='disabled')
    turn += 1
    check_winner()
    if win==True:
        print("Победитель!", winner)
    matriza = lol(game, 3)
    print(matriza)

winner=[]

def check_winner():
    if turn > 0:
        for i in range(0, 3):
            if len(set(matriza[i])) == 1 and matriza[i][0] != None:
                winner.append(matriza[i])
                win=True
            elif len(set(zip(matriza[i]))) == 1 and matriza[i][0] != None:
                winner.append(matriza[i])
                win = True
            elif matriza[0][0] == matriza[1][1] == matriza[2][2] and matriza[0][0] != None:
                winner.append(matriza[0][0])
                win = True
            elif matriza[0][2] == matriza[1][1] == matriza[2][0] and matriza[0][2] != None:
                winner.append(matriza[0][2])
                win = True
            else:
                win=False
    print(winner)


root = Tk()
label=Label(width=20, text='Игра крестики-нолики', font=('Arial', 20, 'bold'))
buttons=[Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='green', command=lambda x=i: push(x)) for i in range(9)]
label.grid(row=0, column=0, columnspan=3)
row=1
column=0
for i in range(9):
    buttons[i].grid(row=row, column=column)
    column+=1
    if column==3:
        row+=1
        column=0


root.mainloop()
