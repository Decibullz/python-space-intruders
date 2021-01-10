# Space intruders

import turtle
import os 
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Inturders by Cody Snell")

#  draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create player turtle

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-280)
player.setheading(90)

playerspeed = 15

#  create bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#  bullet state
# ready to fire
bulletstate = "ready"
# firing


# create enemy
enemies = []
for _ in range(1):
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200,250)
    enemies.append(enemy)
    enemyspeed = 8





# functions
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # changes global state to match that within function
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay pew.wav&")
        bulletstate = "fire"
        # move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()  

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

wn.listen()

wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")


while True: 
    wn.update()
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)
        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)
    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

# check if bullet hits border

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

#  check for a collision of bullet & enemy
    if isCollision(bullet, enemy):
        os.system("afplay 8b-explo.wav&")
        # reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # reset the enemy
        enemy.setposition(-200,250)
        
    if isCollision(player, enemy):
        os.system("afplay 8b-destroy.wav&")
        player.hideturtle()
        enemy.hideturtle()
        print('Game over')
        break


wn.mainloop()