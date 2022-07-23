import pygame as pg

class run():
	def __init__(self):

		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/run/run1.asset"),
		pg.image.load("data/run/run2.asset"),
		pg.image.load("data/run/run3.asset"),
		pg.image.load("data/run/run4.asset"),
		pg.image.load("data/run/run5.asset"),
		pg.image.load("data/run/run6.asset"),
		]

		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
		pg.transform.flip(self.animation_list_right[4], True, False),
		pg.transform.flip(self.animation_list_right[5], True, False),
		]


	def alpha(self):
		self.animation_list_right[0].set_alpha(0)
		self.animation_list_right[1].set_alpha(0)
		self.animation_list_right[2].set_alpha(0)
		self.animation_list_right[3].set_alpha(0)

		self.animation_list_left[0].set_alpha(0)
		self.animation_list_left[1].set_alpha(0)
		self.animation_list_left[2].set_alpha(0)
		self.animation_list_left[3].set_alpha(0)

	def un_alpha(self):
		self.animation_list_right[0].set_alpha(500)
		self.animation_list_right[1].set_alpha(500)
		self.animation_list_right[2].set_alpha(500)
		self.animation_list_right[3].set_alpha(500)

		self.animation_list_left[0].set_alpha(500)
		self.animation_list_left[1].set_alpha(500)
		self.animation_list_left[2].set_alpha(500)
		self.animation_list_left[3].set_alpha(500)




	def animate_right(self,window , x ,y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.15

		if self.count >= 6:
			self.count = 0

	def animate_left(self,window , x ,y):
		window.blit(self.animation_list_left[int(self.count)] ,(x , y))
		self.count += 0.15

		if self.count >= 6:
			self.count = 0

run_animation = run()