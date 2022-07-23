import pygame as pg


# K1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class atk_K1():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/atk_K1/atk1.asset"),
		pg.image.load("data/atk_K1/atk2.asset"),
		pg.image.load("data/atk_K1/atk3.asset"),
		pg.image.load("data/atk_K1/atk4.asset"),
		pg.image.load("data/atk_K1/atk5.asset"),
		]

		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
		pg.transform.flip(self.animation_list_right[4], True, False),
		]


	def animate_right(self,window, x , y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.2

		if self.count >= 5:
			self.count = 0

	def animate_left(self,window, x , y):
		window.blit(self.animation_list_left[int(self.count)],(x , y))
		self.count += 0.2

		if self.count >= 5:
			self.count = 0


atk_K1_animation = atk_K1()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# K2 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class atk_K2():
	def __init__(self):


		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/atk_K2/atk1.asset"),
		pg.image.load("data/atk_K2/atk2.asset"),
		pg.image.load("data/atk_K2/atk3.asset"),
		pg.image.load("data/atk_K2/atk4.asset"),
		pg.image.load("data/atk_K2/atk5.asset"),
		pg.image.load("data/atk_K2/atk6.asset"),
		]

		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
		pg.transform.flip(self.animation_list_right[4], True, False),
		pg.transform.flip(self.animation_list_right[5], True, False),
		]



	def animate_right(self,window, x , y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.2

		if self.count >= 6:
			self.count = 0


	def animate_left(self,window, x , y):
		window.blit(self.animation_list_left[int(self.count)],(x , y))
		self.count += 0.2

		if self.count >= 6:
			self.count = 0


atk_K2_animation = atk_K2()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# K3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class atk_K3():
	def __init__(self):

		self.x = 0
		self.y = 0
		self.count = 0

		self.animation_list_right = [
		pg.image.load("data/atk_K3/atk1.asset"),
		pg.image.load("data/atk_K3/atk2.asset"),
		pg.image.load("data/atk_K3/atk3.asset"),
		pg.image.load("data/atk_K3/atk4.asset"),
		pg.image.load("data/atk_K3/atk5.asset"),
		pg.image.load("data/atk_K3/atk6.asset"),
		]

		self.animation_list_left = [
		pg.transform.flip(self.animation_list_right[0], True, False),
		pg.transform.flip(self.animation_list_right[1], True, False),
		pg.transform.flip(self.animation_list_right[2], True, False),
		pg.transform.flip(self.animation_list_right[3], True, False),
		pg.transform.flip(self.animation_list_right[4], True, False),
		pg.transform.flip(self.animation_list_right[5], True, False),
		]



	def animate_right(self,window, x , y):
		window.blit(self.animation_list_right[int(self.count)],(x , y))
		self.count += 0.15

		if self.count >= 6:
			self.count = 0


	def animate_left(self,window, x , y):
		window.blit(self.animation_list_left[int(self.count)],(x , y))
		self.count += 0.15

		if self.count >= 6:
			self.count = 0


atk_K3_animation = atk_K3()