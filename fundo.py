# coding: utf-8

import random, pygame, os, xml.dom

import geral, object, tile

class Fundo:
	def __init__(self):
		self.coisasadesenhar = []
		self.coisasacolidir = []

	@staticmethod
	def XML(node):
		tipo = node.getAttribute('tipo')
		tela = node.parentNode
		x = int(tela.getAttribute('x'))
		y = int(tela.getAttribute('y'))
		fundo = Fundo()
		if tipo == 'flores':
			fundo.fundo = gerafundoflores((x, y))
		elif tipo == 'ladrilhado':
			imagem = node.getAttribute('imagem')
			fundo.fundo = gerafundoladrilhado(imagem, (x, y))
		elif tipo == '':
			fundo.fundo = pygame.Surface(geral.size)
		else:
			raise Exception
		for elemento in node.childNodes:
			if elemento.nodeType != xml.dom.Node.ELEMENT_NODE:
				continue
			elif elemento.tagName == 'objeto':
				o = object.Object.XML(elemento)
				fundo.coisasadesenhar.append(o)
				if o.colisao is not None:
					fundo.coisasacolidir.append(o)
			elif elemento.tagName == 'tile':
				t = tile.Tile.XML(elemento)
				fundo.coisasadesenhar.append(t)
			else:
				raise Exception
		return fundo

	def render(self, screen):
		screen.blit(self.fundo, (0, 0))
		for coisa in self.coisasadesenhar:
			coisa.render(screen)

RandomFundo = random.Random()

def gerafundoflores(tela):
	seed = 0x345678
	for item in (hash(geral.seed), tela[0], tela[1]):
		seed = (1000003 * seed) ^ item
	seed = seed ^ 3
	RandomFundo.seed(seed)
	pasto = pygame.image.load(os.path.join('imagens', 'tiles', 'grama.png'))
	flor = pygame.image.load(os.path.join('imagens', 'tiles', 'gramaflor.png'))
	pasto = pygame.transform.scale(pasto, [int(geral.px * i) for i in pasto.get_rect()][2:]).convert_alpha()
	pastorect = pasto.get_rect()
	flor = pygame.transform.scale(flor, [int(geral.px * i) for i in flor.get_rect()][2:]).convert_alpha()
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
	ladrilho = pygame.image.load(os.path.join('imagens', 'tiles', imagem + '.png'))
	ladrilho = pygame.transform.scale(ladrilho, [int(geral.px * i) for i in ladrilho.get_rect()][2:]).convert_alpha()
	ladrilhorect = ladrilho.get_rect()
	fundo = pygame.Surface(geral.size)

	for i in range(0, geral.size[0], ladrilhorect[2]):
		for j in range(0, geral.size[1], ladrilhorect[3]):
			fundo.blit(ladrilho, (i, j))

	return fundo

