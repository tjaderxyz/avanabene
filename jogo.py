#! /usr/bin/env python
# coding: utf-8

import sys, pygame, random, datetime
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Aventuras de Ananias e Benevides') 

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

import actor
ananias = actor.Actor('s_ananias_cima.png', (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN))
benevides = actor.Actor('s_benevides_cima.png', (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s))

tempo = pygame.time.Clock()

while True:
	events = pygame.event.get()
	ananias.input(events)
	benevides.input(events)
	for event in events:
		if event.type == pygame.QUIT \
		   or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			sys.exit()

	ananias.update()
	benevides.update()

	screen.blit(fundo, (0, 0))
	ananias.render(screen)
	benevides.render(screen)
	pygame.display.flip()

	tempo.tick(60)
	print tempo.get_fps(), 'QPS'

