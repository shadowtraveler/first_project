# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:52:50 2022

@author: steve
"""

import character
import end


def create_player():
    name=input("Input your player name:")
    create_time=1
    while name=="":
        create_time+=1
        name=input("Input your player name:")
        if create_time%10==0:
            print("別鬧了，快輸入你的名字")
        if create_time>100:
            end.end_name()
    player = character.Player()
    player.set_name(name)
    player.show_status()
    return player

def test_pl():
    player = character.Player()
    player.set_name("Cindy")
    return player

def start():
    print("Hello stranger!!")
    input()
    print("This is the world of C.H.~ A gradute student who is so boring and wants to do something.")
    input()
    print("我來自台灣，所以這邊我就用中文了")
    input()
    print("這只是一個自娛娛人的小專案，如果你有興趣的話，很開心你喜歡")
    input()
    print("那麼，就開始吧")
    input()
    print("Welcome to the World!")
    PLAYER=create_player()
    #PLAYER=test_pl()
    PLAYER.get_EXP(100)
    PLAYER.show_status()

    
def main():
    start()
    
if __name__ == '__main__':
    main()