# Case1
# Developers: Kuznetsova K. (50%), Panukova E. (60%)
import turtle

def parallelogram (x, y, a, b, c, d, r1, r2, r3,color)
# TODO:(Ksysha)
pass
def square (x, y, a, b, c, d, r1, r2, r3,color)
# TODO:(Ksusha)
pass
def triangle_0 (x, y, a, b, c, r1, r2,color)
# TODO:(Kate)
pass
def triangle_1 (x, y, a, b, c, r1, r2,color)
#TODO:(Kate)
pass
def triangle_2 (x, y, a, b, c, r1, r2,color)
# TODO:(Kate)
pass
def triangle_3 (x, y, a, b, c, r1, r2,color)
# TODO:(Kate)
pass
def triangle_4  (x, y, a, b, c, r1, r2,color)
# TODO:(Ksusha)
pass
def main():

import turtle

# Case1
# Developers: Kuznetsova K. (o%), Panukova E. (0%)
import turtle
def triangle(x, y, a, b, c, r1, r2,color): #Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up() #Поднимаю перо
    turtle.setposition(x, y)
    turtle.down() #Опускаю перо
    turtle.color(color) #Цвет
    turtle.begin_fill() #Начинаем заливку цветом
    turtle.forward(a) #Движение вперед
    turtle.right(r1) #Поворот напрво
    turtle.forward(b)
    turtle.right(r2)
    turtle.forward(c)
    turtle.end_fill() #Заканчиваем заливку цветом

def main(): #Объявляю функцию main
    triangle(0, 0, 100, 100, 142, -90, -135, 'blue') #Вводим параметры желаемого треугольника
    turtle.right(-135) #Вводим градус, на который необходимо развернуть перо
    triangle(105, 0, 70, 99, 70, -135, -135, 'purple')
    turtle.right(-135)
    triangle(0, 7, 180, 130, 137, -135, -90, 'yellow')
    turtle.right(0)
    triangle(130, 150, 50, 40, 40, -135, -90, 'pink')
    turtle.right(45)
    triangle(130, 150, 152, 200, 130, 45, 90, 'red')

def square  (x, y, a, b, c, d, r1, r2, r3, color) : #Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up()    #Поднимаю перо
    turtle.setposition(x,y)
    turtle.down() #Опускаю перо
    turtle.color(color) #Цвет
    turtle.begin_fill() #Начинаем заливку цветом
    turtle.forwar(a) #Движение вперед
    turtle.right(r1) #Поворот направо
    turtle.forward(b)
    turtle.right(r2)
    turtle.forward(c)
    turtle.right(r3)
    turtle.forward(d)
    tertle.end_fill() #Заканчиваем заливку цветом

def main():
    turtle.right(-135)
    square(265, 132, 50, 50, 50, 50, -90, -90, -90,'orange' )


def parallelogram  (x, y, a, b, c, d, r1, r2, r3, color) : #Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up()    #Поднимаю перо
    turtle.setposition(x,y)
    turtle.down() #Опускаю перо
    turtle.color(color) #Цвет
    turtle.begin_fill() #Начинаем заливку цветом
    turtle.forwar(a) #Движение вперед
    turtle.right(r1) #Поворот направо
    turtle.forward(b)
    turtle.right(r2)
    turtle.forward(c)
    turtle.right(r3)
    turtle.forward(d)
    tertle.end_fill() #Заканчиваем заливку цветом

def main():
    turtle.right(90)
    parallelogram(155, 317, 50, 80, 50, 80, -45, -135, -45, 'green')

if __name__ == '__main__': #Вызываю функцию main
    main()
