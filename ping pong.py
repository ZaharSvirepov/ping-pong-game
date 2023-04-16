from pygame import *
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
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < 450:
                self.rect.y += self.speed
        if self == racket1:
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 450:
                self.rect.y += self.speed


#* Окно игры и фон / Game window and background
window = display.set_mode((800, 600))
display.set_caption('Ping pong')
background = transform.scale(image.load("background.png"), (800, 600))

racket1 = Player(('player image.png'), 10, 250, 30, 150, 5)
racket2 = Player(('player image.png'), 760, 250, 30, 150, 5)
game = True

#? Игровой цикл / Game loop
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    racket1.update()
    racket2.update()

    racket1.reset()
    racket2.reset()
    display.update()
