import pygame as pg
import jump , idl, atk, run


class player_mechanics():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.y_vel = 5
		self.left = False
		self.right = False

		self.idle_left = False
		self.idle_right = False

		self.atk_1 = False
		self.atk_2 = False
		self.atk_3 = False

		self.cd = False
		self.cd_count = 10

		self.jump = False
		self.on_air = False

		self.y_vel = 0
		

	

	def movement(self,window , keyinput):
		dx = 0
		dy = 0
		self.rect = pg.Rect(self.x +15 ,self.y +10 , 20,30)
		pg.draw.rect(window,(255,0,0),(self.rect),1)



		#MOVEMENT
		run.run_animation.x = self.x
		run.run_animation.y = self.y

		idl.idle_animation.x = self.x
		idl.idle_animation.y = self.y

		atk.atk_K1_animation.x = self.x
		atk.atk_K1_animation.y = self.y

		atk.atk_K2_animation.x = self.x
		atk.atk_K2_animation.y = self.y

		atk.atk_K3_animation.x = self.x
		atk.atk_K3_animation.y = self.y

		jump.jump_animation.x = self.x
		jump.jump_animation.y = self.y

		jump.fall_animation.x = self.x
		jump.fall_animation.y = self.y



		if keyinput[pg.K_RIGHT] and self.atk_1 == False and self.atk_2 == False and self.atk_3 == False: 
			self.right = True
			self.left = False

			self.idle_left = False
			self.idle_right = True
			dx += 2


		if keyinput[pg.K_LEFT] and self.atk_1 == False and self.atk_2 == False and self.atk_3 == False:
			self.left = True
			self.right = False

			self.idle_left = True
			self.idle_right = False
			dx -= 2
			


		if self.right == True and keyinput[pg.K_RIGHT] and self.atk_1 == False and self.atk_2 == False and self.atk_3 == False:
			run.run_animation.animate_right(window)

		if self.left == True and keyinput[pg.K_LEFT] and self.atk_1 == False and self.atk_2 == False and self.atk_3 == False:
			run.run_animation.animate_left(window)



		if self.idle_right == True:
			if not keyinput[pg.K_RIGHT]:
				idl.idle_animation.animate_right(window)



		if self.idle_left == True:
			if not keyinput[pg.K_LEFT]:
				idl.idle_animation.animate_left(window)


		if keyinput[pg.K_LEFT] and keyinput[pg.K_RIGHT]:
			self.left = False
			self.right = True


		#JUMP




		if keyinput[pg.K_UP] and self.jump == False:
			self.jump = True
			self.y_vel = -15

		if keyinput[pg.K_UP] == False:
			self.jump = False


		self.y_vel += 1
		if self.y_vel > 10:
			self.y_vel = 10
		
		dy += self.y_vel
		self.x += dx
		self.y += dy



		if self.on_air == True:
			jump.fall_animation.animate_right(window)
			idl.idle_animation.alpha()


		if self.rect.bottom > 100:
			self.rect.bottom = 100
			self.y = 0


		print(self.y)




	def attack(self,window, keyinput):

		#ACTIONS
		idl.idle_animation.un_alpha()

		self.cd_count += 0.1
		if self.cd_count >= 10:
			self.cd = False



		#ATK 1

		if keyinput[pg.K_q] and self.right == True and self.cd == False and self.cd_count >= 0:
			self.atk_1 = True
			self.cd = True
			self.cd_count = 0

 
		if keyinput[pg.K_q] and self.left == True and self.cd == False and self.cd_count >= 0:
			self.atk_1 = True
			self.cd = True
			self.cd_count = 0

	
		if self.atk_1 == True and self.right == True:
			atk.atk_K1_animation.animate_right(window)
			idl.idle_animation.alpha()


		if self.atk_1 == True and self.left == True :
			atk.atk_K1_animation.animate_left(window)
			idl.idle_animation.alpha()



		if atk.atk_K1_animation.count == 0:
			self.atk_1 = False



		#ATK 2

		if atk.atk_K1_animation.count >= 4 and self.right == True:
			self.atk_2 = True

		if atk.atk_K1_animation.count >= 4 and self.left == True:
			self.atk_2 = True

		if self.atk_2 == True and self.right == True:
			atk.atk_K2_animation.animate_right(window)
			idl.idle_animation.alpha()

		if self.atk_2 == True and self.left == True:
			atk.atk_K2_animation.animate_left(window)
			idl.idle_animation.alpha()


		if atk.atk_K2_animation.count == 0:
			self.atk_2 = False

		#ATK 3

		if atk.atk_K2_animation.count >= 5 and self.right == True:
			self.atk_3 = True


		if atk.atk_K2_animation.count >= 5 and self.left == True:
			self.atk_3 = True


		if self.atk_3 == True and self.right == True:
			atk.atk_K3_animation.animate_right(window)
			idl.idle_animation.alpha()

		if self.atk_3 == True and self.left == True:
			atk.atk_K3_animation.animate_left(window)
			idl.idle_animation.alpha()


		if atk.atk_K3_animation.count == 0:
			self.atk_3 = False


		#SWING PHYSICS

		if atk.atk_K3_animation.count >= 1 and self.right == True:
			dx += 0.2

		if atk.atk_K3_animation.count >= 1 and self.left == True:
			dx -= 0.2


player = player_mechanics()
