import machine
import time
import math
import random
import ssd1306
import framebuf

# 定義搖桿和按鈕引腳
j_x = machine.ADC(2)
j_y = machine.ADC(0)
sw = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# 定義OLED 1306屏幕初始化
i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# 定義貪食蛇和食物的位置
global food_x, food_y, snake_x, snake_y, snake_size

snake_x = [32, 32, 32]
snake_y = [32, 34, 36]
food_x = random.randint(10, oled_width-10)
food_y = random.randint(10, oled_height-10)
if food_x % 2 != 0 : food_x = food_x + 1
if food_y % 2 != 0 : food_y = food_y + 1
snake_size = 3

# 定義顏色
BLACK = 0
WHITE = 1

# 定義方向變量
direction = 0  # 0 = up, 1 = right, 2 = down, 3 = left

# 定義將像素繪制到屏幕上的函數
def draw_pixel(x, y, color):
    oled.pixel(x, y, color)

# 定義檢查貪食蛇是否吃到食物的函數
def check_food():
    global food_x,food_y,snake_x,snake_y,snake_size
    if snake_x[0] == food_x and snake_y[0] == food_y:
        food_x = random.randint(10, oled_width-10)
        food_y = random.randint(10, oled_height-10)
        if food_x % 2 != 0 : food_x = food_x+1
        if food_y % 2 != 0 : food_y = food_y+1
        snake_x.append(snake_x[-1] + 2)
        snake_y.append(snake_y[-1] + 2)
        snake_size += 1

# 定義更新貪食蛇位置的函數
def update_snake():
    global snake_x,snake_y,snake_size,direction
    print(direction)
    
    for i in range(snake_size-1, 0, -1):
        snake_x[i] = snake_x[i-1]
        snake_y[i] = snake_y[i-1]
    if direction == 0:
        snake_y[0] += 2
    elif direction == 1:
        snake_y[0] -= 2
    elif direction == 2:
        snake_x[0] -= 2    
    elif direction == 3:
        snake_x[0] += 2
   

# 定義檢查貪食蛇是否碰到邊緣的函數
def check_border():
    global snake_x,snake_y
    if snake_x[0] < 0:
        snake_x[0] = oled_width-2
    elif snake_x[0] > oled_width-2:
        snake_x[0] = 0
    if snake_y[0] < 0:
        snake_y[0] = oled_height-2
    elif snake_y[0] > oled_height-2:
        snake_y[0] = 0

#定義檢查貪食蛇是否碰到自己的函數
def check_self():
    global snake_x,snake_y,snake_size
    for i in range(1, snake_size):
        if snake_x[0] == snake_x[i] and snake_y[0] == snake_y[i]:
            print(snake_y)
            return True
    return False

#定義繪製遊戲界面的函數
def draw_game():
    # 清空屏幕
    oled.fill(BLACK)
    # 繪製貪食蛇
    for i in range(snake_size):
#         print ('snake_size',snake_size)
        draw_pixel(snake_x[i], snake_y[i], WHITE)

    # 繪製食物
    draw_pixel(food_x, food_y, WHITE)

    # 更新屏幕顯示
    oled.show()

#主循環
while True:
    # 讀取搖桿和按鈕的值
    read_x = j_x.read_u16()
    read_y = j_y.read_u16()
    button = sw.value()
    # 檢查搖桿的方向
    if read_y > 55000:
        direction = 0
#         print ('p')
#         print('{}{:5}{}{:5}'.format('X =',read_x,' Y =',read_y))
    elif read_y < 15000:
        direction = 1
#         print ('d')
#         print('{}{:5}{}{:5}'.format('X =',read_x,' Y =',read_y))
    elif read_x < 15000:
        direction = 3
#         print ('l')
#         print('{}{:5}{}{:5}'.format('X =',read_x,' Y =',read_y))
    elif read_x > 55000:
        direction = 2
#         print ('r')
#         print('{}{:5}{}{:5}'.format('X =',read_x,' Y =',read_y))

    # 更新貪食蛇位置
    update_snake()

    # 檢查貪食蛇是否吃到食物
    check_food()

    # 檢查貪食蛇是否碰到邊緣或自己
    if check_self():
        # 當貪食蛇碰到邊緣或自己時，重新開始遊戲
        snake_x = [32, 32, 32]
        snake_y = [32, 34, 36]
        food_x = random.randint(0, oled_width-1)
        food_y = random.randint(0, oled_height-1)
        snake_size = 3
        direction = 0

    # 檢查貪食蛇是否碰到邊緣
    check_border()

    # 繪製遊戲界面
    draw_game()

    # 控制遊戲速度
    time.sleep(0.1)