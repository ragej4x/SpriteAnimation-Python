import pygame as pg


class jump():
	def __init__(self):

		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/jump/jump1.asset"),
		pg.image.load("data/jump/jump2.asset"),
		pg.image.load("data/jump/jump3.asset"),
		pg.image.load("data/jump/jump4.asset"),

		]

		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
		]



	def animate_right(self,window , x ,y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.15

		if self.count >= 4:
			self.count = 0

	def animate_left(self,window, x , y):
		window.blit(self.animation_list_left[int(self.count)] ,(x, y))
		self.count += 0.1

		if self.count >= 4:
			self.count = 0

jump_animation = jump()


# FALL +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class fall():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/jump/fall1.asset"),
		pg.image.load("data/jump/fall2.asset"),
		]

		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		]



	def animate_right(self,window, x ,y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.15

		if self.count >= 2:
			self.count = 0

	def animate_left(self,window, x ,y):
		window.blit(self.animation_list_left[int(self.count)] ,(x , y))
		self.count += 0.15

		if self.count >= 2:
			self.count = 0

fall_animation = fall()