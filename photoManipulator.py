import pygame
import sys
Image = pygame.image.load((sys.argv[1]))
(wid, hgt) = Image.get_size()
Frame = pygame.display.set_mode((wid,hgt))
Frame.blit(Image,(0,0))
First_Click = False
Second_Click = False
Test = False
BothClicks = False
x = 0
y = 0
x2 = 0
y2 = 0
pygame.display.update()
exit_flag = False
firstCoords = []
secondCoords = []
count = 0
while not exit_flag:
	if Test == True:
		Second_Click = True
	if BothClicks == True:
		BothClicks = False
		firstCoords.append([x,y])
		secondCoords.append([x2,y2])
		for i in range (x,x2,1):
			for j in range (y,y2,1):
				r, g, b, _ = Frame.get_at((i, j))
				Frame.set_at(((i, j)), (255-r,255-g,255-b))
		pygame.display.update()			
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit_flag = True
		elif e.type == pygame.MOUSEBUTTONDOWN and First_Click == False:
			(x,y) = pygame.mouse.get_pos()
			print(x,y)
			First_Click = True
			Test = True
		elif e.type == pygame.MOUSEBUTTONDOWN and Second_Click == True:
			(x2,y2) = pygame.mouse.get_pos()
			print("2nd",x2,y2)
			Second_Click = False
			Test = False
			First_Click = False
			BothClicks = True	
		elif len(firstCoords)>=1 and pygame.key.get_pressed()[pygame.K_r]:
			if(count % 2 ==0):
				for i in range(firstCoords[len(firstCoords)-1][0],secondCoords[len(secondCoords)-1][0],1):
					for j in range(firstCoords[len(firstCoords)-1][1],secondCoords[len(secondCoords)-1][1],1):
						r, g, b, _ = Frame.get_at((i, j))
						Frame.set_at(((i, j)), (255-r,255-g,255-b))
				pygame.display.update()
				firstCoords.pop()
				secondCoords.pop()
			count+=1
		elif pygame.key.get_pressed()[pygame.K_a]:
			if(count % 2 ==0):
				for i in range(0,wid,1):
					for j in range(0,hgt,1):
						r, g, b, _ = Frame.get_at((i, j))
						Frame.set_at(((i, j)), (255-r,255-g,255-b))
				pygame.display.update()
			count+=1
		elif pygame.key.get_pressed()[pygame.K_UP]:
				for i in range(0,wid,1):
					for j in range(0,hgt,1):
						r, g, b, _ = Frame.get_at((i, j))
						Frame.set_at(((i, j)), (b,r,g))
				pygame.display.update()
		elif pygame.key.get_pressed()[pygame.K_DOWN]:
				for i in range(0,wid,1):
					for j in range(0,hgt,1):
						r, g, b, _ = Frame.get_at((i, j))
						Frame.set_at(((i, j)), (g,b,r))
				pygame.display.update()
			
