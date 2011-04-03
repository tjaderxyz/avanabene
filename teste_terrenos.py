#! /usr/bin/env python
# coding: utf-8

import os, sys, pygame
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0
imagem = "images/t_grama.png"

screen = pygame.display.set_mode(size)

def gerafundo(imagem):
	terreno = pygame.image.load(imagem)
	terreno = pygame.transform.scale(terreno, [4 * i for i in terreno.get_rect()][2:]).convert_alpha()
	terrenorect = terreno.get_rect()
	fundo = pygame.Surface(size)

	for i in range(0, size[0], terrenorect[2]):
		for j in range(0, size[1], terrenorect[3]):
				fundo.blit(terreno, (i, j))
	return fundo

fundo = gerafundo(imagem)

tela = [0, 0]

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT \
		   or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_q:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_w:
			fundo = gerafundo("images/t_gramaflor.png")
		#e la se vao os demais terrenos

	screen.blit(fundo, (0, 0))
	pygame.display.flip()

