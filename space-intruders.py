# Space intruders

import turtle
import os 
import random
import math

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Space Inturders by Cody Snell")
wn.bgpic("galactic.gif")
wn.setup(width=800, height=600)

wn.register_shape("bomber.gif")
wn.register_shape("intruder.gif")

#  draw border
# border_pen = turtle.Turtle()
# border_pen.speed(0)
# border_pen.color("black")
# border_pen.penup()
# border_pen.setposition(-300,-300)
# border_pen.pensize(3)
# border_pen.pendown()
# for side in range(4):
#     border_pen.fd(600)
#     border_pen.lt(90)
# border_pen.hideturtle()

#  set score

score = 0

pen =turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.setposition(-290,280)
font = ("Arial", 14, "bold")
pen.write("Score: {}".format(score), align="left", font=font)
pen.hideturtle()
# create player turtle

player = turtle.Turtle()
player.color("blue")
player.shape("bomber.gif")
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
bullet.setposition(0, -400)
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
for _ in range(5):
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("intruder.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)
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
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1


        if isCollision(bullet, enemy):
            os.system("afplay 8b-explo.wav&")
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            score += 100
            pen.clear()
            pen.write("Score: {}".format(score), align="left", font=font)
            # reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            
        if isCollision(player, enemy):
            os.system("afplay 8b-destroy.wav&")
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()
            print('Game over')
            break
    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

# check if bullet hits border

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



wn.mainloop()