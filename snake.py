#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Импортируем библиотеку pygame
import pygame, sys, random
from pygame import *


#Объявляем переменные
WIN_WIDTH = 400 #Ширина создаваемого окна
WIN_HEIGHT = 400 # Высота
i = 0
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"
white = "#ffffff"


def block(screen1, segment, segColor, xchord, ychord):
	segment = Surface ((20,20))
	segment.fill(Color(segColor))
	screen1.blit(segment, (xchord,ychord))


def main():
	pygame.init() # Инициация PyGame, обязательная строчка
	screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
	pygame.display.set_caption("snake") # Пишем в шапку
	bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
	# будем использовать как фон
	bg.fill(Color(BACKGROUND_COLOR)) # Заливаем поверхность сплошным цветом
	block_size = 20
	block_width = 20
	block_height = 20
	blockSnake = Surface ((block_width, block_height))
	blockSnake.fill(Color(white))

	blockFood = Surface ((20,20))
	foodColor = "#ff55ff"
	blockFood.fill (Color(foodColor))
	#color maybe not a variable but const string like that "#ff55ff"
	x = random.randrange(0,400,20)
	y = random.randrange(0,400,20)
	xfood = random.randrange(0,400,20)
	yfood = random.randrange(0,400,20)
	y_speed = 0
	x_speed = 0
	xSnakeChords = []
	ySnakeChords = []
	timer = pygame.time.Clock()



	while 1: # Основной цикл программы
		timer.tick(20)
		for event in pygame.event.get(): # Обрабатываем события
			if event.type == QUIT:
				raise SystemExit("QUIT")



		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -20
				y_speed = 0

			if event.key == pygame.K_RIGHT:
				x_speed = 20
				y_speed = 0

			if event.key == pygame.K_UP:
				y_speed = -20
				x_speed = 0

			if event.key == pygame.K_DOWN:
				y_speed = 20
				x_speed = 0


		# блок удалить после тестирования роста змеи
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0

		# --- Game Logic



		# Move the object according to the speed vector.
		xbuffer = x
		ybuffer = y
		xSnakeChords.append(xbuffer)
		ySnakeChords.append(ybuffer)
		x = x + x_speed
		y = y + y_speed


		# блок условий стенки
		if x < 0:
			x = 380
		if y < 0:
			y = 380
		if x > 380:
			x = 0
		if y > 380:
			y = 0
		# блок условий натыкания на еду
		if x == xfood and y == yfood:
		#if xbuffer < x and ybuffer == y: # влево по Х
		# block_width = block_width + 20
		# blockSnake = Surface ((block_width, block_height))
		# blockSnake.fill(Color("#ffffff"))
		#if xbuffer > x and ybuffer == y: # вправо по Х
		# block_width = block_width + 20
		# blockSnake = Surface ((block_width, block_height))
		# blockSnake.fill(Color("#ffffff"))
		#if ybuffer < y and xbuffer == x: # vniz po y
		# block_height = block_height + 20
		# blockSnake = Surface ((block_width, block_height))
		# blockSnake.fill(Color("#ffffff"))
		#if ybuffer > y and xbuffer == x: # vverh po y
		# block_height = block_height + 20
		# blockSnake = Surface ((block_width, block_height))
		# blockSnake.fill(Color("#ffffff"))
			colors = ["#CD5C5C", "#E9967A", "#DC143C", "#FF0000", "#B22222", "#8B0000", "#ADFF2F", "#32CD32", "#98FB98", "#00FA9A", "#9ACD32", "#FF69B4", "#FF1493", "#C71585", "#DB7093", "#FF4500", "#FFD700", "#20B2AA", "#008B8B", "#00FFFF", "#4682B4", "#8A2BE2", "#8B4513", "#0000FF"]
			
			xfood = random.randrange(0,400,20)
			yfood = random.randrange(0,400,20)
			foodColorNum = random.randrange(0,len(colors),1)
			blockFood.fill (Color(colors[foodColorNum]))
			
		screen.blit(bg, (0,0)) # Каждую итерацию необходимо всё перерисовывать


		screen.blit(blockFood, (xfood, yfood))
		#for i in xSnakeChords:
		# for j in ySnakeChords:
		# screen.blit(blockSnake, (i,j))
		screen.blit(blockSnake, (x,y))


		pygame.display.update() # обновление и вывод всех изменений на экран



if __name__ == "__main__":
	main()

