# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:52:50 2022

@author: steve
"""

import character

def create_player():
    name=input("Input your player name:")
    player = character.Character(name)
    player.show_status()
    return player

def test_pl():
    player=character.Character("Cindy")
    return player

print("Welcome to the World!")
#PLAYER=create_player()
PLAYER=test_pl()
PLAYER.get_EXP(100)
PLAYER.show_status()