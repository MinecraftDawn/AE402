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


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, r, color):
        super().__init__()
        self.image = pygame.Surface([r*2, r*2])
        pygame.draw.circle(self.image, color, (r,r), r, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#        self.rect.center = (x,y)
        

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

allSprits = pygame.sprite.Group()
blocks = pygame.sprite.Group()

for i in range(10):
    for j in range(3):
        w = size[0] / 10
        
        if (i+j) % 2 == 0:
            color = RED
        else:
            color = WHITE
        
        block = Block(color, w, 50)
        block.rect.x = i * 70
        block.rect.y = j * 50
        
        blocks.add(block)
        allSprits.add(block)

player = Block(WHITE, 50, 50)
allSprits.add(player)

ball = Ball(0, 300,300 , 30, WHITE)
allSprits.add(ball)
# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    # --- 程式的運算與邏輯
    

    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)

    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    hits = pygame.sprite.spritecollide(player, blocks, True)
    if hits:
        print("增加" + str(len(hits)) + "分")

    allSprits.draw(screen)
    
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(60)

# 關閉式窗並離開程式
pygame.quit()
exit()


