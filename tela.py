# coding: utf-8

import xml.dom.minidom, random, object, geral, pygame, pessoa, os, fundo

class Telas:
	def __init__(self, arq):
		self.tela = None
		self.telas = {}
		self.xml = xml.dom.minidom.parse(arq)
		mundo = self.xml.documentElement
		if mundo.tagName != 'mundo':
			raise Exception
		for elemento in mundo.childNodes:
			if elemento.nodeType != xml.dom.Node.ELEMENT_NODE:
				continue
			if elemento.tagName == 'tela':
				t = Tela.XML(elemento)
				self.telas[t.pos] = Tela.XML(elemento)
			else:
				raise Exception
	def __getitem__(self, index):
		try:
			return self.telas[index]
		except KeyError:
			self.telas[index] = Tela(index)
			self.telas[index].fundo = fundo.Fundo()
			self.telas[index].fundo.fundo = fundo.gerafundoflores(index)
			return self.telas[index]

class Tela:
	def __init__(self, pos):
		self.coisasaupdatear = []
		self.coisasainputear = []
		self.coisasadesenhar = []
		self.pos = pos

	@staticmethod
	def XML(node):
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		tela = Tela((x, y))
		for elemento in node.childNodes:
			if elemento.nodeType != xml.dom.Node.ELEMENT_NODE:
				continue
			if elemento.tagName == 'fundo':
				tela.fundo = fundo.Fundo.XML(elemento)
			elif elemento.tagName == 'objeto':
				o = object.Object.XML(elemento)
				tela.coisasadesenhar.append(o)
			elif elemento.tagName == 'pessoa':
				p = pessoa.Pessoa.XML(elemento)
				tela.coisasainputear.append(p)
				tela.coisasaupdatear.append(p)
				tela.coisasadesenhar.append(p)
			else:
				raise Exception
		return tela

	def input(self, events):
		for coisa in self.coisasainputear:
			coisa.input(events)

	def update(self):
		for coisa in self.coisasaupdatear:
			coisa.update()

