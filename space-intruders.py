# Space intruders

import turtle
import os 
import random
import math
import platform
import time

# if on windows import windsound
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("winsound module not available")

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Space Intruders by Cody Snell")
wn.bgpic("galactic.gif")
wn.tracer(0)
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
pen.color("red")
pen.speed(0)
pen.penup()
pen.setposition(-290,280)
font = ("Arial", 14, "bold")
pen.write("Score: {}".format(score), align="left", font=font)
pen.hideturtle()
# create player turtle

player = turtle.Turtle()
player.color("black")
player.shape("bomber.gif")
player.penup()
player.speed(0)
player.setposition(0,-280)
player.setheading(90)
player.speed = 0


#  create bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setposition(-500, -500)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 15

#  bullet state
# ready to fire
bulletstate = "ready"
# firing


# create enemy
enemies = []

enemy_start_y = 250
enemy_start_x = -200
enemy_number = 0

for _ in range(30):
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("intruder.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -=50
        enemy_number = 0
    enemies.append(enemy)
    enemyspeed = .7


# functions
def move_left():
    player.speed = -3

def move_right():
    player.speed = 3

def stop_player():
	player.speed = 0

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

def play_sound(sound_file, time = 0):
    # Windows
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # Mac
    else:
        os.system("afplay {}&".format(sound_file))

    # repeat sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t =int(time*1000))

def fire_bullet():
    # changes global state to match that within function
    global bulletstate
    if bulletstate == "ready":
        play_sound("pew.wav")
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
wn.onkeyrelease(stop_player, "Left")
wn.onkeyrelease(stop_player, "Right")
wn.onkeypress(fire_bullet, "space")

# play_sound("bg-sound.wav", 2.6) commentend out sound file plays too loud
while True: 

    wn.update()
    move_player()
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
            play_sound("8b-explo.wav")
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            score += 100
            pen.clear()
            pen.write("Score: {}".format(score), align="left", font=font)
            # reset the enemy
            enemy.setposition(0, 10000)
            enemy.speed = 0

        if isCollision(player, enemy):
            print("1")
            pen.clear()
            pen.setposition(0,0)
            pen.write("GAME OVER Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            pen.setposition(-290,280)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy_start_y = 250
            enemy_start_x = -200
            enemy_number = 0
            for enemy in enemies:
                x = enemy_start_x + (50 * enemy_number)
                y = enemy_start_y
                enemy.setposition(x, y)
                enemy_number += 1
                if enemy_number == 10:
                    enemy_start_y -=50
                    enemy_number = 0
            wn.update()
            time.sleep(5)
            score = 0
            pen.clear()
            pen.write("Score: {}".format(score), align="left", font=font)
        
    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

# check if bullet hits border

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if score == 3000:
        pen.clear()
        pen.setposition(0,0)
        pen.write("YOU WON!! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        pen.setposition(-290,280)
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        enemy_start_y = 250
        enemy_start_x = -200
        enemy_number = 0
        for enemy in enemies:
            x = enemy_start_x + (50 * enemy_number)
            y = enemy_start_y
            enemy.setposition(x, y)
            enemy_number += 1
            if enemy_number == 10:
                enemy_start_y -=50
                enemy_number = 0
        wn.update()
        time.sleep(5)
        score = 0
        pen.clear()
        pen.write("Score: {}".format(score), align="left", font=font)
    for enemy in enemies:
        if enemy.ycor() < -260:
            print("2")
            pen.clear()
            pen.setposition(0,0)
            pen.write("GAME OVER Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            pen.setposition(-290,280)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy_start_y = 250
            enemy_start_x = -200
            enemy_number = 0
            for enemy in enemies:
                x = enemy_start_x + (50 * enemy_number)
                y = enemy_start_y
                enemy.setposition(x, y)
                enemy_number += 1
                if enemy_number == 10:
                    enemy_start_y -=50
                    enemy_number = 0
            wn.update()
            time.sleep(5)
            score = 0
            pen.clear()
            pen.write("Score: {}".format(score), align="left", font=font)


wn.mainloop()