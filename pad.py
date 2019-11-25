import pygame

class Pad (pygame.sprite.Sprite):
	def __init__ (self, pos = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((20, 100)).convert()
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect(center = pos)
		self.max_speed = 10
		self.speed = 0

	def move_up (self):
		self.speed = self.max_speed * -1

	def move_down (self):
		self.speed = self.max_speed * 1

	def stop (self):
		self.speed = 0

	def update (self):
		self.rect.move_ip (0, self.speed)