import pygame
from pygame.locals import *
import time

class HeroPlane(object):
	def __init__(self, screen_temp):
		self.x = 210
		self.y = 700
		self.screen = screen_temp
		self.image = pygame.image.load(".\\feiji\\enemy0.png")
		self.bullet_list = []   #存储发射出去的子弹

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()

	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x += 5

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(object):
	'''敌机的类'''
	def __init__(self, screen_temp):
		self.x = 0
		self.y = 0
		self.screen = screen_temp
		self.image = pygame.image.load(".\\feiji\\enemy0.png")

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		# for bullet in self.bullet_list:
		# 	bullet.display()
		# 	bullet.move()

	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x += 5

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(object):
	'''子弹'''
	def __init__(self, screen_temp, x, y):
		self.x = x + 40
		self.y = y -20
		self.screen = screen_temp
		self.image = pygame.image.load(".\\feiji\\bullet.png")

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

	def move(self):
		self.y -= 20

def key_control(hero_temp):
	#获取事件， 比如按键
	for event in pygame.event.get():
		if event.type == QUIT:
			print("quit")
			exit()

		elif event.type == KEYDOWN:
			if event.key == K_a or event.key == K_LEFT:
				print("left")
				hero_temp.x -= 5
			elif event.key == K_d or event.key == K_RIGHT:
				print("right")
				hero_temp.x += 5
		elif event.type == K_SPACE:
			hero_temp.fire()


def main():
	#1.创建窗口
	screen = pygame.display.set_mode((880, 900), 0, 32)

	#2.创建一个背景
	background = pygame.image.load(".\\feiji\\background.png")

	#3.创建一个飞机
	hero = HeroPlane(screen)

	#4. 创建一个敌机
	enemy = EnemyPlane(screen)

	while True:
		screen.blit(background, (0, 0))
		hero.display()
		enemy.display()
		pygame.display.update()
		key_control(hero)
		time.sleep(0.01)
if __name__ == "__main__":
	main()