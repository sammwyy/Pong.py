# Import the Pygame library
import pygame

# Define class pad for easy imporit in the main.py
class Pad (pygame.sprite.Sprite):
	# define main function
	def __init__ (self, pos = (0, 0)):
		# Create sprite
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((20, 100)).convert()
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect(center = pos)
		self.max_speed = 10
		self.speed = 0

	# Move up pad
	def move_up (self):
		self.speed = self.max_speed * -1

	# Move down pad
	def move_down (self):
		self.speed = self.max_speed * 1

	# Stop pad movement
	def stop (self):
		self.speed = 0

	# Update pad movement
	def update (self):
		self.rect.move_ip (0, self.speed)
