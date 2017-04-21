#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Импортируем библиотеку pygame
import pygame, sys, random
from pygame import *


#Объявляем переменные
WIN_WIDTH = 400 #Ширина создаваемого окна
WIN_HEIGHT = 400 # Высота
WIN_SIZE = 400
i = 0
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"
white = "#ffffff"


#def block(screen1, segment, segColor, xchord, ychord):
#	segment = Surface ((20,20))
#	segment.fill(Color(segColor))
#	screen1.blit(segment, (xchord,ychord))


def main():
	pygame.init() # Инициация PyGame, обязательная строчка
	screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
	pygame.display.set_caption("snake") # Пишем в шапку
	bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
	# будем использовать как фон
	bg.fill(Color(BACKGROUND_COLOR)) # Заливаем поверхность сплошным цветом
	
	#Объявляем переменные
	blockSize = 20
	block_width = 20
	block_height = 20
	foodColor = "#ff55ff"
	menuColor = "#009911"
	
	# declaration of snake and food blocks and fill them with color
	blockSnake = Surface ((blockSize, blockSize))
	blockSnake.fill(Color(white))
	
	blockFood = Surface ((blockSize,blockSize))
	blockFood.fill (Color(foodColor))
	#snake = [blockSnake]
	# случайным образом задаем начальные координаты змеи и еды
	x = random.randrange(0,WIN_SIZE,blockSize)
	y = random.randrange(0,WIN_SIZE,blockSize)
	xfood = random.randrange(0,WIN_SIZE,blockSize)
	yfood = random.randrange(0,WIN_SIZE,blockSize)
	
	y_speed = 0
	x_speed = 0
	xSnakeChords = []
	ySnakeChords = []
	#xprev = []
	#yprev = []
	timer = pygame.time.Clock()


# Основной цикл программы
	while 1: 
		timer.tick(15)
		for event in pygame.event.get(): # Обрабатываем события
			if event.type == QUIT:
				raise SystemExit("QUIT")
		#xprev.append(x_speed)
		#yprev.append(y_speed)
		# блок передвижения блока по нажатию стрелок
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -blockSize
				y_speed = 0

			if event.key == pygame.K_RIGHT:
				x_speed = blockSize
				y_speed = 0

			if event.key == pygame.K_UP:
				y_speed = -blockSize
				x_speed = 0

			if event.key == pygame.K_DOWN:
				y_speed = blockSize
				x_speed = 0

		
		# блок удалить после тестирования роста змеи
		#if event.type == pygame.KEYUP:
		#	if event.key == pygame.K_LEFT:
		#		x_speed = 0
		#		prevKey = left
		#	if event.key == pygame.K_RIGHT:
		#		x_speed = 0
		#		prevKey = right
		#	if event.key == pygame.K_UP:
		#		y_speed = 0
		#		prevKey = up
		#	if event.key == pygame.K_DOWN:
		#		y_speed = 0
		#		prevKey = dowm
		
		# block of game menu during game cycle
	#	if event.type == pygame.KEYUP:
	#		if event.key == pygame.K_ESCAPE:
	#			
	#			bg.fill(Color(menuColor)) # Заливаем поверхность сплошным цветом
	#			screen.blit(bg, (0,0))
	#			blockSnake.fill(Color(menuColor))
	#			blockFood.fill(Color(menuColor))
	#			pygame.display.update() # обновление и вывод всех изменений на экран
				
# --- Game Logic

		# Move the object according to the speed vector.
		
		xSnakeChords.append(x)
		ySnakeChords.append(y)
		x = x + x_speed
		y = y + y_speed

		# блок условий стенки
		if x < 0:
			x = (WIN_SIZE - blockSize)
		if y < 0:
			y = (WIN_SIZE - blockSize)
		if x > (WIN_SIZE - blockSize):
			x = 0
		if y > (WIN_SIZE - blockSize):
			y = 0
			
		# блок условий натыкания на еду
		if x == xfood and y == yfood:
		
			colors = ["#CD5C5C", "#E9967A", "#DC143C", "#FF0000", "#B22222", "#8B0000", "#ADFF2F", "#32CD32", "#98FB98", "#00FA9A", "#9ACD32", "#FF69B4", "#FF1493", "#C71585", "#DB7093", "#FF4500", "#FFD700", "#20B2AA", "#008B8B", "#00FFFF", "#4682B4", "#8A2BE2", "#8B4513", "#0000FF"]
			#snake.append(blockSnake)
			xfood = random.randrange(0,WIN_SIZE,blockSize)
			yfood = random.randrange(0,WIN_SIZE,blockSize)
			foodColorNum = random.randrange(0,len(colors),1)
			blockFood.fill (Color(colors[foodColorNum]))
			
		screen.blit(bg, (0,0)) # Каждую итерацию необходимо всё перерисовывать


		screen.blit(blockFood, (xfood, yfood))
		#for i in xSnakeChords:
		# for j in ySnakeChords:
		# screen.blit(blockSnake, (i,j))
		
		#for j in range (len(xprev)):
			#for h in range (len(yprev)):
				#for i in range (len(snake)):
					#screen.blit(snake[i], (xprev[j],yprev[h]))

		screen.blit(blockSnake, (x, y))
		pygame.display.update() # обновление и вывод всех изменений на экран
		



if __name__ == "__main__":
	main()
