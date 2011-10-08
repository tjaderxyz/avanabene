# coding: utf-8

import os, pygame

import geral

class Collision:
	def __init__(self, pos, colisao):
		self.pos = pos
		self.colisao = colisao

	@staticmethod
	def XML(node):
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		colisao = [[int(i) for i in node.getAttribute('colisao').split(',')]]
		collision = Collision((x, y), colisao)
		return collision

	def get_rect(self):
		return [i / geral.px for i in self.sprites[0].get_rect()]

