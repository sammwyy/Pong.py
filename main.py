# Pong.py coded by Sammwy
# https://github.com/sammwyy/Pong.py
# Twitter: @Sammwy_

# Import python's libs and pygame
import os, sys, pygame
from random import randint

# Imports of game's modules
from ball import Ball
from pad import Pad
from score import Score

# Define the main function
def main ():
	# Init pygame library
	pygame.init()

	# Set window properties
	size = width, height = 800, 600
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption ('Pong')

	# Some utils booleans
	ball_launched = False
	game_started = False

	# Load graphics file (background and icon)
	try:
		bg_file = os.path.join(os.path.dirname(__file__), 'graphics', 'background.png')
		background = pygame.image.load(bg_file)
		background = background.convert()

		menu_bg_file = os.path.join(os.path.dirname(__file__), 'graphics', 'title.png')
		menu_background = pygame.image.load(menu_bg_file)
		menu_background = menu_background.convert()

		icon_file = os.path.join(os.path.dirname(__file__), 'graphics', 'icon.png')
		icon = pygame.image.load(icon_file)
		pygame.display.set_icon(icon)

	# Catch exceptions
	except pygame.error as e:
		print ('Error, graphic file not found: ', filename)
		raise SystemExit(str(e))

	# Define left pad (player one)
	pad_left = Pad((width / 12, height / 4))
	# Define right pad (player two)
	pad_right = Pad((5.5 * width / 6, 3 * height / 4))
	# Define ball
	ball = Ball (( width / 2, height / 2))

	# If pygame does not support fonts
	if not pygame.font:
		# Close the game returning this error:
		raise SystemExit('Pygame does not support fonts')

	# Try to load font file
	try:
		filename = os.path.join(os.path.dirname(__file__), 'fonts', 'wendy.ttf')
		font = pygame.font.Font(filename, 90)

	# Catch exception
	except pygame.error as e:
		print ('Cannot load font: ', filename)
		raise SystemExit(str(e))

	# Define left score (player one points)
	left_score = Score(font, (width / 3, height / 8))
	# Define right score (player two points)
	right_score = Score(font, (2 * width / 3, height / 8))

	# Group all sprites
	sprites = pygame.sprite.Group(pad_left, pad_right, ball, left_score, right_score)

	# Set the pygame's clock and fps
	clock = pygame.time.Clock()
	fps = 60
	pygame.key.set_repeat(1, 1000/fps)

	# Set the corners
	top = pygame.Rect(0, 0, width, 5)
	bottom = pygame.Rect(0, height - 5, width, 5)
	left = pygame.Rect(0, 0, 5, height)
	right = pygame.Rect(width - 5, 0, 5, height)

	# infinite Loop
	while 1:
		# Set the fps for clock
		clock.tick(fps)
		
		# If the game has started
		if game_started == True:
			
			# Stop movement of both pads
			pad_left.stop()
			pad_right.stop()

			# For each event
			for event in pygame.event.get():
				# If event is equal to QUIT
				if event.type == pygame.QUIT:
					# Closse the game
					pygame.quit()
					return

				# If event is equal to KEYDOWN and the key is W move up player one
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
					pad_left.move_up()

				# Else if event is equal to KEYDOWN and the key is S move down player one
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
					pad_left.move_down()
				
				# Else if event is equal to KEYDOWN and the key is UP Arrow move up player two
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
					pad_right.move_up()

				# Else if event is equal to KEYDOWN and the key is DOWN Arrow move down player two	
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
					pad_right.move_down()

				# Else if event is equal to KEYDOWN and the key is SPACE, launch the ball
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					if (ball_launched == False):
						ball_launched = True
						ball.start(randint(3, 6), randint(3, 6))

			# if the ball reaches the Y limit point then it reverses its Y axis
			if (ball.rect.colliderect(top) or ball.rect.colliderect(bottom)):
				ball.change_y()

			# else if the ball touches a pad then it reverses its X axis
			elif (ball.rect.colliderect(pad_left.rect) or ball.rect.colliderect(pad_right.rect)):
				ball.change_x()

			# if the ball reaches the left edge X then player two gets a point and the ball restarts its position
			if ball.rect.colliderect (left):
				ball_launched = False
				right_score.score_up()
				ball.reset()
				ball.stop()
			
			# else if the ball reaches the right edge X then player one gets a point and the ball restarts its position
			elif ball.rect.colliderect (right):
				ball_launched = False
				left_score.score_up()
				ball.reset()
				ball.stop()

			# Update all sprites
			sprites.update()

			# Draw the game background
			screen.blit(background, (0, 0))
			sprites.draw(screen)
			pygame.display.flip()

			# Draw both pads
			screen_rect = screen.get_rect().inflate(0, -10)
			pad_left.rect.clamp_ip(screen_rect)
			pad_right.rect.clamp_ip(screen_rect)

		# Else if the game has not been started
		else:
			# For each event
			for event in pygame.event.get():
				# If event is QUIT then close the game
				if event.type == pygame.QUIT:
					pygame.quit()
					return
				
				# Else if event is KEYDOWN and key is RETURN then Start the game
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					game_started = True

			# Render title background
			screen.blit(menu_background, (0, 0))
			pygame.display.flip()

# Run main function
if __name__ == '__main__':
	main()
