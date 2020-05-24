"""
Title: Classes
Authour: Dhiraj Meenavilli
Date: June/02/2019
"""
import pygame
import random
pygame.init()

### -------- Variables ------- ###

hurt = 0

Width = 800
Height = 600 # I set the width and height separately so that they can be referred to if needed
window = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Reaper.exe")

inLevel = False # I thought it would make the most sense to use these booleans to create levels by using these to trigger specific events at specific times instead of hard coding.
LvL_1 = False
LvL_1_Done = False
LvL_2 = False
LvL_2_Done = False

scale_x = 60 # I found this to be the optimal x and y for characters to be displayed balancing aesthetics and keeping functionality.
scale_y = 60

j = 0 # I need to find more appropriate names for these
k = 0

#### -------------------------- Image Loading ---------------------- ##########

bg = pygame.image.load('C:media\MapAssets\MainHub.png')
bg = pygame.transform.scale(bg,(800,600)) # Ironically if I try to make it smaller than this everything breaks down

#### ---- Player ---- ####

left_one = pygame.image.load('C:media\Main\LW1.png')
left_two = pygame.image.load('C:media\Main\LW2.png')
left_one = pygame.transform.scale(left_one,(scale_x,scale_y))
left_two = pygame.transform.scale(left_two,(scale_x,scale_y))

pr_Left = [left_one,left_two] # I put them all in arrays so that can easily be cycled through when they need to be blitted


right_one = pygame.image.load('C:media\Main\RW1.png')
right_two = pygame.image.load('C:media\Main\RW2.png')
right_one = pygame.transform.scale(right_one,(scale_x,scale_y))
right_two = pygame.transform.scale(right_two,(scale_x,scale_y))

pr_Right = [right_one, right_two]


left_stand = pygame.image.load('C:media\Main\LS.png')
right_stand = pygame.image.load('C:media\Main\RS.png')
left_stand = pygame.transform.scale(left_stand,(scale_x,scale_y))
right_stand = pygame.transform.scale(right_stand,(scale_x,scale_y))

Standing = [left_stand,right_stand]

#### ---- Ghost ---- ####

ghost_right = pygame.image.load('C:media\Ghost\Right.png')
ghost_left = pygame.image.load('C:media\Ghost\Left.png')
ghost_left = pygame.transform.scale(ghost_left,(scale_x,scale_y))
ghost_right = pygame.transform.scale(ghost_right,(scale_x,scale_y))

gt_Move = [ghost_left,ghost_right]

#### ---- ABB ---- ####

normalLeft = pygame.image.load('C:media\ABB\omL1.png')
normalLeft = pygame.transform.scale(normalLeft,(scale_x,scale_y))
normalLeft1 = pygame.image.load('C:media\ABB\omL2.png')
normalLeft1 = pygame.transform.scale(normalLeft1,(scale_x,scale_y))

ABBLeft = [normalLeft,normalLeft1]

normalRight = pygame.image.load('C:media\ABB\omR1.png')
normalRight = pygame.transform.scale(normalRight,(scale_x,scale_y))
normalRight1 = pygame.image.load('C:media\ABB\omR2.png')
normalRight1 = pygame.transform.scale(normalRight1,(scale_x,scale_y))

ABBRight = [normalRight,normalRight1]

angryLeft1 = pygame.image.load('C:media\ABB\ongL1.png')
angryLeft1 = pygame.transform.scale(angryLeft1,(scale_x,scale_y))
angryLeft2 = pygame.image.load('C:media\ABB\ongL2.png')
angryLeft2 = pygame.transform.scale(angryLeft2,(scale_x,scale_y))
angryLeft3 = pygame.image.load('C:media\ABB\ongL3.png')
angryLeft3 = pygame.transform.scale(angryLeft3,(scale_x,scale_y))
angryLeft4 = pygame.image.load('C:media\ABB\ongL4.png')
angryLeft4 = pygame.transform.scale(angryLeft4,(scale_x,scale_y))

angryLeft = [angryLeft1,angryLeft2,angryLeft3,angryLeft4]

angryRight1 = pygame.image.load('C:media\ABB\ongR1.png')
angryRight1 = pygame.transform.scale(angryRight1,(scale_x,scale_y))
angryRight2 = pygame.image.load('C:media\ABB\ongR2.png')
angryRight2 = pygame.transform.scale(angryRight2,(scale_x,scale_y))
angryRight3 = pygame.image.load('C:media\ABB\ongR3.png')
angryRight3 = pygame.transform.scale(angryRight1,(scale_x,scale_y))
angryRight4 = pygame.image.load('C:media\ABB\ongR4.png')
angryRight4 = pygame.transform.scale(angryRight1,(scale_x,scale_y))

angryRight = [angryRight1,angryRight2,angryRight3,angryRight4]

#### ---- Keys and other Items ---- ####

key1 = pygame.image.load('C:media\MapAssets\key1.png')
key2 = pygame.image.load('C:media\MapAssets\key2.png')
key3 = pygame.image.load('C:media\MapAssets\key3.png')
heart = pygame.image.load('C:media\MapAssets\hart.png')
heart = pygame.transform.scale(heart,(40,60))

seen = [ABBRight,ABBLeft,angryLeft,angryRight,gt_Move]
########## --------------------------------- Classes --------------------------- ##################

class assets(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = (self.x, self.y + 11, self.width, self.height)

	def get_X(self):
		return self.x

	def set_X(self,x):
		self.x = x

	def get_Y(self):
		return self.y

	def set_Y(self,y):
		self.y = y
	def get_Height(self):
		return self.height

	def get_Width(self):
		return self.width

	def showHitBox(self,adjustx,adjusty):
		self.hitbox = (self.x, self.y + 11, self.width - adjustx, self.height - adjusty)

class char(assets):
	def __init__(self,x,y,width,height,vel = 5):
		assets.__init__(self,x,y,width,height)
		self.vel = vel
		self.xdir = 1
		self.steps = 0
		self.looking = 0

	def change_look(self,new_look):
		self.looking = new_look

	def change_vel(self,new_vel):
		self.vel = new_vel

	def change_Dir(self,new_Dir):
		self.xdir = new_Dir

	def get_xDir(self):
		return self.xdir

	def reset_Steps(self):
		if self.steps > 100:
			self.steps = 0

class Hero(char):
	def __init__(self,x,y,width,height,vel = 5,hp = 3):
		char.__init__(self,x,y,width,height,vel)
		self.hp = hp
		self.jump = -20
		self.hp = hp
		self.dash = 20

	def draw(self,pressedKeys):
		if pressedKeys[pygame.K_d]:
			self.steps += 1
			self.x += self.vel
			self.change_look(1)
			self.change_Dir(1)
			window.blit(pr_Right[self.steps%2], (self.x,self.y))

		if pressedKeys[pygame.K_a]:
			self.steps += 1
			self.x -= self.vel
			self.change_look(0)
			self.change_Dir(-1)
			window.blit(pr_Left[self.steps % 2], (self.x, self.y))

		if pressedKeys[pygame.K_w]:
			self.x += self.dash*self.xdir
			window.blit(Standing[self.looking], (self.x, self.y))

		self.showHitBox(20,10)

		self.reset_Steps()

		if self.jump > 20:
			self.jump = -20

		if pressedKeys[pygame.K_d] == False and pressedKeys[pygame.K_a] == False and pressedKeys[pygame.K_w] == False:
			window.blit(Standing[self.looking], (self.x, self.y))

	def change_Dash(self,dash_Spd):
		self.dash = dash_Spd

	def hit(self):
		self.hp -= 1

	def get_hp(self):
		return self.hp


class Enemy(char):
	def __init__(self,x,y,width,height,vel = 5):
		char.__init__(self,x,y,width,height,vel)

	def draw(self,j,creature,boundLeft,boundRight,playery):
		self.reset_Steps()
		self.steps += 1

		if creature == 1:
			adjustx = 20
			adjusty = 15
			if self.xdir == 1:
				choice = 0
				if playery == 485:
					self.vel = 15
					choice = 3

			if self.xdir == -1:
				choice = 1
				if playery == 485:
					self.vel = 10
					choice = 2

			if self.x < boundLeft:
				self.xdir = 1
			if self.x > boundRight:
				self.xdir = -1
				choice = 1
			self.x += self.vel * self.xdir

		if creature == 2:
			choice = 4
			adjustx = 0
			adjusty = 0
			if j % 30 == 7:
				positions = [0,50,100,150,200,250,300,450,500,550,600.650]
				self.x = positions[random.randrange(11)]
		self.showHitBox(adjustx,adjusty)
		window.blit(seen[choice][self.steps%2], (self.x, self.y))

Spoon = Hero(0,540,scale_x,scale_y)

lvl1_Door = assets(310,520,30,70)
lvl2_Door = assets(410,520,30,70)


lvl1_Exit = assets(40,530,30,70)
lvl2_Exit = assets(30,540,30,70)

lvl1_Key = assets(675,485,30,30)
lvl2_Key = assets(670,550,30,30)

Fork = Enemy(200,540,scale_x,scale_y)  # The anger in my heart warms you now,
Knife = Enemy(270,485,scale_x,scale_y)  # But it will you leave cold in your grave.

def interact(player,item):
	if player.hitbox[1] < item.hitbox[1] + item.hitbox[3] and item.hitbox[1] + item.hitbox[3] > item.hitbox[1]:
		if player.hitbox[0] + player.hitbox[2] > item.hitbox[0] and player.hitbox[0] < item.hitbox[0] + item.hitbox[2]:
			return True

run = True
while run:
	pygame.time.delay(65)
	pressedKeys = pygame.key.get_pressed()

	window.blit(bg, (0, 0))
	Spoon.draw(pressedKeys)

	if Spoon.get_hp() == 0:
		run = False

	for i in range(Spoon.get_hp()): # This is so that the amount of hearts will be representative of the amount of lives which the player still has
		window.blit(heart,(i*40,300))

	if not inLevel:
		Spoon.change_Dash(20)
		lvl1_Door.showHitBox(0,0)
		lvl2_Door.showHitBox(0,0)
		j = 0

	## Level 1
	if interact(Spoon,lvl1_Door) and pressedKeys[pygame.K_SPACE]: # If the player goes to the first door and presses space the code will load a new background and set the hero at a new x and y
		bg = pygame.image.load('C:media\MapAssets\LVL1Locked.png')
		bg = pygame.transform.scale(bg,(800,600))
		Spoon.set_X(150)
		Spoon.set_Y(390)
		inLevel = True
		LvL_1 = True

	if LvL_1:
		Spoon.change_Dash(100)
		Knife.draw(j, 1, 230, 640, Spoon.get_Y())

	if LvL_1 and not LvL_1_Done:
		window.blit(key1, (675, 485))

	if LvL_1 and Spoon.get_X() > 225: # In level 1 the box the entry door is on ends at the x coordinate at 225 so for continuity purposes for the player I set the charachters y such that it'll look like he dropped.
		Spoon.set_Y(485)

	if LvL_1 and Spoon.get_X() == 675: # This is where the key will be therefore the background needs to once again change such that the player knows they are allowed to leave, and where to go to leave.
		bg = pygame.image.load('C:media\MapAssets\LVL1open.png')
		bg = pygame.transform.scale(bg, (800, 600))
		LvL_1_Done = True

	if interact(Spoon,Knife) and LvL_1 and Spoon.get_Y() == 485:
		Spoon.set_X(150)
		Spoon.hit()

	if LvL_1_Done and LvL_1:
		Spoon.change_Dash(20)
		lvl1_Exit.showHitBox(0,0)

	if LvL_1_Done and Spoon.get_X() < 500:
		Spoon.set_Y(540)

	leave = interact(Spoon,lvl1_Exit)

	if leave and pressedKeys[pygame.K_SPACE]:
		bg = pygame.image.load('C:media\MapAssets\MainHub.png')
		bg = pygame.transform.scale(bg, (800, 600))
		inLevel = False
		LvL_1 = False
		LvL_1_Done = False

	## Level 2

	if interact(Spoon, lvl2_Door) and pressedKeys[pygame.K_SPACE]:
		bg = pygame.image.load('C:media\MapAssets\LVL2Locked.png')
		bg = pygame.transform.scale(bg, (800, 600))
		Spoon.set_X(365)
		inLevel = True
		LvL_2 = True

	if LvL_2:
		j += 1
		Fork.draw(j,2,0,800,Spoon.get_Y())
		lvl2_Key.showHitBox(0,0)

	if LvL_2 and not LvL_2_Done:
		window.blit(key2, (675, 545))

	if interact(Spoon,Fork) and LvL_2:
		Spoon.set_X(410)
		Spoon.hit()

	if LvL_2 and Spoon.get_X() > 650:
		bg = pygame.image.load('C:media\MapAssets\LVL2open.png')
		bg = pygame.transform.scale(bg, (800, 600))
		LvL_2_Done = True
		lvl2_Exit.showHitBox(0,0)

	LvL2_Exit = interact(Spoon,lvl2_Exit)

	if LvL2_Exit and pressedKeys[pygame.K_SPACE]:
		bg = pygame.image.load('C:media\MapAssets\MainHub.png')
		bg = pygame.transform.scale(bg, (800, 600))
		inLevel = False
		LvL_2 = False
		LvL_2_Done = False

	## ---- Exit ---- ##

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
