from turtle import *
import os
import math

playingGame = True
quitGame = False
enemies = []

def SetupScreen(wn):
	wn.bgcolor("black")
	wn.title("Space Invaders")


	border_pen = Turtle()
	border_pen.speed(0)
	border_pen.color("white")
	border_pen.penup()
	border_pen.setposition(-300,-300)
	border_pen.pendown()
	border_pen.pensize(3)
	for side in range(4):
		border_pen.fd(600)
		border_pen.lt(90)
	border_pen.hideturtle()
	wn.listen()

class Bullet(Turtle):
	def __init__(self, player):
		super().__init__()
		self.hideturtle()
		self.color("red")
		self.shape("triangle")
		self.penup()
		self.speed(0)
		self.setposition(player.xcor(), player.ycor())
		self.setheading(90)
		self.showturtle()
		self.speed = 10
		self.collided = False
		self.moving = True

class Enemy(Turtle):
	def __init__(self,pos):
		super().__init__()
		self.hideturtle()
		self.color("green")
		self.shape("circle")
		self.penup()
		self.speed(0)
		self.setposition(pos,200)
		self.speed = 10
		self.st()

class Player:
	def __init__(self,wn):
		self.player = Turtle()
		self.player.color("blue")
		self.player.shape("triangle")
		self.player.penup()
		self.player.speed(0)
		self.player.setposition(0,-250)
		self.player.setheading(90)
		self.speed = 2
		self.moving = False
		self.direction = ""
		self.bullets = []

		wn.onkeypress(self.MoveLeft,"Left")
		wn.onkeyrelease(self.StopMoving,"Left")
		wn.onkeypress(self.MoveRight,"Right")
		wn.onkeyrelease(self.StopMoving,"Right")
		wn.onkey(self.Fire,"space")
		

	def StopMoving(self):
		self.moving = False
		self.direction = ""

	def MoveLeft(self):
		self.moving = True
		self.direction = "Left"

	def MoveRight(self):
		self.moving = True
		self.direction = "Right"

	def Fire(self):
		bullet = Bullet(self.player)
		self.bullets.append(bullet)
		print(len(self.bullets))

def CreateEnemies(positions):
	for pos in positions:
		enemies.append(Enemy(pos))

def MoveBullets(player,enemies):
	for bullet in player.bullets:
		bullet.sety(bullet.ycor() + bullet.speed)
		for enemy in enemies:
			if IsCollide(enemy,bullet):
				player.bullets.remove(bullet)
				bullet.clear()
				bullet.reset()
				continue
		if bullet.ycor() > 285:
			player.bullets.remove(bullet)
			bullet.clear()
			bullet.reset()


def IsCollide(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor() + t2.xcor(),2)) + math.sqrt(math.pow(t1.ycor() + t2.ycor(),2))
	print(distance)
	return False
	# if distance <= 15:
	# 	return True
	# else:
	# 	return False

def MovePlayer(player):
	if player.direction == "Left":
		if player.player.xcor() <= -285:
			player.moving = False
		else:
			player.player.setx(player.player.xcor() - player.speed)
	elif player.direction =="Right":
		if player.player.xcor() >= 285:
			player.moving = False
		else:
			player.player.setx(player.player.xcor() + player.speed)

def Quit():
	global playingGame
	playingGame = False

wn = Screen()
SetupScreen(wn)
player = Player(wn)
onkey(Quit,'q')
CreateEnemies([-200,-100,0,100,200])

while playingGame:
	MovePlayer(player)
	MoveBullets(player,enemies)


	wn.update()

# mainloop()
