#! /usr/bin/env python
# coding: utf-8

import os, sys, pygame, random, argparse

import animatedactor, object, pessoa, geral, tela as telaa

parser = argparse.ArgumentParser(description='Ananias e Benevides.')
parser.add_argument('--mudo', '-m', dest='mudo', action='store_const',
                    const=True, default=False, help='Mudo')
parser.add_argument('--colisao', '-c', dest='colisao', action='store_const',
                    const=True, default=False, help='Caixas de colisão')
parser.add_argument('--fps', '-f', dest='fps', action='store_const',
                    const=True, default=False, help='Imprimir taxa de quadros')
args = parser.parse_args()

pygame.init()

fonte = pygame.font.Font('unifont-5.1.20080820.pcf', 16)

screen = pygame.display.set_mode(geral.size)
pygame.display.set_caption(geral.titulo) 

ananias = animatedactor.AnimatedActor('ananias', (geral.lwidth / 2 - 7, geral.lheight / 2 - 4), [(2, 0, 3, 3)], (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP), (2, 2, 4, 4), (7, 8))
benevides = animatedactor.AnimatedActor('benevides_guri', (geral.lwidth / 2 + 7, geral.lheight / 2 - 4), [(1, 0, 3, 2)], (pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w), (2, 2, 4, 4), (5, 7))

try:
	if args.mudo:
		volume = pygame.mixer.music.get_volume()
		pygame.mixer.music.set_volume(0)
	else:
		volume = 0
	pygame.mixer.music.load(os.path.join('music', 'La esperanza.mp3'))
	pygame.mixer.music.play(-1)
except:
	print 'teste'
	pass

tela = [0, 0]
t = telaa.Telas('telas.xml', [ananias, benevides])

titulo = fonte.render(geral.titulo, False, (255, 255, 255))
titulo = pygame.transform.scale(titulo, [int(geral.px / 2. * i) for i in titulo.get_rect()][2:])
splash = pygame.Surface(geral.size)
splash.blit(titulo, [geral.px * i for i in (geral.lwidth / 2 - titulo.get_rect()[2] / geral.px / 2, geral.lheight / 2 - titulo.get_rect()[3] / geral.px / 2)])
splash.set_alpha(255)
screen.blit(splash, (0, 0))
pygame.display.flip()
acabouosplash = False
pygame.time.set_timer(pygame.USEREVENT, 2000)

tempo = pygame.time.Clock()

while True:
	events = pygame.event.get()
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

	t.input(events)
	t[tuple(tela)].input(events)
	if not acabouosplash:
		continue

	t.update(t[tuple(tela)])
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

	coisasadesenhar = []
	coisasadesenhar += t.coisasadesenhar
	coisasadesenhar += t[tuple(tela)].coisasadesenhar

	coisasadesenhar.sort(key=lambda x: -x.pos[1])
	for coisaadesenhar in coisasadesenhar:
		coisaadesenhar.render(screen)

	#desenha caixas de colisão
	if args.colisao:
		for coisa in t.coisasadesenhar + t[tuple(tela)].fundo.coisasacolidir + t[tuple(tela)].coisasacolidir:
			for colisao in coisa.colisao:
				caixa = [coisa.pos[0] + colisao[0],
					 geral.lheight - (coisa.pos[1] + colisao[1]),
					 colisao[2],
					 colisao[3]]
				caixa[1] -= caixa[3] 
				caixa = [i * geral.px for i in caixa]
				pygame.draw.rect(screen, (255, 0, 255), caixa, 1)

	if splash.get_alpha() > 0:
		splash.set_alpha(max(0, splash.get_alpha() - 255./10))
		screen.blit(splash, (0, 0))
	pygame.display.flip()

	tempo.tick(60)
	if args.fps:
		print tempo.get_fps()

