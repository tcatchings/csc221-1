#!/usr/bin/python3.4
# Brandon Randle 2016 February 12
# Last Update 2016 April 13
# A program for playing with game elements.

import logging

logging.basicConfig(filename='gamelog.log', level=logging.DEBUG)

class Player:
    def __init__(self):
        self.inventory = [Dagger(), 'Gold(5)', 'Crusty Bread']

    def print_inventory(self):
        logging.info('Player viewed Inventory')
        print("Inventory: ")
        for item in self.inventory:
            print("* " + str(item))

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Dagger(Weapon):
    def __init__(self):
        self.name = "Rusty Dagger"
        self.description = "A small dagger with some rust. " \
			   "Somewhat more dangerous than a rock."
        self.damage = 10

def play():
    print("Escape from Cave Terror!")
    player = Player()
    running = 1
	
    while running:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            logging.info('Player has gone north')
            print("Go north!")
        elif action_input in ['s', 'S']:
            print("Go south!")
        elif action_input in ['e', 'E']:
            print("Go east!")
        elif action_input in ['w', 'W']:
            print("Go west!")
        elif action_input in ['i', 'I']:
            player.print_inventory()
        elif action_input in ['quit', 'exit', 'q','qq']:
            print("Farewell for now!")
            running = 0
        else:
            print("Invalid action!")

def get_player_command():
    return input("Action: ")

play()
