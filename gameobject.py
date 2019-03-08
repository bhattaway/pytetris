import pygame

#this is the superclass that all game object classes will inherit from
class Gameobject(object):
    def __init__(self, alive=True):
        self.alive = alive

    def __str__(self):
        return "<Gameobject alive:%s>" % \
                (self.alive)

