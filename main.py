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
	pygame.mixer.init() # init of music mixer
	
	pygame.mixer.music.load("mainost.mp3") #load music file from default folder
	pygame.mixer.music.set_volume(0.30) #volume of sound
	pygame.mixer.music.play()  #start to play NB: try to use it with IF-cycle
 
#	splat = pygame.mixer.Sound("splat.wav")
#	splat.set_volume(0.50)
#	splat.play()

	screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
	pygame.display.set_caption("snake") # Пишем в шапку
	bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
	# будем использовать как фон
	
	bg.fill([0,0,0]) # Заливаем поверхность сплошным цветом
	
	#Объявляем переменные
	blockSize = 20
	block_width = 20
	block_height = 20
	foodColor = "#ff55ff"
	menuColor = "#009911"
	
	# declaration of snake and food blocks and fill them with color
	sizex = blockSize
	sizey = blockSize
	
	foodShadow = Surface ((sizex, sizey))
	
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
	shadowIterator = 0
	y_speed = 0
	x_speed = 0
	xSnakeChords = []
	ySnakeChords = []
	#xprev = []
	#yprev = []
	timer = pygame.time.Clock()
	red = 255
	green = 85
	blue = 255

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
#				x = x + x_speed
#				y = y + y_speed
			if event.key == pygame.K_RIGHT:
				x_speed = blockSize
				y_speed = 0
#				x = x + x_speed
#				y = y + y_speed
			if event.key == pygame.K_UP:
				y_speed = -blockSize
				x_speed = 0
#				x = x + x_speed
#				y = y + y_speed
			if event.key == pygame.K_DOWN:
				y_speed = blockSize
				x_speed = 0
#				x = x + x_speed
#				y = y + y_speed
					
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
			#snake.append(blockSnake)
			shadowX = xfood
			shadowY = yfood
			
			bufferRED = red
			bufferGREEN = green
			bufferBLUE = blue
			
			xfood = random.randrange(0,WIN_SIZE,blockSize)
			yfood = random.randrange(0,WIN_SIZE,blockSize)
			
			foodShadow.fill ([red, green, blue])
			
			red = random.randrange(20,200,1)
			green = random.randrange(20,200,1)
			blue = random.randrange(20,200,1)
			
			blockFood.fill ([red, green, blue])  # меняем цвет еды на рандомные цвета
			bg.fill ([green, blue, red]) #меняем цвет поля на рандомный, но другой цвет
			shadowIterator =  1
			
		screen.blit(bg, (0,0)) # Каждую итерацию необходимо всё перерисовывать
			
		if shadowIterator == 1:
			if sizex <= 600:
				foodShadow = Surface ((sizex, sizey))
				sizex = sizex + 150
				sizey = sizey + 150
				foodShadow.fill ([bufferRED, bufferGREEN, bufferBLUE])
				screen.blit(foodShadow, (shadowX, shadowY))
				shadowX = shadowX - 75
				shadowY = shadowY - 75
			else:
				shadowIterator = 0
				sizex = 0
				sizey = 0
				foodShadow = Surface ((sizex, sizey))
			
		screen.blit(blockFood, (xfood, yfood))
		screen.blit(blockSnake, (x, y))
		pygame.display.update() # обновление и вывод всех изменений на экран
		
if __name__ == "__main__":
	main()
