# coding: utf-8

import os, pygame

class Actor:
	def __init__(self, id, controls):
		self.sprite = pygame.image.load(os.path.join('images', id))
		self.sprite = pygame.transform.scale(self.sprite, [4 * i for i in self.sprite.get_rect()][2:]).convert_alpha()
		self.pos = [0, 0]
		self.controls = controls
		self.eventtime = True
		self.speed = [0, 0]
		self.eventqueue = []

	def rect(self):
		return self.pos + [i for i in self.sprite.get_rect()]

	def render(self, screen):
		screen.blit(self.sprite, self.pos)

	def input(self, events):
		self.eventqueue += [i for i in events if i.type in (pygame.KEYUP, pygame.KEYDOWN) and i.key in self.controls]
		if self.eventtime:
			while self.eventqueue:
				event = self.eventqueue.pop()
				if event.type == pygame.KEYDOWN:
					if event.key == self.controls[0]:
						self.speed[0] -= 2
					if event.key == self.controls[1]:
						self.speed[0] += 2
					if event.key == self.controls[2]:
						self.speed[1] -= 2
					if event.key == self.controls[3]:
						self.speed[1] += 2
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

