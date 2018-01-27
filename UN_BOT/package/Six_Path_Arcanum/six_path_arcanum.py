
from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class six_path_arcanum:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions
		

	def __call__(self):
		return self

	def claim(self):
		if eval(str(self.positions.parse(_SETTINGS, 'six_path_arcanum', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'open'))
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'open'))
			sleep(4)
			self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'claim_all'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'close'))
			self.positions.write(_SETTINGS,'six_path_arcanum','done', 1)
		else:
			print "[+] Six Path Arcanum : Complete"
			#self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'close'))