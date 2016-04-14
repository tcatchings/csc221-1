###CSC221 - Spring 2016 - Belhaven University
###Final Project - Brandon Randle & Tristan Catchings

##PROJECT SPECIFICATIONS

###Objects Needed
- Player
- Location
- Item
- Game

###Built-In Modules Needed
- logging

##CLASSES OVERVIEW

###GAME CLASS
####Data
 - Dictionary containing location objects, with the keys being the coordinate pair that identifies the location.
 - List containing all items that exist
 - Variable containing the player object
####Methods
 - loadLocations
 - loadItems
 - loadPlayer
 - saveLocations
 - saveItems
 - savePlayer
 - processUserCommands
 - beginGame
 - endGame

###PLAYER CLASS
####Data
 - List of all items in inventory
 - Variable with current location object reference
####Methods
 - moveLocation
 - createLocation
 - examineLocation
 - grabItem
 - dropItem
 - createItem
 - viewInventory
 - help

###LOCATION CLASS
####Data
 - String with location name
 - String with location description
 - List of exits available
 - List of items in location

###ITEM CLASS
####Data
 - String with item name
 - String with item description

---

##CLASSES DETAILS

###GAME CLASS
####Data
 - Dictionary with coordinate pairs as keys and location objects as elements.
 - List with all items
 - Variable with player object
####Methods
 - loadLocations
 - reads locations.game file
  - parses info (name, description, items, and exits)
  - creates a location object, initializing it with the data from the file
  - location object is added to dictionary
  - continues creating objects until all locations have been created
 - loadItems
  - reads items.game file
  - parses info (name, description)
  - creates an item object, initilizing it with the data from the file
  - item object is added to the list
  - continues creating objects until all items have been created
 - loadPlayer
  - reads player.game file
  - parses info (inventory, current location)
  - creates a player object, initializing it with the data from the file
  - player is added to the player variable
 - saveLocations
  - open locations.game file in overwrite mode
  - iterate through the dictionary of location objects, taking the data from each object and appending it to the file through the parsing scheme
  - save and close file
 - saveItems
  - open items.game file in overwrite mode
  - iterate through the list of location objects, taking the data from each object and appending it to the file through the parsing scheme
  - save and close file
 - savePlayer
  - open player.game file in overwrite mode
  - take data from player object and write it to the file through the parsing scheme
  - save and close file
 - processUserCommands
  - execute beginGame
  - set running to true (1)
  - while running, execute code in an if block, with if statements correlating to user commands.
  - execute endGame when no longer running 
 - beginGame
  - execute loadLocations, loadItems, and loadPlayer
  - print welcome text and run examineLocation
 - endGame
  - print farewell text
  - execute saveLocations, saveItems, and savePlayer

###PLAYER CLASS
####Data
 - List with item objects in inventory
 - Variable with current location reference
####Methods
 - moveLocation(direction)
  - takes a parameter (direction) such as north, south, east, or west
  - if block with a statement for each direction that modifies the current location coordinates based on direction taken
  - for instance, if NORTH was the direction, 1 would be added to the Y coordinate
  - calls examineLocation()
 - createLocation(direction)
  - creates a new location in the direction specified in the argument
  - takes name and description as input from user
  - creates a new location object, adds it to the dictionary
 - examineLocation()
  - prints the name, description, items, and exits for the players current location
 - grabItem(itemName)
  - iterate through items in the location.
  - if an item is found that matches itemName, remove it from location list and add to player inventory
  - if item is not found, print message saying that there is no such item here
 - dropItem(itemName)
  - iterate through items in player inventory
  - if an item is found that matches itemName, remove it from player inventory and add to location list
  - if an item is not found, print message saying that there is no such item held
 - createItem()
  - creates a new item
  - takes name and description as input from user
  - creates a new item object, adds it to game item list and to player inventory
 - viewInventory()
  - iterates through player inventory, printing names of all items held
 - help()
  - lists all commands available to player (help, createItem, createLocation, grab, drop, north, south, east, west, look, quit)

###LOCATION CLASS
####Data
 - name
  - name of current location
 - description
  - description of current location
 - exits
  - directions that may be taken
 - items
  - list of items in location
 - coordinates
  - coordinate pair of the location

###ITEM CLASS
####Data
 - name
  - name of the item
 - description
  - description of the item
