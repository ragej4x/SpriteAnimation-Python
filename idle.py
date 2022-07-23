import pygame as pg

class idle():
	def __init__(self):

		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/idle/idl1.asset"),
		pg.image.load("data/idle/idl2.asset"),
		pg.image.load("data/idle/idl3.asset"),
		pg.image.load("data/idle/idl4.asset"),
		]



		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
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


	def animate_right(self,window,x , y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.1

		if self.count >= 4:
			self.count = 0


	def animate_left(self,window,x , y):
		window.blit(self.animation_list_left[int(self.count)],(x , y))
		self.count += 0.1

		if self.count >= 4:
			self.count = 0





idle_animation = idle()





class idle_2():
	def __init__(self):

		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/idle/idl2_1.asset"),
		pg.image.load("data/idle/idl2_2.asset"),
		pg.image.load("data/idle/idl2_3.asset"),
		pg.image.load("data/idle/idl2_4.asset"),
		]



		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
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


	def animate_right(self,window,x , y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.1

		if self.count >= 4:
			self.count = 0


	def animate_left(self,window,x , y):
		window.blit(self.animation_list_left[int(self.count)],(x , y))
		self.count += 0.1

		if self.count >= 4:
			self.count = 0





idle_animation_2 = idle_2()