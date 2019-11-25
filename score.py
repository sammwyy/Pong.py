import pygame

class Score (pygame.sprite.Sprite):
	def __init__ (self, font, pos = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.font = font
		self.pos = pos
		self.score = 0
		self.image = self.font.render(str(self.score), 0, (255, 255, 255))
		self.rect = self.image.get_rect(center = self.pos)

	def score_up (self):
		self.score += 1

	def update(self):
		self.image = self.font.render(str(self.score), 0, (255, 255, 255))
		self.rect = self.image.get_rect(center = self.pos)