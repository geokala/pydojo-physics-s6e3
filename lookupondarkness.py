#! /usr/bin/env python
import random
import time

class Particle:
    def __init__(self, particle_type, vel=[0.0], pos=[0,0]):
        self.gravity = 5
        self.vel = vel
        self.pos = pos
        self.type = particle_type

    def move(self):
        self.vel[1] = self.vel[1] - self.gravity
        self.pos = [self.pos[axis] + self.vel[axis] for axis in (0,1)]
        return self.get()

    def get(self):
        return self.pos, self.type

class Generator:
    def __init__(self,particle= None, vel=[100,0], pos=[0,0]):
        self.particle = particle
        self.pos = pos
        self.vel = vel


    def spawn(self):
        return Particle(self.particle.type, self.vel, self.pos)



def run(width=100, height=70):
    generators = []
    generators.append(Generator(Particle(
                "smoke",
                [0, random.randint(0,height)],
                [width - random.randint(0,width), 0]
            )
        )
    )


    particles = []
    for i in range(0, 5):
        particles.append(
            Particle(
                "smoke",
                [0, random.randint(0,height)],
                [width - random.randint(0,width), 0]
        )
    )


    while True:
        [particles.append(g.spawn()) for g in generators]
        yield [p.move() for p in particles]


if __name__ == "__main__":
    for item in run():
        print(item)
        time.sleep(1)
