
import xml.parsers.expat, random, object, geral, pygame, pessoa

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
			return Tela({})

RandomFundo = random.Random()
def gerafundo(tela):
	RandomFundo.seed((geral.seed, tela[0], tela[1]))
	if tela[0] == -1 and tela[1] == 0:
		pasto = pygame.image.load("images/t_deserto.png")
		fro = pygame.image.load("images/t_deserto.png")
	else:
		pasto = pygame.image.load("images/t_grama.png")
		fro = pygame.image.load("images/t_gramaflor.png")
	pasto = pygame.transform.scale(pasto, [geral.px * i for i in pasto.get_rect()][2:]).convert_alpha()
	pastorect = pasto.get_rect()
	fro = pygame.transform.scale(fro, [geral.px * i for i in fro.get_rect()][2:]).convert_alpha()
	fundo = pygame.Surface(geral.size)

	for i in range(0, geral.size[0], pastorect[2]):
		for j in range(0, geral.size[1], pastorect[3]):
			if RandomFundo.random() > 0.92:
				fundo.blit(fro, (i, j))
			else:
				fundo.blit(pasto, (i, j))

	return fundo

class Tela:
	def __init__(self, atr):
		self.coisasadesenhar = []
		self.coisasaupdatear = []
		self.fundo = gerafundo((int(atr['x']), int(atr['y'])))
	def insere(self, tipo, atr):
		if tipo == 'objeto':
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

