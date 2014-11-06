#! /usr/bin/env python
import random
import time

class Particle:
    def __init__(self, gravity, particle_type, vel=[0.0], pos=[0,0]):
        self.gravity = gravity
        self.vel = vel
        self.pos = pos
        self.type = particle_type

    def move(self):
        self.vel[1] = self.vel[1] - self.gravity
        self.pos = [self.pos[axis] + self.vel[axis] for axis in (0,1)]
        return self.get()

    def get(self):
        return self.pos, self.type


def run(width=100):

    particles = []
    for i in range(0, 5):
        particles.append(
            Particle(
                random.randint(3,10),
                "smoke",
                [0, random.randint(0,70)],
                [width - random.randint(0,width), 0])
        )

    while True:
        yield [p.move() for p in particles]

if __name__ == "__main__":
    for item in run():
        print(item)
        time.sleep(1)
