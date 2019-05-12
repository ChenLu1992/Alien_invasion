#!/usr/bin/env python
#coding=gbk
#
#       settings.py
#       
#       Copyright 2019 Administrator <Administrator@2013-20151101LB>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       



class Settings():
	""" 存储外星人入侵的所有设置的类 """
	def __init__(self):
		"""初始化游戏设置"""
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5

