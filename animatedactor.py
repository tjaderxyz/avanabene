# coding: utf-8

import os, pygame, geral, pessoa

class AnimatedActor(pessoa.Pessoa):
	def __init__(self, id, pos, colisao, controls, frames, size):
		pessoa.Pessoa.__init__(self, id, pos, colisao, frames, size)
		self.controls = controls

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		w = int(node.getAttribute('w'))
		h = int(node.getAttribute('h'))
		controles = tuple(getattr(pygame, tecla) for tecla in node.getAttribute('controles').split(','))
		frames = [int(i) for i in node.getAttribute('frames').split(',')]
		try:
			colisao = [int(i) for i in node.getAttribute('colisao').split(',')]
		except:
			colisao = None
		ator = AnimatedActor(id, (x, y), colisao, controles, frames, (w, h))
		return ator

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

