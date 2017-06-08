#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, random # Импортируем библиотеку pygame, sys , random
from pygame import * #wtf?

#Объявляем переменные
WIN_SIZE = 400 #Ширина создаваемого окна
i = 0 #iterator
DISPLAY = (WIN_SIZE, WIN_SIZE) # Группируем ширину и высоту в одну переменную
black = "#000000" #color name
white = "#ffffff"  #color name

def main():
	pygame.init() # Инициация PyGame, обязательная строчка
	
	pygame.mixer.init() # init of music mixer
	pygame.mixer.music.load("mainost.mp3") #load music file from default folder
	pygame.mixer.music.set_volume(0.30) #volume of sound
	pygame.mixer.music.play()  #start to play NB: try to use it with IF-cycle
 
	screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
	pygame.display.set_caption("Snake Master") # Пишем в шапку
	
	bg = Surface((WIN_SIZE,WIN_SIZE)) # Создание фоновой поверхности
	bg.fill(Color(black)) # Заливаем поверхность сплошным цветом
	
#Объявляем переменные
	blockSize = 20  #size of 1 block
	block_width = 20 
	block_height = 20
	foodColor = "#ff55ff" #initial food color

	listIterator = 0 #iterator of lengh of snake
	listX = [] #list of choords
	listY = []
	
	abc = Surface ((blockSize, blockSize)) #secondary blocks of the snake

	# declaration of snake and food blocks and fill them with color
	sizex = blockSize #initial declaration of size of shadow. shadow will change it's size so we need different variable than block size
	sizey = blockSize
	
	foodShadow = Surface ((sizex, sizey)) #declaration of shadow after food
	
	blockSnake = Surface ((blockSize, blockSize)) #declaration of snake block
	blockSnake.fill(Color(white)) #initial color of snake
	abc = Surface ((blockSize, blockSize))
	
	blockFood = Surface ((blockSize,blockSize)) #declaration of food block
	blockFood.fill (Color(foodColor)) #initial color of food
	 
	# случайным образом задаем начальные координаты змеи и еды
	x = random.randrange(0,WIN_SIZE,blockSize)
	y = random.randrange(0,WIN_SIZE,blockSize)
	X = [] #list of chords for snake blocks
	Y = []
	
	xfood = random.randrange(0,WIN_SIZE,blockSize)
	yfood = random.randrange(0,WIN_SIZE,blockSize)
	
	y_speed = 0 #initial speed of snake
	x_speed = 0
	
	shadowIterator = 0 #iterator of shadow opacity
	
	timer = pygame.time.Clock() #declaration of game timer
	red = 255 #inital colors declaration. values are stands for initial color of food block
	green = 85
	blue = 255

# Основной цикл программы
	while 1: 
		timer.tick(10) # value stands for speed of game
		for event in pygame.event.get(): # Обрабатываем события
			if event.type == QUIT:
				raise SystemExit("QUIT")

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
			
			shadowX = xfood #buffer variables to save previous coords for shadow expansion
			shadowY = yfood
			
			bufferRED = red  #buffer variables to save previous color for shadow color
			bufferGREEN = green
			bufferBLUE = blue
			
			
			listX.append(xfood) #remember coords of food
			listY.append(yfood)
			
			listIterator += 1 #change the lengh of snake
			if len(X) < 1:
				X = [x]
				Y = [y]
			else:
				X.append(x) #remember previous coords of snake
				Y.append(y)			
			
			xfood = random.randrange(0,WIN_SIZE,blockSize) #randomly set coords of new food block
			yfood = random.randrange(0,WIN_SIZE,blockSize)			
			
			red = random.randrange(20,200,1) #randomly set color of new food block
			green = random.randrange(20,200,1)
			blue = random.randrange(20,200,1)
			
			blockFood.fill ([red, green, blue])  # меняем цвет еды на рандомные цвета
			bg.fill ([green, blue, red]) #меняем цвет поля на рандомный, но другой цвет
			shadowIterator =  1 #iterator for shadow expansion
			
		screen.blit(bg, (0,0)) # Каждую итерацию необходимо всё перерисовывать
			
		if shadowIterator == 1: #if 1 then shadow expands while it riched the size of 600
			if sizex <= 600:
				foodShadow = Surface ((sizex, sizey)) #each game cycle redraw with new size
				
				foodShadow.fill ([bufferRED, bufferGREEN, bufferBLUE]) #each time redraw with old color
				screen.blit(foodShadow, (shadowX, shadowY)) #draw it on screen
				sizex = sizex + 150 #area growth increment
				sizey = sizey + 150
				
				shadowX = shadowX - 75 #change of coords according to area growth
				shadowY = shadowY - 75
			else:
				shadowIterator = 0 # drop of shadow counter
				sizex = 0 #destroy the shadow
				sizey = 0 
				
# блок передвижения блока по нажатию стрелок
		
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT:
				x_speed = -blockSize #change of speed vector
				y_speed = 0
#				x = x + x_speed  #save vector and speed of motion
#				y = y + y_speed
				
		
			if event.key == pygame.K_RIGHT:
				x_speed = blockSize
				y_speed = 0
#				x = x + x_speed  #save vector and speed of motion
#				y = y + y_speed
				
			if event.key == pygame.K_UP:
				y_speed = -blockSize
				x_speed = 0
#				x = x + x_speed  #save vector and speed of motion
#				y = y + y_speed
				
			
			if event.key == pygame.K_DOWN:
				y_speed = blockSize
				x_speed = 0
#				x = x + x_speed  #save vector and speed of motion
#				y = y + y_speed	
			
		
		screen.blit(blockSnake, (x, y))


		
		for i in range(listIterator): #change vector of snake blocks in list according to new coords
			
			
				# блок условий стенки
			if X[i] < 0:
				X[i] = (WIN_SIZE - blockSize)
			if Y[i] < 0:
				Y[i] = (WIN_SIZE - blockSize)
			
			if X[i] > (WIN_SIZE - blockSize):
				X[i] = 0
			if Y[i] > (WIN_SIZE - blockSize):
				Y[i] = 0
				
			X[i] = x
			Y[i] = y

			X[i-1] = X[i] - x_speed
			Y[i-1] = Y[i] - y_speed
		
		x = x + x_speed  #save vector and speed of motion
		y = y + y_speed	
			
		for j in range(listIterator):	
			#each game cycle draw as much snake blocks as counted in listIterator
			X[j] = X[j] + x_speed
			Y[j] = Y[j] + y_speed
			
			screen.blit (blockSnake, (X[j], Y[j])) #draw on screen

			
		screen.blit(blockFood, (xfood, yfood)) #draw new food on screen

		 #draw snake head on screen
		pygame.display.update() # обновление и вывод всех изменений на экран
		
if __name__ == "__main__":
	main()
