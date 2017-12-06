import pygame
import time

def main():
	#1. 创建窗口
	screen = pygame.display.set_mode((880, 852), 0, 32)

	#2. 创建一个背景图片
	background = pygame.image.load(".\\feiji\\fanfan.jpg")

	#3. 创建一个飞机图片
	hero = pygame.image.load(".\\feiji\\fanfan.jpg")

	x = 210
	y = 700

	while True:
		screen.blit(background, (0, 0))
		screen.blit(hero, (x, y))

		pygame.display.update()

		x += 1
		y -= 1

		time.sleep(0.01)


if __name__ == "__main__":
	main()