# Import the Pygame library
import pygame

# Define class ball for easy imporit in the main.py
class Ball (pygame.sprite.Sprite):
	# Define init function (main)
	def __init__ (self, pos = (0, 0)):
		# Create sprite
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface ((20, 20)).convert()
		self.pos = pos
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect(center = self.pos)
		self.speed_x = 0
		self.speed_y = 0

	# Invert Y movement
	def change_y (self):
		self.speed_y *= -1

	# Invert X movement
	def change_x (self):
		self.speed_x *= -1

	# Start ball movement
	def start (self, speed_x, speed_y):
		self.speed_x = speed_x
		self.speed_y = speed_y

	# Stop ball movement
	def stop (self):
		self.speed_x = 0
		self.speed_y = 0

	# Reset ball position
	def reset (self):
		self.rect = self.image.get_rect (center = self.pos)

	# Update ball position
	def update (self):
		self.rect.move_ip (self.speed_x, self.speed_y)
