# coding: utf-8

import os, pygame, geral

class Actor:
	def __init__(self, id, controls):
		self.sprites = (pygame.image.load(os.path.join('images', 's_' + id + '_' + direcao + '.png')) for direcao in ('esq', 'dir', 'cima', 'baixo'))
		self.sprites = [pygame.transform.scale(sprite, [geral.px * i for i in sprite.get_rect()][2:]).convert_alpha() for sprite in self.sprites]
		self.pos = [0, 0]
		self.controls = controls
		self.eventtime = True
		self.speed = [0, 0]
		self.eventqueue = []
		self.direction = 0

	def get_rect(self):
		return [i / geral.px for i in self.sprites[0].get_rect()]

	def render(self, screen):
		if self.speed[0] < 0 and self.speed[1] == 0:
			self.direction = 0
		if self.speed[0] > 0 and self.speed[1] == 0:
			self.direction = 1
		if self.speed[0] == 0 and self.speed[1] < 0:
			self.direction = 2
		if self.speed[0] == 0 and self.speed[1] > 0:
			self.direction = 3
		screen.blit(self.sprites[self.direction], [i * geral.px for i in self.pos])

	def input(self, events):
		self.eventqueue += [i for i in events if i.type in (pygame.KEYUP, pygame.KEYDOWN) and i.key in self.controls]
		if self.eventtime:
			while self.eventqueue:
				event = self.eventqueue.pop()
				if event.type == pygame.KEYDOWN:
					if event.key == self.controls[0]:
						self.speed[0] -= .5
						self.direction = 0
					if event.key == self.controls[1]:
						self.speed[0] += .5
						self.direction = 1
					if event.key == self.controls[2]:
						self.speed[1] -= .5
						self.direction = 2
					if event.key == self.controls[3]:
						self.speed[1] += .5
						self.direction = 3
				elif event.type == pygame.KEYUP:
					if event.key == self.controls[0]:
						self.speed[0] += .5
					if event.key == self.controls[1]:
						self.speed[0] -= .5
					if event.key == self.controls[2]:
						self.speed[1] += .5
					if event.key == self.controls[3]:
						self.speed[1] -= .5
		self.eventtime = not self.eventtime

	def update(self):
		self.pos = [sum(i) for i in zip(self.pos, self.speed)]

