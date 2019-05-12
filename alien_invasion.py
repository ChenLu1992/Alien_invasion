#coding=gbk

import pygame
from settings import Settings
from ship import *
import game_functions as gf
def run_game():
	#��Ļ��ʼ��
	pygame.init()
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#����һ�ҷɴ�
	ship = Ship(ai_settings, screen)
	
	waner = WanEr(screen)

	while True:
		#�����¼�
		gf.check_events(ship)
		
		ship.update()
		
		gf.update_screen(ai_settings, screen, ship)

run_game()
		
		
