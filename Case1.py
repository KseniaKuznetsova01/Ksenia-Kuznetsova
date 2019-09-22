# Case1
# Developers: Kuznetsova K. (50%), Panukova E. (60%)
import turtle

def parallelogram (x, y, a, b, c, d, r1, r2, r3,color)
# TODO:(Ksusha)
pass
def square (x, y, a, b, c, d, r1, r2, r3,color)
# TODO:(Ksusha)
pass
def triangle (x, y, a, b, c, r1, r2,color)
# TODO:(Kate)
pass
def figure_1
# TODO:(Kate)
pass
def figure_2
# TODO:(Kate)
pass
def figure_3
# TODO:(Kate)
pass
def figure_4
# TODO:(Kate)
pass
def figure_5
# TODO:(Ksusha)
pass
def figure_6
# TODO:(Ksusha)
pass
def figure_7
# TODO:(Ksusha)
pass
def figure_8
# TODO:(Ksusha)
pass
# Case1
# Developers: Kuznetsova K. (o%), Panukova E. (0%)


import turtle


def triangle(x, y, a, b, c, r1, r2,color):  # Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет (Екатерина)
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()  #
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(r1)
    turtle.forward(b)
    turtle.right(r2)
    turtle.forward(c)
    turtle.end_fill()

def parallelogram (x, y, a, b, c, d, r1, r2, r3, color) : #Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up() #Поднимаю перо
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

def square (x, y, a, b, c, d, r1, r2, r3, color) : #Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up() #Поднимаю перо
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
    # Picture:man (Екатерина)
    turtle.right(-135)
    triangle(0, 2, 50, 50, 71, 90, 135, 'orange')
    turtle.right(180)
    triangle(0, 2, 71, 50, 50, 135, 90, 'orange')
    turtle.right(-45)
    triangle(-2, -3, 128, 180, 128, 135, 135, 'red')
    turtle.right(90)
    triangle(2, -3, 128, 180, 128, -135, -135, 'yellow')
    turtle.right(-45)
    triangle(-2, -195, 71, 50, 50, 135, 90, 'green')
    turtle.right(180)
    triangle(-2, -195, 50, 71, 50, 135, 135, 'green')
    turtle.right(0)
    triangle(2, -145, 71, 71, 100, -90, -135, 'blue')
    turtle.right(180)
    triangle(55, -220, 71, 50, 50, -135, -90, 'purple')
    turtle.right(-90)
    triangle(-35, -233, 50, 50, 71, 90, 135, 'pink')

    # Picture:Rabbit (Екатерина)
    turtle.right(45)
    triangle(200, 200, 100, 100, 142, -90, -135, 'blue')
    turtle.right(-135)
    triangle(304, 200, 70, 99, 70, -135, -135, 'purple')
    turtle.right(-135)
    triangle(200, 207, 180, 130, 132, -135, -90, 'yellow')
    turtle.right(0)
    triangle(331, 354, 71, 50, 50, -135, -90, 'pink')
    turtle.right(45)
    triangle(326, 337, 128, 180, 128, -135, -135, 'red')
    turtle.right(-90)
    triangle(330, 455, 60, 60, 85, 90, 135, 'orange')
    turtle.right(-135)
    triangle(330, 455, 60, 60, 85, -90, -135, 'orange')
    turtle.right(45)
    triangle(360, 519, 70, 50, 86, 90, 125, 'green')
    turtle.right(180)
    triangle(290, 519, 86, 70, 50, 145, 90, 'green')

    # Picture:Box (Екатерина)
    turtle.right(180)
    triangle(-401, -309, 142, 100, 100, 135, 90, 'yellow')
    turtle.right(225)
    triangle(-398, -165, 142, 100, 100, 135, 90, 'red')
    turtle.right(-135)
    triangle(-253, -167, 71, 50, 50, 135, 90, 'purple')
    turtle.right(-135)
    triangle(-255, -240, 71, 50, 50, 135, 90, 'orange')
    turtle.right(135)
    triangle(-255, -240, 71, 50, 50, -135, -90, 'orange')
    turtle.right(135)
    triangle(-253, -242, 71, 71, 100, 90, 135, 'blue')
    turtle.right(-135)
    triangle(-327, -312, 71, 50, 50, 135, 90, 'green')
    turtle.right(180)
    triangle(-327, -312, 50, 71, 50, 135, 135, 'green')
    turtle.right(-90)
    triangle(-328, -239, 50, 70, 50, 135, 135, 'pink')

    # Picture:Whale (Екатерина)
    turtle.right(-45)
    triangle(3, 200, 142, 100, 100, 135, 90, 'red')
    turtle.right(135)
    triangle(-2, 200, 142, 100, 100, -135, -90, 'yellow')
    turtle.right(180)
    triangle(-116, 236, 50, 70, 50, 135, 135, 'pink')
    turtle.right(-90)
    triangle(-78, 270, 50, 70, 50, 135, 135, 'purple')
    turtle.right(-45)
    triangle(-180, 250, 71, 50, 50, 135, 90, 'orange')
    turtle.right(135)
    triangle(-180, 250, 71, 50, 50, -135, -90, 'orange')
    turtle.right(-90)
    triangle(-105, 347, 71, 71, 100, 90, 135, 'blue')
    turtle.right(180)
    triangle(40, 382, 71, 50, 50, 135, 90, 'green')
    turtle.right(180)
    triangle(40, 382, 50, 71, 50, 135, 135, 'green')


if __name__ == '__main__':
    main()
