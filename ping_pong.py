#Создай собственный Шутер!
from pygame import *


#класс родитель для спрайтов
class GameSprite(sprite.Sprite):
    #коструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт далжен хранить свойство rect - прямоугольник, в который внисан спрайт
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс игрока    
class Player(GameSprite):
    #метод управление с клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 150:
            self.rect.y += self.speed

#Игровая сцена
back = (200, 255, 255) #фон
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#флаги, отвечающие за состояние изры
run = True
finish = False
clock = time.Clock()
FPS = 60
#создание ракетки
racket1 = Player('racket.png', 10, 200, 50, 150, 4)
racket2 = Player('racket.png', 540, 200, 50, 150, 4)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()

    display.update()
    clock.tick(FPS)
  
