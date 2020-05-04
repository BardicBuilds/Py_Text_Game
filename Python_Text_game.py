# Python game
# Molly

import CMD
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####
class player:
	def__init__(self):
		self.name = ""
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = "start"
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		 start_game() # placeholder until written
	elif option.lower() == ("help"):
		help_menu() #placeholder
	elif option.lower() == ("quit"):
		sys.exit() 
	while option.lower() not in ["play", "help", "quit"]:
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
		 	start_game() # placeholder until written
		elif option.lower() == ("help"):
			help_menu() #placeholder
		elif option.lower() == ("quit"):
			sys.exit() 

def title_screen():
	os.system("clear")
	print("################################")
	print("# Welcome to Quarantine in NYC #")
	print("################################")
	print("             ~ Play ~           ")
	print("             ~ Help ~           ")
	print("             ~ Quit ~           ")
	print("   Copyright Cursed Year 2020   ")
	print("############################### ")
	title_screen_selections()

def help_menu():
	print("#######################################")
	print("#      How To Explore this World      #")
	print("#######################################")
	print(" ~ Use up, down, left, right to move ~ ")
	print("    ~ Type your commands to do them ~   ")
	print("   ~ Use 'look' to inspect something~  ")
	print("            ~ Good luck! ~             ")
	print("###################################### ")
	title_screen_selections()

#### GAME FUNCTIONALITY ###
def start_game():



##### MAP ######
"""
a1  a2...  #PLAYER STARTS AT b2
-------------
|  |  |  |  |  a4 
-------------
|  |  |  |  |  b4...
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""

ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "info"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
				"b1": False, "b2": False, "b3": False, "b4": False,
				"c1": False, "c2": False, "c3": False, "c4": False,
				"d1": False, "d2": False, "d3": False, "d4": False,
				}

zonemap = {
	"a1": {
		ZONENAME: "Village Spirits Shoppe",
		DESCRIPTION = " 'Welcome to the Spirits Shoppe! We have a great feeling about today and an even greater selection!' "
		EXAMINATION = " *The small old mandrake in the corner of the shoppe looks at you as if it does not, in face, have a great feeling about today* "
		SOLVED = False
		UP = " "
		DOWN = "down", "south"
		LEFT = " "
		RIGHT = "right", "east"
	},
"a1": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"a1": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"a2": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"a3": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"a4": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"b1": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"b2": {
		ZONENAME: "Home",
		DESCRIPTION = "This is your home."
		EXAMINATION = "Your home looks clean."
		SOLVED = False,
		UP = "a2",
		DOWN = "c2",
		LEFT = "b1",
		RIGHT = "b3",
	},
	"b3": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"b4": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"c1": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"c2": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"c3": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
	"c4": {
		ZONENAME: ""
		DESCRIPTION = "description"
		EXAMINATION = "info"
		SOLVED = False
		UP = "up", "north"
		DOWN = "down", "south"
		LEFT = "left", "west"
		RIGHT = "right", "east"
	},
		}















