#! /usr/bin/env python
# coding: utf-8

import sys, pygame, random, datetime
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Aventuras de Ananias e Benevides') 

ananias = pygame.image.load("imagens/s_ananias_baixo.png")
ananias = pygame.transform.scale(ananias, [4 * i for i in ananias.get_rect()][2:]).convert_alpha()
ananiasrect = ananias.get_rect()
ananiasspeed = [0, 0]
benevides = pygame.image.load("imagens/s_benevides_baixo.png")
benevides = pygame.transform.scale(benevides, [4 * i for i in benevides.get_rect()][2:]).convert_alpha()
benevidesrect = benevides.get_rect()
benevidesspeed = [0, 0]
corletra = 0
pasto = pygame.image.load("imagens/t_grama.png")
pasto = pygame.transform.scale(pasto, [4 * i for i in pasto.get_rect()][2:]).convert_alpha()
pastorect = pasto.get_rect()
fro = pygame.image.load("imagens/t_gramaflor.png")
fro = pygame.transform.scale(fro, [4 * i for i in fro.get_rect()][2:]).convert_alpha()
fundo = pygame.Surface(size)

for i in range(0, size[0], pastorect[2]):
	for j in range(0, size[1], pastorect[3]):
		if random.random() > 0.92:
			fundo.blit(fro, (i, j))
		else:
			fundo.blit(pasto, (i, j))

tempo = pygame.time.Clock()
quadroimpar = False

while True:
	if quadroimpar:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ananiasspeed[0] += 1
				if event.key == pygame.K_LEFT:
					ananiasspeed[0] -= 1
				if event.key == pygame.K_DOWN:
					ananiasspeed[1] += 1
				if event.key == pygame.K_UP:
					ananiasspeed[1] -= 1
				if event.key == pygame.K_d:
					benevidesspeed[0] += 1
				if event.key == pygame.K_a:
					benevidesspeed[0] -= 1
				if event.key == pygame.K_s:
					benevidesspeed[1] += 1
				if event.key == pygame.K_w:
					benevidesspeed[1] -= 1
				if event.key == pygame.K_q:
					sys.exit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ananiasspeed[0] -= 1
				if event.key == pygame.K_LEFT:
					ananiasspeed[0] += 1
				if event.key == pygame.K_DOWN:
					ananiasspeed[1] -= 1
				if event.key == pygame.K_UP:
					ananiasspeed[1] += 1
				if event.key == pygame.K_d:
					benevidesspeed[0] -= 1
				if event.key == pygame.K_a:
					benevidesspeed[0] += 1
				if event.key == pygame.K_s:
					benevidesspeed[1] -= 1
				if event.key == pygame.K_w:
					benevidesspeed[1] += 1
			else:
				print event

	ananiasrect = ananiasrect.move([2 * i for i in ananiasspeed])
	benevidesrect = benevidesrect.move([2 * i for i in benevidesspeed])
	quadroimpar = not quadroimpar

	if (ananiasrect.colliderect(benevidesrect)):
		corletra = 255
	screen.blit(fundo, (0, 0))
	screen.blit(pygame.font.SysFont('Linux Libertine O', 36).render(unicode('Testefi', 'utf8'), True, (corletra, corletra, corletra)), (50, 50, 50, 50))
	if corletra > 0:
		corletra -= 1
	screen.blit(ananias, ananiasrect)
	screen.blit(benevides, benevidesrect)
	pygame.display.flip()
	tempo.tick(60)
	print tempo.get_fps(), 'QPS'

