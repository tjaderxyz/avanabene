#! /usr/bin/env python
# coding: utf-8

import os, sys, pygame, random, actor, animatedactor, object
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

fonte = pygame.font.Font('unifont-5.1.20080820.pcf', 16)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Aventuras de Ananias e Benevides') 

ananias = animatedactor.AnimatedActor('ananias', (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN), (2, 2, 4, 4))
benevides = animatedactor.AnimatedActor('benevides', (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s), (2, 2, 4, 4))
ananias.pos = (300, 188)
benevides.pos = (328, 188)

#casa = pygame.image.load(os.path.join('images', 'o_casa.png'))
#casa = pygame.transform.scale(casa, [4 * i for i in casa.get_rect()][2:]).convert_alpha()
#casa2 = pygame.image.load(os.path.join('images', 'o_casa2.png'))
#casa2 = pygame.transform.scale(casa2, [4 * i for i in casa2.get_rect()][2:]).convert_alpha()
duende = pygame.image.load(os.path.join('images', 's_duende_baixo0.png'))
duende = pygame.transform.scale(duende, [4 * i for i in duende.get_rect()][2:]).convert_alpha()
pirata = pygame.image.load(os.path.join('images', 's_pirata_baixo0.png'))
pirata = pygame.transform.scale(pirata, [4 * i for i in pirata.get_rect()][2:]).convert_alpha()
casebre = pygame.image.load(os.path.join('images', 'o_casebre2.png'))
casebre = pygame.transform.scale(casebre, [4 * i for i in casebre.get_rect()][2:]).convert_alpha()

casa = object.Object('casa')
casa.pos = (100, 90)
casa2 = object.Object('casa2')
casa2.pos = (200, 280)
casebre = object.Object('casebre')
casebre.pos = (400, 100)
#duende = actor.Object('duende')


try:
	pygame.mixer.music.load(os.path.join('music', 'lojinha song.mp3'))
	pygame.mixer.music.play(-1)
except:
	#não esquenta
	pass

def gerafundo(tela):
	pasto = pygame.image.load("images/t_grama.png")
	pasto = pygame.transform.scale(pasto, [4 * i for i in pasto.get_rect()][2:]).convert_alpha()
	pastorect = pasto.get_rect()
	fro = pygame.image.load("images/t_gramaflor.png")
	fro = pygame.transform.scale(fro, [4 * i for i in fro.get_rect()][2:]).convert_alpha()
	fundo = pygame.Surface(size)

	for i in range(0, size[0], pastorect[2]):
		for j in range(0, size[1], pastorect[3]):
			if random.random() > 0.92:
				fundo.blit(fro, (i, j))
			else:
				fundo.blit(pasto, (i, j))

	txt = fonte.render(repr(tela), False, (255, 255, 255))
#	txt = pygame.transform.scale(txt, [4 * i for i in txt.get_rect()][2:])
	fundo.blit(txt, (size[0] - txt.get_rect()[2] - 10, size[1] - txt.get_rect()[3] - 10))
	return fundo

tela = [0, 0]

fundo = gerafundo(tela)

titulo = fonte.render('Aventuras de Ananias e Benevides', False, (255, 255, 255))
titulo = pygame.transform.scale(titulo, [2 * i for i in titulo.get_rect()][2:])
splash = pygame.Surface(size)
splash.blit(titulo, [4 * i for i in (size[0] / 8 - titulo.get_rect()[2] / 8, size[1] / 8 - titulo.get_rect()[3] / 8)])
splash.set_alpha(255)
screen.blit(splash, (0, 0))
pygame.display.flip()
pygame.time.wait(2000)

tempo = pygame.time.Clock()

while True:
	events = pygame.event.get()
	ananias.input(events)
	benevides.input(events)
	for event in events:
		if event.type == pygame.QUIT \
		   or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()

	ananias.update()
	benevides.update()

	def mudatela(actor, outro):
		if not actor.eventtime:
			return
		if actor.pos[0] + actor.get_rect()[2] < 0:
			actor.pos[0] += size[0]
			outro.pos[0] = actor.pos[0]
			if outro.pos[1] > actor.pos[1]:
				outro.pos[1] = actor.pos[1] + actor.get_rect()[3]
			else:
				outro.pos[1] = actor.pos[1] - actor.get_rect()[3]
			tela[0] -= 1
			outro.set_direction(0)
		elif actor.pos[0] >= size[0]:
			actor.pos[0] -= size[0]
			outro.pos[0] = actor.pos[0]
			if outro.pos[1] > actor.pos[1]:
				outro.pos[1] = actor.pos[1] + actor.get_rect()[3]
			else:
				outro.pos[1] = actor.pos[1] - actor.get_rect()[3]
			tela[0] += 1
			outro.set_direction(1)
		elif actor.pos[1] + actor.get_rect()[3] < 0:
			actor.pos[1] += size[1]
			if outro.pos[0] > actor.pos[0]:
				outro.pos[0] = actor.pos[0] + actor.get_rect()[3]
			else:
				outro.pos[0] = actor.pos[0] - actor.get_rect()[3]
			outro.pos[1] = actor.pos[1]
			tela[1] -= 1
			outro.set_direction(2)
		elif actor.pos[1] >= size[1]:
			actor.pos[1] -= size[1]
			if outro.pos[0] > actor.pos[0]:
				outro.pos[0] = actor.pos[0] + actor.get_rect()[3]
			else:
				outro.pos[0] = actor.pos[0] - actor.get_rect()[3]
			outro.pos[1] = actor.pos[1]
			tela[1] += 1
			outro.set_direction(3)
		else:
			return
		global fundo
		fundo = gerafundo(tela)
		print tela

	mudatela(ananias, benevides)
	mudatela(benevides, ananias)

	screen.blit(fundo, (0, 0))

	coisasadesenhar = [ananias, benevides]
	if tela[0] == -1 and tela[1] == 0:
		coisasadesenhar += [casa, casa2]
	if tela[0] == 0 and tela[1] == 0:
		fundo.blit(duende, (200, 200))
		fundo.blit(pirata, (50, 350))
		coisasadesenhar += [casebre]

	coisasadesenhar.sort(key=lambda x: x.pos[1] + x.get_rect()[3])
	for coisaadesenhar in coisasadesenhar:
		coisaadesenhar.render(screen)

	if splash.get_alpha() > 0:
		splash.set_alpha(max(0, splash.get_alpha() - 255./10))
		screen.blit(splash, (0, 0))
	pygame.display.flip()

	tempo.tick(60)
#	print tempo.get_fps(), 'QPS'

