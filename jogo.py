#! /usr/bin/env python
# coding: utf-8

import os, sys, pygame, random, animatedactor, object, pessoa, geral, tela as telaa
pygame.init()

fonte = pygame.font.Font('unifont-5.1.20080820.pcf', 16)

screen = pygame.display.set_mode(geral.size)
pygame.display.set_caption('Aventuras de Ananias e Benevides') 

ananias = animatedactor.AnimatedActor('ananias', (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN), (2, 2, 4, 4), (7, 8))
benevides = animatedactor.AnimatedActor('benevides', (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s), (2, 2, 4, 4), (7, 8))
ananias.pos = (geral.lwidth / 2 - 7, geral.lheight / 2 - 4)
benevides.pos = (geral.lwidth / 2 + 7, geral.lheight / 2 - 4)

casa = object.Object('casa_tijolos_simples')
casa.pos = (25, 20)
arvoreseca = object.Object('arvoreseca_simples')
arvoreseca.pos = (65, 45)
arvoreseca2 = object.Object('arvoreseca2_simples')
arvoreseca2.pos = (100, 60)
casebre = object.Object('casebre1_simples')
casebre.pos = (100, 25)
duende = pessoa.Pessoa('duende', (2, 2, 4, 4), (7, 9))
duende.pos = [geral.lwidth / 2, geral.lheight / 2]
pirata = pessoa.Pessoa('pirata', (2, 2, 4, 4), (7, 8))
pirata.pos = [geral.lwidth / 2, geral.lheight / 2]

try:
	pygame.mixer.music.load(os.path.join('music', 'lojinha song.mp3'))
	pygame.mixer.music.play(-1)
except:
	pass

tela = [0, 0]
t = telaa.Telas('telas.xml')

titulo = fonte.render('Aventuras de Ananias e Benevides', False, (255, 255, 255))
titulo = pygame.transform.scale(titulo, [(geral.px / 2) * i for i in titulo.get_rect()][2:])
splash = pygame.Surface(geral.size)
splash.blit(titulo, [geral.px * i for i in (geral.lwidth / 2 - titulo.get_rect()[2] / geral.px / 2, geral.lheight / 2 - titulo.get_rect()[3] / geral.px / 2)])
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
	duende.update()
	pirata.update()
	t[tuple(tela)].update()

	def mudatela(actor, outro):
		if not actor.eventtime:
			return
		if actor.pos[0] + actor.get_rect()[2] < 0:
			actor.pos[0] += geral.lsize[0]
			outro.pos[0] = actor.pos[0]
			if outro.pos[1] > actor.pos[1]:
				outro.pos[1] = actor.pos[1] + actor.get_rect()[3]
			else:
				outro.pos[1] = actor.pos[1] - actor.get_rect()[3]
			tela[0] -= 1
			outro.set_direction(0)
		elif actor.pos[0] >= geral.lsize[0]:
			actor.pos[0] -= geral.lsize[0]
			outro.pos[0] = actor.pos[0]
			if outro.pos[1] > actor.pos[1]:
				outro.pos[1] = actor.pos[1] + actor.get_rect()[3]
			else:
				outro.pos[1] = actor.pos[1] - actor.get_rect()[3]
			tela[0] += 1
			outro.set_direction(1)
		elif actor.pos[1] + actor.get_rect()[3] < 0:
			actor.pos[1] += geral.lsize[1]
			if outro.pos[0] > actor.pos[0]:
				outro.pos[0] = actor.pos[0] + actor.get_rect()[3]
			else:
				outro.pos[0] = actor.pos[0] - actor.get_rect()[3]
			outro.pos[1] = actor.pos[1]
			tela[1] -= 1
			outro.set_direction(2)
		elif actor.pos[1] >= geral.lsize[1]:
			actor.pos[1] -= geral.lsize[1]
			if outro.pos[0] > actor.pos[0]:
				outro.pos[0] = actor.pos[0] + actor.get_rect()[3]
			else:
				outro.pos[0] = actor.pos[0] - actor.get_rect()[3]
			outro.pos[1] = actor.pos[1]
			tela[1] += 1
			outro.set_direction(3)
		else:
			return

	mudatela(ananias, benevides)
	mudatela(benevides, ananias)

	screen.blit(t[tuple(tela)].fundo, (0, 0))

	coisasadesenhar = [ananias, benevides]
	coisasadesenhar += t[tuple(tela)].coisasadesenhar

	coisasadesenhar.sort(key=lambda x: x.pos[1] + x.get_rect()[3])
	for coisaadesenhar in coisasadesenhar:
		coisaadesenhar.render(screen)

	if splash.get_alpha() > 0:
		splash.set_alpha(max(0, splash.get_alpha() - 255./10))
		screen.blit(splash, (0, 0))
	pygame.display.flip()

	tempo.tick(60)

