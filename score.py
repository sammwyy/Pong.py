# Import the Pygame library
import pygame

# Define class score for easy imporit in the main.py
class Score (pygame.sprite.Sprite):
	# Define main function
	def __init__ (self, font, pos = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.font = font
		self.pos = pos
		self.score = 0
		self.image = self.font.render(str(self.score), 0, (255, 255, 255))
		self.rect = self.image.get_rect(center = self.pos)

	# Add 1+ point to the score
	def score_up (self):
		self.score += 1

	# Update sprite
	def update(self):
		self.image = self.font.render(str(self.score), 0, (255, 255, 255))
		self.rect = self.image.get_rect(center = self.pos)
