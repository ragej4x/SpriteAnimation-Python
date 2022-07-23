import pygame as pg

class home_map():
	def __init__(self):
		self.size = 20
		self.tile = ("level1_data.txt")




	def tiles(self,window):
		y = 0
		with open(self.tile, "r") as map_1:
			x = 0
			for row in map_1:

				if row == 1:
					print("A")
					pg.draw.rect(window,(255,0,255),(x * self.size ,y * self.size ,self.size,self.size))
				if row == 0:
					pg.Rect(x * self.size ,y * self.size ,self.size,self.size)
				x += 1
			y += 1
map_1 = home_map()
