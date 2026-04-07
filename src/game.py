import pygame

from .config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill(BG_COLOR)

			pygame.display.flip()

			self.clock.tick(FPS)

		pygame.quit()