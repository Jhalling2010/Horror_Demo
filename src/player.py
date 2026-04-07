import pygame

class Player:
	def __init__(self, game):
		self.game = game
		self.rect = pygame.Rect(375, 275, 50, 50)
		self.color = "black"

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)