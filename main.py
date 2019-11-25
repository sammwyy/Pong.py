import os, sys, pygame

from ball import Ball
from pad import Pad
from score import Score

from random import randint

def main ():
	pygame.init()

	size = width, height = 800, 600
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption ('Pong')

	ball_launched = False
	game_started = False

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

	except pygame.error as e:
		print ('Error, graphic file not found: ', filename)
		raise SystemExit(str(e))

	pad_left = Pad((width / 12, height / 4))
	pad_right = Pad((5.5 * width / 6, 3 * height / 4))

	ball = Ball (( width / 2, height / 2))

	if not pygame.font:
		raise SystemExit('Pygame does not support fonts')

	try:
		filename = os.path.join(os.path.dirname(__file__), 'fonts', 'wendy.ttf')
		font = pygame.font.Font(filename, 90)

	except pygame.error as e:
		print ('Cannot load font: ', filename)
		raise SystemExit(str(e))

	left_score = Score(font, (width / 3, height / 8))
	right_score = Score(font, (2 * width / 3, height / 8))

	sprites = pygame.sprite.Group(pad_left, pad_right, ball, left_score, right_score)

	clock = pygame.time.Clock()
	fps = 60

	pygame.key.set_repeat(1, 1000/fps)

	top = pygame.Rect(0, 0, width, 5)
	bottom = pygame.Rect(0, height - 5, width, 5)
	left = pygame.Rect(0, 0, 5, height)
	right = pygame.Rect(width - 5, 0, 5, height)

	while 1:

		if game_started == True:
			clock.tick(fps)

			pad_left.stop()
			pad_right.stop()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
					pad_left.move_up()

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
					pad_left.move_down()

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
					pad_right.move_up()

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
					pad_right.move_down()

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					if (ball_launched == False):
						ball_launched = True
						ball.start(randint(3, 6), randint(3, 6))

			if (ball.rect.colliderect(top) or ball.rect.colliderect(bottom)):
				ball.change_y()

			elif (ball.rect.colliderect(pad_left.rect) or ball.rect.colliderect(pad_right.rect)):
				ball.change_x()

			if ball.rect.colliderect (left):
				ball_launched = False
				right_score.score_up()
				ball.reset()
				ball.stop()

			elif ball.rect.colliderect (right):
				ball_launched = False
				left_score.score_up()
				ball.reset()
				ball.stop()

			sprites.update()

			screen.blit(background, (0, 0))
			sprites.draw(screen)
			pygame.display.flip()

			screen_rect = screen.get_rect().inflate(0, -10)
			pad_left.rect.clamp_ip(screen_rect)
			pad_right.rect.clamp_ip(screen_rect)

		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					game_started = True

			screen.blit(menu_background, (0, 0))
			pygame.display.flip()

if __name__ == '__main__':
	main()