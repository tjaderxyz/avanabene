# coding: utf-8

import os, pygame, object, random, geral

class Pessoa(object.Object):
	def __init__(self, id, pos, colisao, frames, size):
		self.sprites = []
		spritesheet = pygame.image.load(os.path.join('images', 'sh_' + id + '.png'))
		spritesheet = pygame.transform.scale(spritesheet, [geral.px * i for i in spritesheet.get_rect()][2:]).convert_alpha()
		for y, nframes in zip(range(4), frames):
			spritesdir = []
			for x in range(nframes):
				rect = [(size[0] + 1) * x, (size[1] + 1) * y, size[0], size[1]]
				rect = [geral.px * i for i in rect]
				spritesdir.append(spritesheet.subsurface(rect))
			self.sprites.append(spritesdir)
		self.pos = pos
		self.colisao = colisao
		self.eventtime = True
		self.speed = [0, 0]
		self.eventqueue = []
		self.direction = 0
		self.frameswalkinginthisdirection = 0

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		w = int(node.getAttribute('w'))
		h = int(node.getAttribute('h'))
		frames = [int(i) for i in node.getAttribute('frames').split(',')]
		try:
			colisao = [int(i) for i in node.getAttribute('colisao').split(',')]
		except:
			colisao = None
		pessoa = Pessoa(id, (x, y), colisao, frames, (w, h))
		return pessoa

	def get_rect(self):
		return [i / geral.px for i in self.sprites[0][0].get_rect()]

	def set_direction(self, direction):
		if self.direction != [0, 1, 3, 2][direction]:
			self.direction = [0, 1, 3, 2][direction]
			self.frameswalkinginthisdirection = 0

	def render(self, screen):
		self.frameswalkinginthisdirection += 1
		if self.speed[0] < 0 and self.speed[1] == 0:
			self.set_direction(0)
		elif self.speed[0] > 0 and self.speed[1] == 0:
			self.set_direction(1)
		elif self.speed[0] == 0 and self.speed[1] < 0:
			self.set_direction(2)
		elif self.speed[0] == 0 and self.speed[1] > 0:
			self.set_direction(3)
		elif self.speed[0] == 0 == self.speed[1]:
			self.frameswalkinginthisdirection = 0

		v = 12
		nframe = ((self.frameswalkinginthisdirection + v-1) / v) % len(self.sprites[self.direction])
		pos = (self.pos[0] * geral.px,
		       (geral.lheight - self.pos[1] - self.get_rect()[3]) * geral.px)
		screen.blit(self.sprites[self.direction][nframe], pos)

	def input(self, events):
		if random.random() > 0.99:
			if self.speed == [0, 0]:
				self.speed = [random.choice((-.5, 0, .5)), random.choice((-.5, 0, .5))]
				if self.speed[0] < 0:
					self.set_direction(0)
				if self.speed[0] > 0:
					self.set_direction(1)
				if self.speed[1] < 0:
					self.set_direction(2)
				if self.speed[1] > 0:
					self.set_direction(3)
			else:
				self.speed = [0, 0]
		if self.speed != [0, 0]:
			if random.random() > 0.95:
				self.speed[0] = random.choice((-.5, 0, .5))
				if self.speed[0] < 0:
					self.set_direction(0)
				if self.speed[0] > 0:
					self.set_direction(1)
			if random.random() > 0.95:
				self.speed[1] = random.choice((-.5, 0, .5))
				if self.speed[1] < 0:
					self.set_direction(2)
				if self.speed[1] > 0:
					self.set_direction(3)
			if (self.pos[0] < 3 and self.speed[0] < 0) or \
			   (self.pos[0] > geral.lsize[0] - 3 - self.get_rect()[2] and self.speed[0] > 0):
				self.speed[0] = -self.speed[0]
			if (self.pos[1] < 3 and self.speed[1] < 0) or \
			   (self.pos[1] > geral.lsize[1] - 3 - self.get_rect()[3] and self.speed[1] > 0):
				self.speed[1] = -self.speed[1]

	def update(self, tela):
		self.eventtime = not self.eventtime
		speed = self.speed
		if (self.colisao is not None):
		    speed = tela.podemover(speed, self)
		self.pos = [sum(i) for i in zip(self.pos, speed)]
