import tkinter as tk
from tkinter import Menu
import random

# Tạo cửa sổ game
window = tk.Tk()
window.title("Nguyễn Kỳ Vĩ")
window.geometry("600x400")

# Tạo vùng canvas cho game
canvas = tk.Canvas(window, width=600, height=400, bg="black")
canvas.pack()

# Các biến cần thiết
snake_direction = "Right"
snake_body = [(300, 200), (290, 200), (280, 200)]
food_position = (100, 100)
GAME_WIDTH = 600
GAME_HEIGHT = 400
game_running = True

# Hàm thay đổi hướng di chuyển của rắn
def change_direction(new_direction):
    global snake_direction
    opposite_directions = {
        "Up": "Down", "Down": "Up",
        "Left": "Right", "Right": "Left"
    }
    if opposite_directions.get(new_direction) != snake_direction:
        snake_direction = new_direction

# Hàm game over
def game_over():
    canvas.create_text(
        GAME_WIDTH // 2, GAME_HEIGHT // 2,
        text="GAME OVER", fill="white", font=("Arial", 24)
    )
    global game_running
    game_running = False  # Dừng game khi game over

# Hàm vẽ rắn
def draw_snake():
    for segment in snake_body:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green") 

# Hàm vẽ thức ăn
def draw_food():
    canvas.create_oval(food_position[0], food_position[1], food_position[0] + 10, food_position[1] + 10, fill="red")

# Hàm đặt thức ăn mới
def place_food():
    global food_position
    food_position = (random.randint(0, (GAME_WIDTH // 10) - 1) * 10, random.randint(0, (GAME_HEIGHT // 10) - 1) * 10)

# Hàm di chuyển rắn
def move_snake():
    global snake_body, snake_direction, game_running

    if not game_running:
        return

    # Tạo một bản sao của rắn
    new_head = list(snake_body[0])
    
    if snake_direction == "Up":
        new_head[1] -= 10
    elif snake_direction == "Down":
        new_head[1] += 10
    elif snake_direction == "Left":
        new_head[0] -= 10
    elif snake_direction == "Right":
        new_head[0] += 10

    snake_body = [tuple(new_head)] + snake_body[:-1]

    # Kiểm tra va chạm với tường
    if (new_head[0] < 0 or new_head[0] >= GAME_WIDTH or 
        new_head[1] < 0 or new_head[1] >= GAME_HEIGHT):
        game_over()
        return

    # Kiểm tra va chạm với chính rắn
    if new_head in snake_body[1:]:
        game_over()
        return

    # Vẽ lại rắn và thức ăn
    canvas.delete("all")
    draw_snake()
    draw_food()

    # Kiểm tra va chạm với thức ăn
    if new_head == list(food_position):
        snake_body.append(snake_body[-1])  # Tăng kích thước rắn
        place_food()

    window.after(100, move_snake)

# Tạo menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Tạo menu File
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Game", command=lambda: restart_game())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Tạo menu Help
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

# Hàm khởi động lại game
def restart_game():
    global snake_body, snake_direction, game_running
    snake_body = [(300, 200), (290, 200), (280, 200)]
    snake_direction = "Right"
    game_running = True
    canvas.delete("all")
    place_food()
    draw_snake()
    draw_food()
    move_snake()

# Gán các phím điều khiển rắn
window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))
window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Right>", lambda event: change_direction("Right"))

# Khởi động game
place_food()
draw_snake()
draw_food()
move_snake()

# Chạy vòng lặp sự kiện của cửa sổ
window.mainloop()