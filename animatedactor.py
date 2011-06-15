# coding: utf-8

import os, pygame, geral, pessoa

class AnimatedActor(pessoa.Pessoa):
	def __init__(self, id, controls, frames, size):
		pessoa.Pessoa.__init__(self, id, frames, size)
		self.controls = controls

	def input(self, events):
		self.eventqueue += [i for i in events if i.type in (pygame.KEYUP, pygame.KEYDOWN) and i.key in self.controls]
		if self.eventtime:
			while self.eventqueue:
				event = self.eventqueue.pop()
				if event.type == pygame.KEYDOWN:
					if event.key == self.controls[0]:
						self.speed[0] -= .5
						self.set_direction(0)
					if event.key == self.controls[1]:
						self.speed[0] += .5
						self.set_direction(1)
					if event.key == self.controls[2]:
						self.speed[1] -= .5
						self.set_direction(2)
					if event.key == self.controls[3]:
						self.speed[1] += .5
						self.set_direction(3)
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

