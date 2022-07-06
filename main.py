
import time

import pygame
from pygame.locals import *
import random

class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/pedestrian-man (1).png")
        self.x = 700
        self.y = 600

    def move_left(self):
        self.x -= 150


    def move_right(self):
        self.x += 150


    def move_up(self):
        self.y -= 0


    def move_down(self):
        self.y += 0


    def draw(self):


        if self.x >= 1000:
            self.x = 1000
        if self.x <= 400:
            self.x = 400

        if self.y >= 600:
            self.y = 600
        if self.y <= 500:
            self.y = 500
        self.parent_screen.blit(self.block, (self.x, self.y))

    def isCollide(self,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,enspx,enspy):


        if self.x == 400:
            if (self.y <= y1+80 and self.y>=y1+10) or (self.y <= y6+80 and self.y>=y6+10):
                # print("collide1")
                return True
        if self.x == 550:
            if (self.y <= y2+80 and self.y>=y2+10) or (self.y <= y7+80 and self.y>=y7+10):
                # print("collide2")
                return True
        if self.x == 700:
            if (self.y <= y3+80 and self.y>=y3+10) or (self.y <= y8+80 and self.y>=y8+10):
                # print("collide3")
                return True
        if self.x == 850:
            if (self.y <= y4+80 and self.y>=y4+10) or (self.y <= y9+80 and self.y>=y9+10):
                # print("collide4")
                return True
        if self.x == 1000:
            if (self.y <= y5+80 and self.y>=y5+10) or (self.y <= y10+80 and self.y>=y10+10):
                # print("collide5")
                return True
        if self.x == enspx:
            if self.y <= enspy+80 and self.y >= enspy+10 :
                return True

        return False


class Game:




    game_over = True
    score_value = 0
    x = 0
    background = pygame.image.load("resources/desert1 (1).jpg")

    enemy1 = pygame.image.load("resources/fire.png")
    enemy2 = pygame.image.load("resources/satellite.png")
    enemy3 = pygame.image.load("resources/fire.png")
    enemy4 = pygame.image.load("resources/satellite.png")

    enemy5 = pygame.image.load("resources/fire.png")
    enemy6 = pygame.image.load("resources/satellite.png")
    enemy7 = pygame.image.load("resources/fire.png")
    enemy8 = pygame.image.load("resources/satellite.png")

    enemy9 = pygame.image.load("resources/fire.png")
    enemy10 = pygame.image.load("resources/satellite.png")

    ensp = pygame.image.load("resources/comet.png")

    belt = pygame.image.load("resources/belt (1).png")



    en1x = 400-40
    en2x = 550-40
    en3x = 700-40
    en4x = 850-40
    en5x = 1000-40

    en6x = 400-40
    en7x = 550-40
    en8x = 700-40
    en9x = 850-40
    en10x = 1000-40

    en1y = random.randint(-80, -60)
    en2y = random.randint(-230, -220)
    en3y = random.randint(-50, -30)
    en4y = random.randint(-180, -170)
    en5y = random.randint(-50, -30)

    en6y = random.randint(-600, -590)
    en7y = random.randint(-450, -430)
    en8y = random.randint(-600, -590)
    en9y = random.randint(-700, -650)
    en10y = random.randint(-500, -450)

    enspx = random.randrange(100,400,150)
    enspy = random.randint(-3000,-2000)

    belty = 0

    incvalue = 0.01
    # score = pygame.font.render("Score : " + str(score_value // 100), True, (0, 10, 20))


    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1400, 800))
        self.surface.blit(self.background,(0,0))
        self.snake = Snake(self.surface)



        # self.en1x = 400 - 40
        # self.en2x = 550 - 40
        # self.en3x = 700 - 40
        # self.en4x = 850 - 40
        # self.en5x = 1000 - 40
        #
        # self.en6x = 400 - 40
        # self.en7x = 550 - 40
        # self.en8x = 700 - 40
        # self.en9x = 850 - 40
        # self.en10x = 1000 - 40
        #
        # self.en1y = random.randint(-80, -60)
        # self.en2y = random.randint(-230, -220)
        # self.en3y = random.randint(-50, -30)
        # self.en4y = random.randint(-180, -170)
        # self.en5y = random.randint(-50, -30)
        #
        # self.en6y = random.randint(-600, -590)
        # self.en7y = random.randint(-450, -430)
        # self.en8y = random.randint(-600, -590)
        # self.en9y = random.randint(-700, -650)
        # self.en10y = random.randint(-500, -450)
        #
        # self.incvalue = 0.01

    def game_over(self):

        game = Game()
        self.surface.blit(self.background,(-50,0))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        line1 = font.render(f"Game is over! Your score is {self.score_value//10}", True, (255, 255, 255))
        line2 = font.render(f"Hit Enter to restart", True, (255, 255, 255))
        self.surface.blit(line1, (500, 350))
        self.surface.blit(line2, (570, 400))
        # loop_var = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit(0)
                    return True
                if event.key == K_RETURN:
                    # print("bnm")
                    game.run()
                    # print("bnm")
                    return True
            if event.type == QUIT:
                exit(0)
        return True


    def run(self):
        running = True
        loop_var = False
        collision = False
        pause = False
        flg = 1
        self.surface.blit(self.background, (-50, 0))
        # font = pygame.font.SysFont('arial', 30)
        # line1 = font.render(f" 3 ", True, (255, 255, 255))
        # line2 = font.render(f" 3 ", True, (255, 255, 255))
        # line3 = font.render(f" 3 ", True, (255, 255, 255))
        #
        # self.surface.blit(line1, (200, 300))
        # time.sleep(1000)
        # self.surface.blit(line2, (200,300))
        # time.sleep(1000)
        # self.surface.blit(line3, (200, 300))
        pygame.display.update()
        while running:
            # if loop_var == False:
            #     self.collision = self.snake.isCollide(self.en1y, self.en2y, self.en3y, self.en4y, self.en5y, self.en6y,
            #                                 self.en7y, self.en8y, self.en9y, self.en10y)
            #
            # if self.collision:
            #     var = self.game_over()
            #     print(var)
            #     # print(self.en1y,self.en2y,self.en3y,self.en4y,self.en5y,self.en6y,self.en7y,self.en8y,self.en9y,self.en10y)
            #     # print(self.snake.isCollide(self.en1y,self.en2y,self.en3y,self.en4y,self.en5y,self.en6y,self.en7y,self.en8y,self.en9y,self.en10y))
            #     if var:
            #         self.loop_var = True

            if self.snake.isCollide(self.en1y, self.en2y, self.en3y, self.en4y, self.en5y, self.en6y,
                                             self.en7y, self.en8y, self.en9y, self.en10y, self.x , self.enspy):

                self.game_over()

                # running = False


            else:

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False

                        if event.key == K_LEFT and pause == False:

                            self.snake.move_left()

                        if event.key == K_RIGHT and pause == False:
                            self.snake.move_right()

                        if event.key == K_UP and pause == False:
                            self.snake.move_up()

                        if event.key == K_DOWN and pause == False:
                            self.snake.move_down()

                        if event.key == K_SPACE:

                            if flg == 1:
                                flg = 0
                                print("bnm")
                                pause = True
                            else:
                                flg = 1
                                pause = False

                    elif event.type == QUIT:
                        running = False

                if pause:
                    self.en1y += 0
                    self.en2y += 0
                    self.en3y += 0
                    self.en4y += 0
                    self.en5y += 0
                    self.en6y += 0
                    self.en7y += 0
                    self.en8y += 0
                    self.en9y += 0
                    self.en10y += 0
                    self.enspy += 0
                    self.belty += 0
                    self.score_value += 0


                else:
                    self.en1y += 1.5*3 + self.incvalue
                    self.en2y += 1.5*3 + self.incvalue
                    self.en3y += 1.5*3 + self.incvalue
                    self.en4y += 1.5*3 + self.incvalue
                    self.en5y += 1.5*3 + self.incvalue
                    self.en6y += 1.5*3 + self.incvalue
                    self.en7y += 1.5*3 + self.incvalue
                    self.en8y += 1.5*3 + self.incvalue
                    self.en9y += 1.5*3 + self.incvalue
                    self.en10y += 1.5*3 + self.incvalue
                    self.enspy += 5*3 + self.incvalue
                    self.belty +=1.5*3 + self.incvalue

                    self.score_value += 1





                self.incvalue += 0.0001
                if self.en1y >= 800:
                    self.en1y = random.randint(-80, -60)
                if self.en2y >= 800:
                    self.en2y = random.randint(-230, -220)
                if self.en3y >= 800:
                    self.en3y = random.randint(-50, -30)
                if self.en4y >= 800:
                    self.en4y = random.randint(-180, -170)
                if self.en5y >= 800:
                    self.en5y = random.randint(-50, -30)
                if self.en6y >= 800:
                    self.en6y = random.randint(-600, -590)
                if self.en7y >= 800:
                    self.en7y = random.randint(-450, -430)
                if self.en8y >= 800:
                    self.en8y = random.randint(-600, -590)
                if self.en9y >= 800:
                    self.en9y = random.randint(-700, -650)
                if self.en10y >= 800:
                    self.en10y = random.randint(-500, -450)
                if self.belty >= 800:
                    self.belty = 0

                if self.enspy >= 800:
                    self.enspy = random.randint(-10000, -7000)

                self.surface.blit(self.background, (-50, 0))
                self.snake.draw()
                self.surface.blit(self.enemy1, (self.en1x, self.en1y))
                self.surface.blit(self.enemy2, (self.en2x, self.en2y))
                self.surface.blit(self.enemy3, (self.en3x, self.en3y))
                self.surface.blit(self.enemy4, (self.en4x, self.en4y))
                self.surface.blit(self.enemy5, (self.en5x, self.en5y))
                self.surface.blit(self.enemy6, (self.en6x, self.en6y))
                self.surface.blit(self.enemy7, (self.en7x, self.en7y))
                self.surface.blit(self.enemy8, (self.en8x, self.en8y))
                self.surface.blit(self.enemy9, (self.en9x, self.en9y))
                self.surface.blit(self.enemy10, (self.en10x, self.en10y))

                if self.enspy <= 0 :
                    self.x = self.snake.x
                else:
                    pass
                self.surface.blit(self.ensp, (self.x,self.enspy))



                font = pygame.font.SysFont('Comic Sans MS', 30)
                line1 = font.render(f"Your score  {self.score_value // 10}", True, (255, 255, 255))
                line2 = font.render(f"Space Survival", True, (255, 255, 255))
                self.surface.blit(self.belt, (-50, self.belty))
                self.surface.blit(self.belt, (-50,self.belty-382))
                self.surface.blit(self.belt, (-50, self.belty - 764))
                self.surface.blit(self.belt, (-50, self.belty - 1146))
                self.surface.blit(self.belt, (-50, self.belty - 1528))
                self.surface.blit(self.belt, (1050, self.belty))
                self.surface.blit(self.belt, (1050, self.belty - 382))
                self.surface.blit(self.belt, (1050, self.belty - 764))
                self.surface.blit(self.belt, (1050, self.belty - 1146))
                self.surface.blit(self.belt, (1050, self.belty - 1528))
                self.surface.blit(line1, (10, 10))
                self.surface.blit(line2, (1170, 10))


            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

