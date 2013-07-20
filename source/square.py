#!/usr/bin/python
import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((100,100))

mstate = 0

class tinySquare:
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0],pos[1],16,16)
        self.img = pygame.Surface((16,16))
        self.state = 0
        self.img.fill((51,51,51))

    def update(self,mousepos):
        global mstate
        if self.rect.collidepoint(mousepos):
            if mstate >= 1 and self.state == 0:
                self.state = mstate
                mstate = 0
            elif mstate >= 1 and self.state >= 1:
                pass
            else:
                mstate = self.state
                self.state = 0
        if self.state == 0:
            self.img.fill((51,51,51))
        elif self.state == 1:
            self.img.fill((153,30,30))
        elif self.state == 2:
            self.img.fill((200,50,50))

class bigSquare:
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0],pos[1],36,36)
        self.img = pygame.Surface((36,36))
        self.number = 12
        self.color = pygame.Color(0,0,0,0)
        self.color.hsva = (0,84,80,0)
        self.img.fill(self.color)
        self.state = 0
    def update(self,mousepos):
        global mstate
        if self.rect.collidepoint(mousepos):
            if mstate >= 1:
                if self.number < 12:
                    self.number += 1
                    mstate = 0
            else:
                if self.number > 0:
                    self.number -= 1
                    mstate = 1+self.state
        self.color.hsva = (self.state*120,(84-7*(12-self.number)),80,0)
        self.img.fill(self.color)

squares = [
    tinySquare((12,12)),
    tinySquare((32,12)),
    tinySquare((52,12)),
    tinySquare((72,12)),
    tinySquare((12,32)),
    tinySquare((72,32)),
    tinySquare((12,52)),
    tinySquare((72,52)),
    tinySquare((12,72)),
    tinySquare((32,72)),
    tinySquare((52,72)),
    tinySquare((72,72)),
    ]

bs = bigSquare((32,32))
mousepos = (0,0)
screen = pygame.image.load("square.png")

while True:
    bs.state = 0
    window.blit(screen,(0,0))
    pygame.display.update()
    event = pygame.event.wait()
    if event.type == MOUSEBUTTONDOWN:
        bs.update((0,0))
        while True:
            event = pygame.event.wait()
            if event.type == MOUSEMOTION:
                mousepos = event.pos
            if event.type == MOUSEBUTTONDOWN:
                allactive = True
                for square in squares:
                    square.update(event.pos)
                    if square.state == 0:
                        allactive = False
                bs.update(event.pos)
                mousepos = event.pos
                if allactive:
                    for square in squares:
                        square.state = 2
                        square.update((0,0))
                    bs.state = 1
                if bs.number == 12 and bs.state == 1:
                    break
            elif event.type == QUIT:
                pygame.quit()

            window.fill(0)
            for square in squares:
                window.blit(square.img,square.rect)
            window.blit(bs.img,bs.rect)
            if mstate >= 1:
                if mstate == 2:
                    color = (41,255,41)
                else:
                    color = (255,41,41)
                pygame.draw.rect(window,color,pygame.Rect(mousepos[0]-8,mousepos[1]-8,16,16))
            pygame.display.update()
    elif event.type == QUIT:
        pygame.quit()
