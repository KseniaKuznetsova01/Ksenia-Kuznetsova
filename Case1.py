# Case1
# Developers: Kuznetsova K. (50%), Panukova E. (60%)
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


if __name__ == '__main__': #Вызываю функцию main
    main()
