from pygame import *

win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#задаем цвет согласно цветовой схеме RGB

class GameSprite(sprite.Sprite):
   # конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y):
       # Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))  
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   # метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))




packman  = GameSprite("hero.png",100,300,80,80)
w1 = GameSprite('platform2.png',100, 250, 300, 50)
w2 = GameSprite('platform2_v.png', 370, 100, 50, 400)
run = True

while run:
    time.delay(50)
    window.fill(back)#закрашиваем окно цветом
    for e in event.get():
        if e.type == QUIT:
            run = False
    #рисуем объекты
    w1.reset()
    w2.reset()
    packman.reset()
     
    display.update()