#coding=gbk

import pygame
from settings import Settings
from ship import *
import game_functions as gf
def run_game():
	#屏幕初始化
	pygame.init()
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	
	waner = WanEr(screen)

	while True:
		#监听事件
		gf.check_events(ship)
		
		ship.update()
		
		gf.update_screen(ai_settings, screen, ship)

run_game()
		
		
