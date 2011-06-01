#! /usr/bin/env python
# coding: utf-8

import os, sys, pygame, random, animatedactor, object, pessoa, geral, tela as telaa

pygame.init()

fonte = pygame.font.Font('unifont-5.1.20080820.pcf', 16)

screen = pygame.display.set_mode(geral.size)
pygame.display.set_caption('Aventuras de Ananias e Benevides') 

ananias = animatedactor.AnimatedActor('patinador', (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN), (3, 3, 3, 3), (8, 10))
benevides = animatedactor.AnimatedActor('lemanco', (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s), (3, 3, 3, 3), (7, 8))
ananias.pos = (geral.lwidth / 2 - 7, geral.lheight / 2 - 4)
benevides.pos = (geral.lwidth / 2 + 7, geral.lheight / 2 - 4)

try:
	if '-m' in sys.argv:
		volume = pygame.mixer.music.get_volume()
		pygame.mixer.music.set_volume(0)
	else:
		volume = 0
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
acabouosplash = False
pygame.time.set_timer(pygame.USEREVENT, 2000)

tempo = pygame.time.Clock()

events = []

while True:
	events += pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT \
		   or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()
		elif event.type == pygame.USEREVENT:
			acabouosplash = True
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_m):
			a = pygame.mixer.music.get_volume()
			pygame.mixer.music.set_volume(volume)
			volume = a
	if not acabouosplash:
		continue

	ananias.input(events)
	benevides.input(events)
	events = []

	ananias.update()
	benevides.update()
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

	t[tuple(tela)].fundo.render(screen)

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

