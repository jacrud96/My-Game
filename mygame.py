
import pygame
import math
import os
import random
from pygame import *
from pygame.sprite import *
from random import *


color_white = (255,255,255)
color_black = (0,0,0)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_yellow = (225, 225, 0)

pygame.init()
screen = display.set_mode((700,500)) #Creates a window of this size  
pygame.display.set_caption("Jaclyn Rudolf's Game") #Caption of the game

background_image = image.load("space3.bmp") #Adds the background image of space



DELAY = 1000;  

class Player (pygame.sprite.Sprite):   #class to create the Player at the bottom of the screen, inheritance from Sprite
	def __init__(self):
		Sprite.__init__(self)
		self.image = pygame.Surface([40, 20])    
		self.image.fill(color_white) #the players color
		self.rect = self.image.get_rect()
		self.rect.center = (300, 460)
		self.speed = 10  #the speed of the player back and forth from left to right
		self.state = "still"   
		self.reinit()
		self.area = screen.get_rect()
		self.score = 0    #initializes score to zero

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
		t = f.render("Score = " + str(player.score), False, (255,255,255)) #creates score (in white)

	def update_score(self):
		pygame.font.init()
		if self.rect.colliderect(redObj.rect):    #updates score when it collides with red objects (decreases) v green (increases)
			self.score = self.score - 1
		if self.rect.colliderect(greenObj.rect):
			self.score = self.score + 1
		

  
class Points (pygame.sprite.Sprite):
	def __init__(self):
		self.image= pygame.Surface


class GreenPiece(pygame.sprite.Sprite):   #This class is for the green pieces
	def __init__(self, groups):
		Sprite.__init__(self)
		self.image = pygame.Surface([20, 20])
		self.image.fill(color_green)
		self.rect = self.image.get_rect()
		self.rect.center = (350, 0)

		self.velocity = randint(3, 5)   #sets the velocity of the green pieces falling randomly between 3 and 5 
		self.add(groups)     #more than one
       
	def move(self):
		cent_x = self.rect.centerx
		cent_y = self.rect.centery
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
		self.image.fill(color_red)
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

