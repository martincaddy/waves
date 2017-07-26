from ywaves import ywave
import unicornhat
from time import sleep
#from tkinter import*
#import pygame, sys, time
#from pygame.locals import *
#if keypress == KEY_UP
while True:
    direction = input ('What direction do you want to go in enter Up, Down, Left or Right: ')

    if direction == "Left":
        unicornhat.rotation(0)
        ywave()
        unicornhat.show()
        sleep(1)
            
    elif direction == "Up":
        unicornhat.rotation(90)
        ywave()
        sleep(1)
            
    elif direction == "Right":
        unicornhat.rotation(180)
        ywave()
        sleep(1)
            
    elif direction == "Down":
        unicornhat.rotation(270)
        ywave()
        sleep(1)
