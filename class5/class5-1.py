"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame
import random

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
score = 0
boxes = []
for _ in range(10):
    x = random.randrange(size[0])
    y = random.randrange(size[1])
    boxes.append([x,y,True])

# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束
    # --- 程式的運算與邏輯
    
    pygame.display.set_caption("目前分數" + str(score))
    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)
    x1,y1 = pygame.mouse.get_pos()
    
    for i in range(len(boxes)):
        x = boxes[i][0]
        y = boxes[i][1]
        if (x <= x1+32 <= x+32 or x <= x1 <= x+32) and \
        (y <= y1+32 <= y+32 or y <= y1 <= y+32):
            if boxes[i][2]:
                score += 1
                if score == 10:
                    done = True
            boxes[i][2] = False
    
    pygame.draw.rect(screen, WHITE, [x1,y1,32,32])
    
    for i in range(len(boxes)):
        x,y,draw = boxes[i]
        if draw:
            pygame.draw.rect(screen, WHITE, [x,y,32,32])
    
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(60)

# 關閉式窗並離開程式
pygame.quit()
exit()


