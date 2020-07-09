"""
Developed by Limon250
Date: 09.07.2020
Python version 3.8
"""

import pygame, sys, random
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
pygame.init()
pygame.font.init()

SIZE_BLOCK = 20
FRAME_COLOR = (0, 0, 200)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
HEADER_COLOR = (0, 0, 150)
SNAKE_COLOR = (0, 0, 250)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1
size = (SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS,
        SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS+HEADER_MARGIN)
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)
small_font = pygame.font.SysFont(None, 20)
med_font = pygame.font.SysFont(None, 50)
large_font = pygame.font.SysFont(None, 60)
Tk().wm_withdraw()
click = pygame.mouse.get_pressed()

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])
        
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    click = False
    while True:

        screen.fill((0,0,0))
        draw_text('Main menu', med_font, (255, 255, 255), screen, 150, 20)
 
        mx, my = pygame.mouse.get_pos()  

        bttn1 = pygame.Rect(125, 150, 200, 50)
        bttn2 = pygame.Rect(125, 250, 200, 50)
        bttn3 = pygame.Rect(125, 350, 200, 50)
        if bttn1.collidepoint((mx, my)):
            if click:
                choose_level()
        if bttn2.collidepoint((mx, my)):
            if click:
                options()
        if bttn3.collidepoint((mx, my)):
            if click:
                _quit()

        mouse = pygame.mouse.get_pos()
        #print(mouse)

        if 125+200 > mouse[0] > 125 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(screen, (135, 206, 250), bttn1)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn1)
        if 125+200 > mouse[0] > 125 and 250+50 > mouse[1] > 250:
            pygame.draw.rect(screen, (135, 206, 250), bttn2)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn2)
        if 125+200 > mouse[0] > 125 and 350+50 > mouse[1] > 350:
            pygame.draw.rect(screen, (135, 206, 250), bttn3)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn3)

        draw_text("Play", large_font, (255, 255, 255), screen, 178, 155)
        draw_text("Options", large_font, (255, 255, 255), screen, 145, 255)
        draw_text("Quit", large_font, (255, 255, 255), screen, 178, 355)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        timer.tick(60) 

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Options', med_font, (255, 255, 255), screen, 175, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
                pygame.exit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        timer.tick(60)

def _quit():
    while True:
        s = messagebox.askyesno("Attention", "Are you sure you want to exit?")
        print(s)
        if s == True:
            messagebox.showinfo("Hey", "Hope you liked this game")
            print("exit")
            pygame.exit()
            sys.exit()
        else:
            main_menu()

def choose_level():
    click = False
    while True:

        screen.fill((0, 0, 0))
        draw_text('Choose level', med_font, (255, 255, 255), screen, 125, 20)

        mx, my = pygame.mouse.get_pos()

        bttn1 = pygame.Rect(50, 100, 50, 50)
        bttn2 = pygame.Rect(125, 100, 50, 50)
        bttn3 = pygame.Rect(200, 100, 50, 50)
        bttn4 = pygame.Rect(275, 100, 50, 50)
        bttn5 = pygame.Rect(350, 100, 50, 50)
        bttn6 = pygame.Rect(50, 200, 50, 50)
        bttn7 = pygame.Rect(125, 200, 50, 50)
        bttn8 = pygame.Rect(200, 200, 50, 50)
        bttn9 = pygame.Rect(275, 200, 50, 50)
        bttn10 = pygame.Rect(350, 200, 50, 50)
        bttn11 = pygame.Rect(50, 300, 50, 50)
        bttn12 = pygame.Rect(125, 300, 50, 50)
        bttn13 = pygame.Rect(200, 300, 50, 50)
        bttn14 = pygame.Rect(275, 300, 50, 50)
        bttn15 = pygame.Rect(350, 300, 50, 50)

        bttn_back = pygame.Rect(250, 450, 150, 50)

        if bttn1.collidepoint((mx, my)):
            if click:
                game().lvl_1()
        if bttn2.collidepoint((mx, my)):
            if click:
                game().lvl_2()
        if bttn3.collidepoint((mx, my)):
            if click:
                game().lvl_3()
        if bttn4.collidepoint((mx, my)):
            if click:
                game().lvl_4()
        if bttn5.collidepoint((mx, my)):
            if click:
                game().lvl_5()
        if bttn6.collidepoint((mx, my)):
            if click:
                game().lvl_6()
        if bttn7.collidepoint((mx, my)):
            if click:
                game().lvl_7()
        if bttn8.collidepoint((mx, my)):
            if click:
                game().lvl_8()
        if bttn9.collidepoint((mx, my)):
            if click:
                game().lvl_9()
        if bttn10.collidepoint((mx, my)):
            if click:
                game().lvl_10()
        if bttn11.collidepoint((mx, my)):
            if click:
                game().lvl_11()
        if bttn12.collidepoint((mx, my)):
            if click:
                game().lvl_12()
        if bttn13.collidepoint((mx, my)):
            if click:
                game().lvl_13()
        if bttn14.collidepoint((mx, my)):
            if click:
                game().lvl_14()
        if bttn15.collidepoint((mx, my)):
            if click:
                game().lvl_15()
        if bttn_back.collidepoint((mx, my)):
            if click:
                main_menu()

        mouse = pygame.mouse.get_pos()
        #print(mouse)

        if 50+50 > mouse[0] > 50 and 100+50 > mouse[1] > 100:
            pygame.draw.rect(screen, (35, 206, 250), bttn1)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn1)
        if 125+50 > mouse[0] > 125 and 100+50 > mouse[1] > 100:
            pygame.draw.rect(screen, (35, 206, 250), bttn2)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn2)
        if 200+50 > mouse[0] > 200 and 100+50 > mouse[1] > 100:
            pygame.draw.rect(screen, (35, 206, 250), bttn3)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn3)
        if 275+50 > mouse[0] > 275 and 100+50 > mouse[1] > 100:
            pygame.draw.rect(screen, (35, 206, 250), bttn4)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn4)
        if 350+50 > mouse[0] > 350 and 100+50 > mouse[1] > 100:
            pygame.draw.rect(screen, (35, 206, 250), bttn5)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn5)
        if 50+50 > mouse[0] > 50 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(screen, (35, 206, 250), bttn6)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn6)
        if 125+50 > mouse[0] > 125 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(screen, (35, 206, 250), bttn7)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn7)
        if 200+50 > mouse[0] > 200 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(screen, (35, 206, 250), bttn8)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn8)
        if 275+50 > mouse[0] > 275 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(screen, (35, 206, 250), bttn9)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn9)
        if 350+50 > mouse[0] > 350 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(screen, (35, 206, 250), bttn10)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn10)
        if 50+50 > mouse[0] > 50 and 300+50 > mouse[1] > 300:    
            pygame.draw.rect(screen, (35, 206, 250), bttn11)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn11)
        if 125+50 > mouse[0] > 125 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(screen, (35, 206, 250), bttn12)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn12)
        if 200+50 > mouse[0] > 200 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(screen, (35, 206, 250), bttn13)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn13)
        if 275+50 > mouse[0] > 275 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(screen, (35, 206, 250), bttn14)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn14)
        if 350+50 > mouse[0] > 350 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(screen, (35, 206, 250), bttn15)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn15)
        
        if 250+150 > mouse[0] > 250 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, (35, 206, 250), bttn_back)
        else:
            pygame.draw.rect(screen, (0, 0, 150), bttn_back)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print('quit')
                pygame.exit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        timer.tick(60)

def game():
    class SnakeBlock:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def is_inside(self):
            return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS

        def __eq__(self, other):
            return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS-1)
        y = random.randint(0, COUNT_BLOCKS-1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS-1)
            empty_block.y = random.randint(0, COUNT_BLOCKS-1)
        return empty_block
    snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]
    apple = get_random_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = 1

    def lvl_1():
        pass

    def lvl_2():
        pass

    def lvl_3():
        pass

    def lvl_4():
        pass

    def lvl_5():
        pass

    def lvl_6():
        pass

    def lvl_7():
        pass

    def lvl_8():
        pass

    def lvl_9():
        pass

    def lvl_10():
        pass

    def lvl_11():
        pass

    def lvl_12():
        pass

    def lvl_13():
        pass

    def lvl_14():
        pass

    def lvl_15():
        pass
        
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col!=0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col!=0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row!=0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row!=0:
                    buf_row = 0
                    buf_col = 1
                elif event.key == K_ESCAPE:
                    a = messagebox.askyesno("Attention!", "Are you sure you want to go to main menu?")
                    if a == True:
                        print('go to main menu')
                        running = False
                        main_menu()
                    else:
                        return game()
                    
        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        text_total = courier.render(f"Total: {total}", 0, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK+230, SIZE_BLOCK))

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            messagebox.showinfo('Crash', 'Crash, return to main menu')
            print('crash')
            running = False
            main_menu()
        
        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        pygame.display.flip()

        if apple == head:
            total += 1
            speed = total //5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            messagebox.showinfo('Crash youself', 'Crash yourself, return to main menu')
            print('crash yourself')
            running = False
            main_menu()


        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
        timer.tick(7+speed)

if __name__ == '__main__':
    main_menu()