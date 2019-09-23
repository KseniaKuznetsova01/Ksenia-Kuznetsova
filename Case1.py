# Case1
# Developers: Kuznetsova K. (50%), Panukova E. (60%)
import turtle
from turtle import *
import math



def triangle(x, y, a, b, c, r1, r2,color):  # Объявляем функцию triangle с входными параметрами: стартовая позиция, длины сторон, углы и цвет (Екатерина)
    turtle.up() #Поднимаю перо
    turtle.setposition(x, y) #Занимаем стартовую позицию
    turtle.down()  #Опускаю перо
    turtle.color(color) #Цвет
    turtle.begin_fill()#Начинаем заливку цветом
    turtle.forward(a)  #Движение вперед
    turtle.right(r1)#Поворот направо
    turtle.forward(b) #Движение вперед
    turtle.right(r2)#Поворот направо
    turtle.forward(c) #Движение вперед
    turtle.end_fill()

def parallelogram (x, y, a, b, c, d, r1, r2, r3, color) : #Объявляем функцию parallelogram с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up() #Поднимаю перо
    turtle.setposition(x,y) #Занимаем стартовую позицию
    turtle.down() #Опускаю перо
    turtle.color(color) #Цвет
    turtle.begin_fill() #Начинаем заливку цветом
    turtle.forward(a) #Движение вперед
    turtle.right(r1) #Поворот направо
    turtle.forward(b) #Движение вперед
    turtle.right(r2) #Поворот направо
    turtle.forward(c)  #Движение вперед
    turtle.right(r3) #Поворот направо
    turtle.forward(d) #Движение вперед
    turtle.end_fill() #Заканчиваем заливку цветом

def square (x, y, a, b, c, d, r1, r2, r3, color) : #Объявляем функцию square с входными параметрами: стартовая позиция, длины сторон, углы и цвет
    turtle.up() #Поднимаю перо
    turtle.setposition(x,y)
    turtle.down() #Опускаю перо
    turtle.color(color) #Цвет
    turtle.begin_fill() #Начинаем заливку цветом
    turtle.forward(a) #Движение вперед
    turtle.right(r1) #Поворот направо
    turtle.forward(b) #Движение вперед
    turtle.right(r2) #Поворот направо
    turtle.forward(c) #Движение вперед
    turtle.right(r3) #Поворот направо
    turtle.forward(d) #Движение вперед
    turtle.end_fill() #Заканчиваем заливку цветом

def main():
    # Picture_1:man (Екатерина)
    turtle.right(-135)
    square(0, -2, 50, 50, 50, 50, 90, 90, 90, 'orange')
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

    # Picture_2:Rabbit (Екатерина)
    turtle.right(45)
    triangle(200, -50, 100, 100, 142, -90, -135, 'blue')
    turtle.right(-135)
    triangle(304, -50, 70, 99, 70, -135, -135, 'purple')
    turtle.right(-135)
    triangle(200, -43, 180, 130, 132, -135, -90, 'yellow')
    turtle.right(0)
    triangle(331, 104, 71, 50, 50, -135, -90, 'pink')
    turtle.right(45)
    triangle(326, 87, 128, 180, 128, -135, -135, 'red')
    turtle.right(-90)
    square(330, 205, 60, 60, 60, 60, 90, 90, 90, 'orange')
    turtle.right(45)
    parallelogram(360, 269, 71, 50, 71, 50, -45, -135, -45, 'green')

    # Picture_3:Box (Екатерина)
    turtle.right(-90)
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

    # Picture_4:Whale (Екатерина)
    turtle.right(-45)
    triangle(3, 120, 142, 100, 100, 135, 90, 'red')
    turtle.right(135)
    triangle(-2, 120, 142, 100, 100, -135, -90, 'yellow')
    turtle.right(180)
    triangle(-116, 156, 50, 70, 50, 135, 135, 'pink')
    turtle.right(-90)
    triangle(-78, 190, 50, 70, 50, 135, 135, 'purple')
    turtle.right(-45)
    triangle(-180, 170, 71, 50, 50, 135, 90, 'orange')
    turtle.right(135)
    triangle(-180, 170, 71, 50, 50, -135, -90, 'orange')
    turtle.right(-90)
    triangle(-105, 267, 71, 71, 100, 90, 135, 'blue')
    turtle.right(180)
    triangle(40, 302, 71, 50, 50, 135, 90, 'green')
    turtle.right(180)
    triangle(40, 302, 50, 71, 50, 135, 135, 'green')

    # Picture_5:Fish (Ksenia)
    turtle.right(0)
    triangle(-565, -190, 100, 100, 142, -90, -135, 'yellow')
    turtle.right(135)
    triangle(-465, -88, 100, 100, 142, -90, -135, 'red')
    turtle.right(-90)
    triangle(-464, -124, 50, 50, 71, -90, -135, 'blue')
    turtle.right(45)
    square(-466, -89, 41, 41, 41, 41, -90, -90, -90, 'orange')
    turtle.right(-90)
    parallelogram(-524, -89, 41, 29, 41, 29, -45, -135, -45, 'green')
    turtle.right(180)
    triangle(-524, -90, 29, 29, 41, -90, -135, 'pink')
    turtle.right(0)
    triangle(-583, -20, 41, 29, 29, 135, 90, 'purple')

    # Picture_6:Men2(Ksenia)
    turtle.right(-45)
    square(600, 1200, 71, 71, 71, 71, -90, -90, -90, 'orange' )
    turtle.right(135)
    triangle(550, 1098, 128, 180, 128, 135, 135, 'red')
    turtle.right(180)
    parallelogram(549, 1098, 50, 71, 50, 71, 45, 135, 45, 'green')
    turtle.right(135)
    triangle(570, 990, 128, 128, 180, 90, 135, 'yellow')
    turtle.right(-135)
    triangle(450, 870, 50, 50, 71, -90, -135, 'pink')
    turtle.right(135)
    triangle(572, 860, 100, 71, 71, -135, -90, 'blue')
    turtle.right(-90)
    triangle(570, 810, 50, 50, 71, -90, -135, 'purple' )

    # Picture_7:Ship(Ksenia)
    turtle.right(-45)
    parallelogram(30, 900, 50, 30, 50, 30, 135, 45, 135, 'green')
    turtle.right(45)
    triangle(61, 900, 50, 71, 50, 135, 135, 'blue')
    turtle.right(135)
    triangle(61, 936, 180, 128, 128, 135, 90, 'red')
    turtle.right(180)
    triangle(61, 935, 63, 63, 90, 90, 135, 'pink')
    turtle.right(45)
    square(151, 936, 63, 63, 63, 63, 90, 90, 90, 'orange')
    turtle.right(0)
    triangle(59, 1066, 100, 71, 71, -135, -90, 'yellow')
    turtle.right(0)
    triangle(61, 1117, 63, 90, 63, 135, 135, 'purple')

    # Picture_8:Lama(Ksenia)
    turtle.right(135)
    triangle(-500, 1130, 91, 91, 128, 90, 135, 'blue')
    turtle.right(-90)
    parallelogram(-500, 1129, 128, 70, 128, 70, -45, -135, -45, 'green')
    turtle.right(180)
    triangle(-499, 1129, 180, 128, 128, -135, -90, 'red')
    turtle.right(90)
    triangle(-371, 912, 128, 128, 180, 90, 135, 'yellow')
    turtle.right(135)
    triangle(-299, 912, 71, 50, 71, -135, -90, 'purple')
    turtle.right(-135)
    square(-243, 1041, 60, 60, 60, 60, -90, -90, -90, 'orange')
    turtle.right(0)
    triangle(-303, 1042, 71, 50, 50, -135, -90, 'pink')

if __name__ == '__main__':
   main()
