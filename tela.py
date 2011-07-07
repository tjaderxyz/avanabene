# coding: utf-8

import xml.dom.minidom, random, object, geral, pygame, pessoa, os, fundo, animatedactor

class Telas:
	def __init__(self, arq, atores):
		self.coisasaupdatear = [i for i in atores]
		self.coisasainputear = [i for i in atores]
		self.coisasadesenhar = [i for i in atores]
		self.coisasacolidir = [i for i in atores]
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
				t.coisasacolidir += self.coisasacolidir
				self.telas[t.pos] = t
			elif elemento.tagName == 'ator':
				a = animatedactor.AnimatedActor.XML(elemento)
				self.coisasainputear.append(a)
				self.coisasaupdatear.append(a)
				self.coisasadesenhar.append(a)
				if a.colisao:
					self.coisasacolidir.append(a)
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

	def input(self, events):
		for coisa in self.coisasainputear:
			coisa.input(events)

	def update(self, tela):
		for coisa in self.coisasaupdatear:
			coisa.update(tela)

class Tela:
	def __init__(self, pos):
		self.coisasaupdatear = []
		self.coisasainputear = []
		self.coisasadesenhar = []
		self.coisasacolidir = []
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
				if o.colisao is not None:
					self.coisasacolidir.append(o)
			elif elemento.tagName == 'pessoa':
				p = pessoa.Pessoa.XML(elemento)
				tela.coisasainputear.append(p)
				tela.coisasaupdatear.append(p)
				tela.coisasadesenhar.append(p)
				if p.colisao:
					self.coisasacolidir.append(p)
			else:
				raise Exception
		return tela

	def podemover(self, pos, objeto):
		caixa = [sum(i) for i in zip(pos + pos, objeto.colisao)]
		print self.coisasacolidir
		for coisa in self.coisasacolidir:
			if coisa == objeto:
				continue
			caixac = [sum(i) for i in zip(coisa.pos + coisa.pos, coisa.colisao)]
			print caixa, caixac
			if (caixa[0] < caixac[2] and caixa[2] > caixac[0]
			    and caixa[1] < caixac[3] and caixa[3] > caixac[1]):
				return False
		return True

	def input(self, events):
		for coisa in self.coisasainputear:
			coisa.input(events)

	def update(self):
		for coisa in self.coisasaupdatear:
			coisa.update(self)

