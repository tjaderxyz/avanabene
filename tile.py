# coding: utf-8

import os, pygame, geral

class Tile:
	def __init__(self, id, pos, size):
		self.sprite = pygame.image.load(os.path.join('images', 't_' + id + '.png'))
		self.sprite = pygame.transform.scale(self.sprite, [geral.px * i for i in self.sprite.get_rect()][2:]).convert_alpha()
		self.pos = pos
		self.size = size
		ladrilhorect = self.sprite.get_rect()
		self.spritemesmo = pygame.Surface((self.size[0] * ladrilhorect[2], self.size[1] * ladrilhorect[3])).convert_alpha()
		for i in range(size[0]):
			for j in range(size[1]):
				self.spritemesmo.blit(self.sprite, (i * ladrilhorect[2], j * ladrilhorect[3]))

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		try:
			w = int(node.getAttribute('w'))
		except ValueError:
			w = 1
		try:
			h = int(node.getAttribute('h'))
		except ValueError:
			h = 1
		tile = Tile(id, (x, y), (w, h))
		return tile

	def get_rect(self):
		return [i / geral.px for i in self.sprite.get_rect()]

	def render(self, screen):
		screen.blit(self.spritemesmo, [i * geral.px for i in self.pos])

	def input(self, events):
		pass

	def update(self):
		pass

