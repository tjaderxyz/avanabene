# coding: utf-8

import os, pygame

class Object:
	def __init__(self, id):
		self.sprite = pygame.image.load(os.path.join('images', 'o_' + id + '.png'))
		self.sprite = pygame.transform.scale(self.sprite, [4 * i for i in self.sprite.get_rect()][2:]).convert_alpha()
		self.pos = [0, 0]
		self.speed = [0, 0]
		self.eventqueue = []
		self.direction = 0

	def get_rect(self):
		return self.sprite.get_rect()

	def render(self, screen):
		screen.blit(self.sprite, self.pos)

	def input(self, events):
		pass

	def update(self):
		pass

