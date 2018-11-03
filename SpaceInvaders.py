from turtle import *
import os

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

class Bullet:
	def __init__(self, player):
		player = player
		self.bullet = Turtle()
		self.bullet.hideturtle()
		self.bullet.color("red")
		self.bullet.shape("triangle")
		self.bullet.penup()
		self.bullet.speed(0)
		self.bullet.setposition(player.xcor(), player.ycor())
		self.bullet.setheading(90)
		self.bullet.st()
		self.speed = 10
		self.collided = False
		self.moving = False

	def MoveBullet(self):
		if self.moving:
			pass
		else:
			self.moving = True
			while not self.collided and self.moving:
				self.bullet.sety(self.bullet.ycor() + self.speed)
				if self.bullet.ycor() >= 600:
					self.bullet.ht()
					self.collided = True
					self.moving = False

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
		self.bullets = []

		wn.onkeypress(self.MoveLeft,"Left")
		wn.onkeyrelease(self.StopMoving,"Left")
		wn.onkeypress(self.MoveRight,"Right")
		wn.onkeyrelease(self.StopMoving,"Right")
		wn.onkey(self.Fire,"space")
		

	def StopMoving(self):
		self.moving = False

	def MoveLeft(self):
		if self.moving:
			pass
		else:
			self.moving = True
			while self.moving:
				if self.player.xcor() <= -285:
					self.moving = False
				else:
					self.player.setx(self.player.xcor() - self.speed)

		

	def MoveRight(self):
		if self.moving:
			pass
		else:
			self.moving = True
			while self.moving:
				if self.player.xcor() >= 285:
					self.moving = False
				else:
					self.player.setx(self.player.xcor() + self.speed)

	def Fire(self):
		bullet = Bullet(self.player)
		bullet.MoveBullet()
		self.bullets.append(bullet)


def Main():
	wn = Screen()
	SetupScreen(wn)
	player = Player(wn)

	wn.mainloop()

Main()