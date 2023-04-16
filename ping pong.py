from pygame import *
from time import *
#! Класс GameSprite 
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #?вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #*каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #*каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #?метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #*метод для управления спрайтом стрелками клавиатуры
    def update(self):
        if self == racket2:
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 1:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.speed
        if self == racket1:
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 1:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 400:
                self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        global diffel_y
        global deer
        self.rect.x += diffel_x * self.speed
        self.rect.y += diffel_y * self.speed
        if self.rect.y == 0:
            diffel_y = 1
        elif self.rect.y == 550:
            diffel_y = -1

        if self.rect.x <= -50 or self.rect.x >= 800:
            if self.rect.x <= 0:
                global deer
                deer = 2
                global finish
                finish = True
            else:
                deer = 1
                finish = True

#* Окно игры и фон / Game window and background
window = display.set_mode((800, 600))
display.set_caption('Ping pong')
background = transform.scale(image.load("background.png"), (800, 600))
font.init()
font = font.SysFont('Arial', 70)
text2 = font.render('Игрок 1 победил', True, (255, 255, 255))
text3 = font.render('Игрок 2 победил', True, (255, 255, 255))

ball = Ball(('ball.png'), 350, 250, 50, 50, 2)
racket1 = Player(('player image.png'), 60, 200, 30, 200, 5)
racket2 = Player(('player image.png'), 710, 200, 30, 200, 5)
game = True
finish = False
diffel_x = 1
diffel_y = 1
deer = 0
#? Игровой цикл / Game loop
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if finish != True:
        window.blit(background, (0, 0))  
        racket1.update()
        racket2.update()
        ball.update()
        if sprite.collide_rect(racket1, ball):
            diffel_x = 1
        elif sprite.collide_rect(racket2, ball):
            diffel_x = -1
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()

    if deer == 1:           
        window.blit(text2, (200, 270))  
        display.update()       
    elif deer == 2:
        window.blit(text3, (200, 270))
        display.update()
