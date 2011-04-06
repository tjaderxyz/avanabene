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
			fundo = gerafundo("images/t_praia.png")
		if event.key == pygame.K_e:
			fundo = gerafundo("images/t_deserto.png")
		if event.key == pygame.K_r:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_t:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_y:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_u:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_i:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_o:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_p:
			fundo = gerafundo("images/t_grama_primeira.png")
		if event.key == pygame.K_a:
			fundo = gerafundo("images/t_gramaescuro.png")
		if event.key == pygame.K_s:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_d:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_f:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_g:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_h:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_j:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_k:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_l:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_z:
			fundo = gerafundo("images/t_gramaescuro2.png")
		if event.key == pygame.K_x:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_c:
			fundo = gerafundo("images/t_gramaflor.png")
		if event.key == pygame.K_v:
			fundo = gerafundo("images/t_grama.png")
		if event.key == pygame.K_b:
			fundo = gerafundo("images/t_grama3.png")
		if event.key == pygame.K_n:
			fundo = gerafundo("images/t_grama2.png")
		if event.key == pygame.K_m:
			fundo = gerafundo("images/t_grama1.png")
		#e la se vao os demais terrenos

	screen.blit(fundo, (0, 0))
	pygame.display.flip()

