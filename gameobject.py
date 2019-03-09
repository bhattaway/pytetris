import pygame

#this is the superclass that all game object classes will inherit from
class Gameobject(object):
    def __init__(self, dx=0, dy=0, alive=True):
        self.dx = dx
        self.dy = dy
        self.alive = alive

    def __str__(self):
        return "<Gameobject dx:%s dy:%s alive:%s>" % \
                (self.dx, self.dy, self.alive)

