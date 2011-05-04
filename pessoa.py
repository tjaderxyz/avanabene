# coding: utf-8

import os, pygame, object, random

class Pessoa(object.Object):
	def __init__(self, id, frames):
		self.sprites = []
		for direcao, nframes in zip(('esq', 'dir', 'cima', 'baixo'), frames):
			sprites = (pygame.image.load(os.path.join('images', 's_' + id + '_' + direcao + str(i) + '.png')) for i in range(nframes))
			sprites = [pygame.transform.scale(sprite, [4 * i for i in sprite.get_rect()][2:]).convert_alpha() for sprite in sprites]
			self.sprites.append(sprites)
		self.pos = [0, 0]
		self.eventtime = True
		self.speed = [0, 0]
		self.eventqueue = []
		self.direction = 0
		self.frameswalkinginthisdirection = 0

	def get_rect(self):
		return self.sprites[0][0].get_rect()

	def set_direction(self, direction):
		if self.direction != direction:
			self.direction = direction
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
		screen.blit(self.sprites[self.direction][nframe], self.pos)

	def input(self, events):
		pass

	def update(self):
		if random.random() > 0.99:
			if self.speed == [0, 0]:
				self.speed = [random.choice((-2, 0, 2)), random.choice((-2, -1, 0, 1, 2))]
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
				self.speed[0] = random.choice((-2, 0, 2))
				if self.speed[0] < 0:
					self.set_direction(0)
				if self.speed[0] > 0:
					self.set_direction(1)
			if random.random() > 0.95:
				self.speed[1] = random.choice((-2, 0, 2))
				if self.speed[1] < 0:
					self.set_direction(2)
				if self.speed[1] > 0:
					self.set_direction(3)
			if (self.pos[0] < 10 and self.speed[0] < 0) or \
			   (self.pos[0] > 630 - self.get_rect()[2] and self.speed[0] > 0):
				self.speed[0] = -self.speed[0]
			if (self.pos[1] < 10 and self.speed[1] < 0) or \
			   (self.pos[1] > 470 - self.get_rect()[3] and self.speed[1] > 0):
				self.speed[1] = -self.speed[1]
		self.pos = [sum(i) for i in zip(self.pos, self.speed)]

