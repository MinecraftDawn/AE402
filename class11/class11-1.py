"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame
from snake import Snake, Food
import random
import time
# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()

snake = Snake(5, size)

foodGroup = pygame.sprite.Group()

def addFood():
    x = random.randrange(size[0])
    y = random.randrange(size[1])
    x -= x % 20
    y -= y % 20
    food = Food(WHITE, x, y)
    foodGroup.add(food)
    
for _ in range(10):
    addFood()
    
# 判斷遊戲是否開始(玩家有沒有按下按鍵)
start = False

# 產生文字物件，當作標題/結尾使用
font = pygame.font.Font(None, 50)


# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    # --- 程式的運算與邏輯
    pressed = pygame.key.get_pressed()
    
    # 若遊戲還沒開始 等待按鍵按下才開始遊戲
    if pressed.count(1) == 0 and not start:
        
        pygame.display.flip()
        continue
    else:
        start = True
    
    
    snake.move(pressed)
    
    if snake.isOutOfRange() or snake.collideSelf():
        done = True
        
        text = font.render("you loss", True, WHITE)

        screen.fill(BLACK)
        screen.blit(text, (10,10))
        pygame.display.flip()
        time.sleep(3)
        continue
        
        
    if len(foodGroup) < 10:
        addFood()
    
    snake.有沒有吃到食物(foodGroup)

    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)
    snake.group.draw(screen)
    foodGroup.draw(screen)
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘5個frame
    clock.tick(5)

# 關閉式窗並離開程式
pygame.quit()



