#! /usr/bin/env python

class Particle:
    def __init__(self, gravity, particle_type, vel=[0.0], pos=[0,0]):
        self.gravity = gravity
        self.vel = vel
        self.pos = pos
        self.type = particle_type

    def move(self):
        self.vel[1] = self.vel[1] - self.gravity

    def get(self):
        return self.pos, self.type


        
