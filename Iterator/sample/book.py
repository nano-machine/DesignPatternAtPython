# -*- coding: utf-8 -*-

class Book:
	"""docstring for Book"""
	def __init__(self, name):
		self.__name = name
	def getName(self):
		return self.__name