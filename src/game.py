import pygame

from .config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR
from .player import Player

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.player = Player(self)

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill(BG_COLOR)

			self.player.draw(self.screen)

			pygame.display.flip()

			self.clock.tick(FPS)

		pygame.quit()