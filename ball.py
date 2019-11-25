import pygame

class Ball (pygame.sprite.Sprite):
	def __init__ (self, pos = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface ((20, 20)).convert()
		self.pos = pos
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect(center = self.pos)
		self.speed_x = 0
		self.speed_y = 0

	def change_y (self):
		self.speed_y *= -1

	def change_x (self):
		self.speed_x *= -1

	def start (self, speed_x, speed_y):
		self.speed_x = speed_x
		self.speed_y = speed_y

	def stop (self):
		self.speed_x = 0
		self.speed_y = 0

	def reset (self):
		self.rect = self.image.get_rect (center = self.pos)

	def update (self):
		self.rect.move_ip (self.speed_x, self.speed_y)