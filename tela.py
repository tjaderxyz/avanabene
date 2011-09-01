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
				t = Tela.XML(elemento, self)
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
			self.telas[index] = Tela(index, self)
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
	def __init__(self, pos, telas):
		self.coisasaupdatear = []
		self.coisasainputear = []
		self.coisasadesenhar = []
		self.coisasacolidir = []
		self.telas = telas
		self.pos = pos

	@staticmethod
	def XML(node, telas):
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		tela = Tela((x, y), telas)
		for elemento in node.childNodes:
			if elemento.nodeType != xml.dom.Node.ELEMENT_NODE:
				continue
			if elemento.tagName == 'fundo':
				tela.fundo = fundo.Fundo.XML(elemento)
			elif elemento.tagName == 'objeto':
				o = object.Object.XML(elemento)
				tela.coisasadesenhar.append(o)
				if o.colisao is not None:
					tela.coisasacolidir.append(o)
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
		caixa = [pos[0] + objeto.colisao[0],
		         pos[1] + objeto.colisao[1],
		         pos[0] + objeto.colisao[0] + objeto.colisao[2],
		         pos[1] + objeto.colisao[1] + objeto.colisao[3]]
		for coisa in self.telas.coisasacolidir + self.coisasacolidir:
			if coisa == objeto:
				continue
			caixac = [coisa.pos[0] + coisa.colisao[0],
			          coisa.pos[1] + coisa.colisao[1],
			          coisa.pos[0] + coisa.colisao[0] + coisa.colisao[2],
			          coisa.pos[1] + coisa.colisao[1] + coisa.colisao[3]]
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

