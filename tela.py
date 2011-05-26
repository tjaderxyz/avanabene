#! /usr/bin/env python
# coding: utf-8

import xml.parsers.expat, random, object, geral, pygame, pessoa, os

class Telas:
	def __init__(self, arq):
		self.tela = None
		self.telas = {}
		p = xml.parsers.expat.ParserCreate()
		p.StartElementHandler = self.elemento
		p.Parse(open(arq).read())
	def elemento(self, nome, atr):
		if nome == 'tela':
			self.tela = int(atr['x']), int(atr['y'])
			self.telas[self.tela] = Tela(atr)
		else:
			if self.tela is not None:
				self.telas[self.tela].insere(nome, atr)
	def __getitem__(self, index):
		try:
			return self.telas[index]
		except KeyError:
			self.telas[index] = Tela({'x': str(index[0]), 'y': str(index[1])})
			self.telas[index].fundo = gerafundoflores(index)
			return self.telas[index]

RandomFundo = random.Random()

def gerafundoflores(tela):
	RandomFundo.seed((geral.seed, tela[0], tela[1]))
	pasto = pygame.image.load("images/t_grama.png")
	flor = pygame.image.load("images/t_gramaflor.png")
	pasto = pygame.transform.scale(pasto, [geral.px * i for i in pasto.get_rect()][2:]).convert_alpha()
	pastorect = pasto.get_rect()
	flor = pygame.transform.scale(flor, [geral.px * i for i in flor.get_rect()][2:]).convert_alpha()
	fundo = pygame.Surface(geral.size)

	for i in range(0, geral.size[0], pastorect[2]):
		for j in range(0, geral.size[1], pastorect[3]):
			if RandomFundo.random() > 0.92:
				fundo.blit(flor, (i, j))
			else:
				fundo.blit(pasto, (i, j))

	return fundo

def gerafundoladrilhado(imagem, tela):
	RandomFundo.seed((geral.seed, tela[0], tela[1]))
	ladrilho = pygame.image.load(os.path.join('images', 't_' + imagem + '.png'))
	ladrilho = pygame.transform.scale(ladrilho, [geral.px * i for i in ladrilho.get_rect()][2:]).convert_alpha()
	ladrilhorect = ladrilho.get_rect()
	fundo = pygame.Surface(geral.size)

	for i in range(0, geral.size[0], ladrilhorect[2]):
		for j in range(0, geral.size[1], ladrilhorect[3]):
			fundo.blit(ladrilho, (i, j))

	return fundo

class Tela:
	def __init__(self, atr):
		self.coisasadesenhar = []
		self.coisasaupdatear = []
		self.pos = int(atr['x']), int(atr['y'])
	def insere(self, tipo, atr):
		if tipo == 'fundo':
			if atr['tipo'] == 'flores':
				self.fundo = gerafundoflores(self.pos)
			elif atr['tipo'] == 'ladrilhado':
				self.fundo = gerafundoladrilhado(atr['imagem'], self.pos)
		elif tipo == 'objeto':
			o = object.Object(atr['id'])
			o.pos = int(atr['x']), int(atr['y'])
			self.coisasadesenhar.append(o)
		elif tipo == 'pessoa':
			p = pessoa.Pessoa(atr['id'], [int(i) for i in atr['frames'].split(',')], (int(atr['w']), int(atr['h'])))
			p.pos = int(atr['x']), int(atr['y'])
			self.coisasadesenhar.append(p)
			self.coisasaupdatear.append(p)

	def update(self):
		for coisa in self.coisasaupdatear:
			coisa.update()

