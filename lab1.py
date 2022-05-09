from pygame import *

win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#задаем цвет согласно цветовой схеме RGB
run = True
while run:
    time.delay(50)
    window.fill(back)#закрашиваем окно цветом
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()