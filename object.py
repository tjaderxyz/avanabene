# coding: utf-8

import os, pygame, geral

class Object:
	def __init__(self, id, frames, size, animado = True):
		self.pos = [0, 0]
		self.frames = 0
		spritesheet = pygame.image.load(os.path.join('images', 'o_' + id + '.png'))
		spritesheet = pygame.transform.scale(spritesheet, [geral.px * i for i in spritesheet.get_rect()][2:]).convert_alpha()
		if not animado:
			self.sprites = [spritesheet]
			return
		self.sprites = []
		for x in range(frames):
			rect = [(size[0] + 1) * x, 0, size[0], size[1]]
			rect = [geral.px * i for i in rect]
			self.spritesdir.append(spritesheet.subsurface(rect))

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		try:
			frames = int(node.getAttribute('frames').split(','))
			w = int(node.getAttribute('w'))
			h = int(node.getAttribute('h'))
			animado = True
		except:
			frames = 1
			w = 0
			h = 0
			animado = False
		object = Object(id, frames, (w, h), animado)
		object.pos = x, y
		return object

	def get_rect(self):
		return [i / geral.px for i in self.sprites[0].get_rect()]

	def render(self, screen):
		v = 12
		nframe = ((self.frames + v-1) / v) % len(self.sprites)
		screen.blit(self.sprites[nframe], [i * geral.px for i in self.pos])

	def input(self, events):
		pass

	def update(self):
		pass

