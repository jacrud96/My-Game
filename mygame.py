#My idea is to do a similar thing to the demo---where there is "things" falling down that are either red which kill you (after 3) or green which u have to get to increase score



import pygame
import math
import os
import random
from pygame import *
from pygame.sprite import *
from random import *


#create colors MAKE MY OWN!!!
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (225, 225, 0)

pygame.init()
screen = display.set_mode((700,500)) #creates a window 
pygame.display.set_caption("Jaclyn Rudolf's Game")

background_image = image.load("space3.bmp")



DELAY = 1000;  

class Player (pygame.sprite.Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = pygame.Surface([40, 20])
		self.image.fill(white)
		#self.rect = self.image.get_rect().move(300,460)
		self.rect = self.image.get_rect()
		self.rect.center = (300, 460)
		self.speed = 10
		self.state = "still"
		self.reinit()
		self.area = screen.get_rect()
		self.score = 0

	def reinit(self):
		self.state = 'still'
		self.movepos = [300,480]

	def update(self):
		newposition = self.rect.move(self.movepos)
		if self.area.contains(newposition):
			self.rect = newposition
		pygame.event.pump()
		self.update_score()

	def moveleft(self):
		self.movepos[0] = self.movepos[0] - (self.speed)
		self.state = "move left"

	def moveright(self):
		self.movepos[0] = self.movepos[0] + (self.speed)
		self.state = "move right"

	def score_create():
		f = font.Font(None, 25)
		t = f.render("Score = " + str(player.score), False, (255,255,255))

	def update_score(self):
		pygame.font.init()
		if self.rect.colliderect(redObj.rect):
			self.score = self.score - 1
		if self.rect.colliderect(greenObj.rect):
			self.score = self.score + 1
		# if self.score == 10:
		# 	font = pygame.font.Font(None, 36)
		# 	text = font.render("You Won", False, (255,255,255))    
		# 	textpos = text.get_rect()
		# 	screen.blit(text,(350, 250))
		# 	pygame.time.delay(3000)
		# if self.score == -10:
		# 	font = pygame.font.Font(None, 36)
		# 	text = font.render("Game Over", False, (255, 255, 255))
		# 	textpos = text.get_rect()
		# 	screen.blit(text,(350, 250))
		# 	pygame.time.delay(3000)

  #   def score_create():
		# f = font.Font(None, 25)
		# t = f.render("Score = " + str(player.score), False, (0,0,0))


  
class Points (pygame.sprite.Sprite):
	def __init__(self):
		self.image= pygame.Surface


class GreenPiece(pygame.sprite.Sprite):
	def __init__(self, groups):
		Sprite.__init__(self)
		self.image = pygame.Surface([20, 20])
		self.image.fill(green)
		self.rect = self.image.get_rect()
		self.rect.center = (350, 0)

		self.velocity = randint(3, 5)
		self.add(groups)
       

    # move gold to a new random location
	def move(self):
		cent_x = self.rect.centerx
		cent_y = self.rect.centery
		# current_rect = self.image.get_rect()
		randX = randint(cent_x-10, cent_x+10)
		randY = randint(cent_y, cent_y+10)
		self.rect.center = (randX,randY)


	def update(self):
		x, y = self.rect.center
		if y>500:
			x, y = randint(10,750), 0  #350
			self.velocity  = randint(3, 5)
		else:
			x, y = x, y+self.velocity
		self.rect.center = x, y

    		

		



class RedPiece(pygame.sprite.Sprite): #Do i need to make it Pygame.sprite.Sprite ?
	def __init__(self):
		Sprite.__init__(self)
		self.image = pygame.Surface([20, 20])
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.rect.center = (350, 0)

		self.velocity = randint(3, 5)
		


    # move gold to a new random location
	def move(self):
		cent_x = self.rect.centerx
		cent_y = self.rect.centery
		# current_rect = self.image.get_rect()
		randX = randint(cent_x-10, cent_x+10)
		randY = randint(cent_y, cent_y+10)
		self.rect.center = (randX,randY)

	def update(self):
		x, y = self.rect.center
		if y>500:
			x, y = 350, 0
			self.velocity  = randint(3, 5)
		else:
			x, y = x, y+self.velocity
		self.rect.center = x, y



everything = pygame.sprite.Group()

#THIS WAS ON STARTER CODE

greenObj = GreenPiece(everything)
greenObj1 = GreenPiece(everything)
greenObj2 = GreenPiece(everything)
redObj = RedPiece()
redObj1 = RedPiece()
redObj2 = RedPiece()
player = Player()
init()

screen = display.set_mode((640, 480))
display.set_caption('Get to 10!')

f = pygame.font.Font(None, 25)

greenObj = GreenPiece(everything)
greenObj1 = GreenPiece(everything)
greenObj2 = GreenPiece(everything)
redObj = RedPiece()
redObj1 = RedPiece()
redObj2 = RedPiece()
player = Player()
#group2 = pygame.sprite.group()


time.set_timer(USEREVENT + 1, DELAY)



# # creates a group of sprites so all can be updated at once
sprites = RenderPlain(player, redObj, redObj1, redObj2, greenObj, greenObj1, greenObj2)


pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)

# loop until user quits
while True:
	e = event.poll()
	if e.type == QUIT:
		quit()
		break
	if e.type == KEYDOWN:
		if e.key == pygame.K_RIGHT:
			player.moveright()
		if e.key == pygame.K_LEFT:
			player.moveleft()
	elif e.type == KEYUP:
		if e.key == K_LEFT or e.key == K_RIGHT:
			player.movepos = [0,0]
			player.state = "still"
	# elif e.type == MOUSEBUTTONDOWN: 
	# 	if Player.update_score(RedPiece):
	# 		mixer.Sound("Explosion1.wav").play()
	elif e.type == USEREVENT + 1: 
		greenObj.move()
		greenObj1.move()
		greenObj2.move()
		redObj.move()
		redObj1.move()
		redObj2.move()
	elif player.score == 11 or player.score == -11:
		break

	screen.blit(background_image, (0,0))

    # refill background color so that we can paint sprites in new locations
	# screen.fill(white)
	t = f.render("Score = " + str(player.score), False, (255,255,255))
	screen.blit(t, (320, 0))    

     #+ (int(player.score))  #hits
      # draw text to screen.  Can you move it?

    # update and redraw sprites
	sprites.update()
	sprites.draw(screen)
	display.update()
	everything.update()

sprites.draw(screen)

print ('done')
print (player.score)
if player.score > 10:
	print("won")
	font = pygame.font.Font(None, 36)
	text = font.render("You Won", False, (255,255,255))    
	textpos = text.get_rect()
	screen.blit(text,(350, 250))
if player.score < -10:
	print("loss")
	font = pygame.font.Font(None, 36)
	text = font.render("Game Over", False, (255, 255, 255))
	textpos = text.get_rect()
	screen.blit(text,(350, 250))
	

# sprites.update()
display.update()
# everything.update()
pygame.time.delay(2000)
pygame.quit()

