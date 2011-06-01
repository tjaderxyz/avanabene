# coding: utf-8

import os, pygame, geral

class Tile:
	def __init__(self, id, pos, size):
		self.sprite = pygame.image.load(os.path.join('images', 't_' + id + '.png'))
		self.sprite = pygame.transform.scale(self.sprite, [geral.px * i for i in self.sprite.get_rect()][2:]).convert_alpha()
		self.pos = pos
		self.size = size
		self.spritemesmo = pygame.Surface([i * geral.px for i in self.size])
		ladrilhorect = self.sprite.get_rect()
		print [i * geral.px for i in self.size]
		for i in range(0, size[0] * geral.px, ladrilhorect[2]):
			for j in range(0, size[1] * geral.px, ladrilhorect[3]):
				self.spritemesmo.blit(self.sprite, (i, j))

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		w = int(node.getAttribute('w'))
		h = int(node.getAttribute('h'))
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

