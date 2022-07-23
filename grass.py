import pygame as pg

class grass_tile():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.count = 0

		self.animation_list = [
		pg.image.load("data/blocks/grass/grass1.asset"),
		pg.image.load("data/blocks/grass/grass2.asset"),
		pg.image.load("data/blocks/grass/grass3.asset"),
		pg.image.load("data/blocks/grass/grass4.asset"),
		]

	def action(self,window):

		window.blit(self.animation_list[int(self.count)],(self.x ,self.y))

		self.count += 0.2
		if self.count >= 4:
			self.count = 0

grass_block = grass_tile()