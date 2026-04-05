from tkinter import *
import random

root = Tk()
root.title("SNAKE GAME")
root.resizable(False,False)

WIDTH = 800
HEIGHT = 650
SPEED = 150
SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
score = 0
direction = "right"

root.update_idletasks()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

WINDOW_HEIGHT = HEIGHT + 70

x = (screen_width // 2) - (WIDTH // 2) + 100
y = (screen_height // 2) - (HEIGHT // 2)

root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

label = Label(root, text=f"Score:{score}", font="Arial 30 bold" )
label.pack()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


# Creating Snake

snake = [(400,400), (350,400), (300,400)]

for (x,y) in snake:
    canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=SNAKE_COLOR, tag="snake")

# Creating food 

x_food = random.randint(1, (WIDTH//SIZE)-3)*SIZE
y_food = random.randint(1, (HEIGHT//SIZE)-3)*SIZE

food = (x_food, y_food)

foods = canvas.create_oval(x_food, y_food, x_food+SIZE, y_food+SIZE, fill=FOOD_COLOR, tag="food")

def gameover():
    canvas.delete("all")
    canvas.create_text(WIDTH/2, HEIGHT/2, text = "GAME OVER :(", fill = "red", font = "Arial 40 bold")

# MOVEMENT

def next_turn():

    global score
    global food
    global foods

    head_x, head_y = snake[0]

    if direction == "up":
       head_y -= SIZE
    
    if direction == "down":
        head_y += SIZE

    if direction == "right":
        head_x += SIZE
    
    if direction == "left":
        head_x -= SIZE

    new_head = (head_x, head_y)

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        gameover()
        return
    elif new_head in snake[1:]:
        gameover()
        return
    
    snake.insert(0, new_head)

    if new_head == food:
        score +=1
        label.config(text = f"Score: {score}")

        canvas.delete("food")

        x_new = random.randint(1, (WIDTH//SIZE)-3)*SIZE
        y_new = random.randint(1, (HEIGHT//SIZE)-3)*SIZE
        food=(x_new, y_new)
        foods = canvas.create_oval(x_new, y_new, x_new+SIZE, y_new+SIZE, fill=FOOD_COLOR, tag="food")
    else:
        snake.pop()

    canvas.delete("snake")
 
    for x,y in snake:
        canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=SNAKE_COLOR, tag="snake")    

    root.after(SPEED, next_turn)
    
next_turn()

# Key presses

def change_direction(event):
    global direction

    if event.keysym == "Up" and direction != "down":
        direction = "up"
    elif event.keysym == "Down" and direction != "up":
        direction = "down"
    elif event.keysym == "Left" and direction != "right":
        direction = "left"
    elif event.keysym == "Right" and direction != "left":
        direction = "right"

root.bind("<Key>", change_direction)

root.mainloop()
