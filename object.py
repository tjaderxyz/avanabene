# coding: utf-8

import os, pygame, geral

class Object:
	def __init__(self, id):
		self.sprite = pygame.image.load(os.path.join('images', 'o_' + id + '.png'))
		self.sprite = pygame.transform.scale(self.sprite, [geral.px * i for i in self.sprite.get_rect()][2:]).convert_alpha()
		self.pos = [0, 0]
		self.speed = [0, 0]
		self.eventqueue = []
		self.direction = 0

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		object = Object(id)
		object.pos = x, y
		return object

	def get_rect(self):
		return [i / geral.px for i in self.sprite.get_rect()]

	def render(self, screen):
		screen.blit(self.sprite, [i * geral.px for i in self.pos])

	def input(self, events):
		pass

	def update(self):
		pass

