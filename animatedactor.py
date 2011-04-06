# coding: utf-8

import os, pygame

class AnimatedActor:
	def __init__(self, id, controls, frames):
		self.sprites = []
		for direcao, nframes in zip(('esq', 'dir', 'cima', 'baixo'), frames):
			sprites = (pygame.image.load(os.path.join('images', 's_' + id + '_' + direcao + str(i) + '.png')) for i in range(nframes))
			sprites = [pygame.transform.scale(sprite, [4 * i for i in sprite.get_rect()][2:]).convert_alpha() for sprite in sprites]
			self.sprites.append(sprites)
		self.pos = [0, 0]
		self.controls = controls
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
		self.eventqueue += [i for i in events if i.type in (pygame.KEYUP, pygame.KEYDOWN) and i.key in self.controls]
		if self.eventtime:
			while self.eventqueue:
				event = self.eventqueue.pop()
				if event.type == pygame.KEYDOWN:
					if event.key == self.controls[0]:
						self.speed[0] -= 2
						self.set_direction(0)
					if event.key == self.controls[1]:
						self.speed[0] += 2
						self.set_direction(1)
					if event.key == self.controls[2]:
						self.speed[1] -= 2
						self.set_direction(2)
					if event.key == self.controls[3]:
						self.speed[1] += 2
						self.set_direction(3)
				elif event.type == pygame.KEYUP:
					if event.key == self.controls[0]:
						self.speed[0] += 2
					if event.key == self.controls[1]:
						self.speed[0] -= 2
					if event.key == self.controls[2]:
						self.speed[1] += 2
					if event.key == self.controls[3]:
						self.speed[1] -= 2
		self.eventtime = not self.eventtime

	def update(self):
		self.pos = [sum(i) for i in zip(self.pos, self.speed)]

