from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self, screen):
       pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity*dt
    def split(self):
        #You should 
        self.kill()
        #NOW
        if (self.radius < ASTEROID_MIN_RADIUS):
            return
        else:
            newangle = random.uniform(20,50)
            vector1 = self.velocity.rotate(newangle)
            vector2 = self.velocity.rotate(-newangle)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            asteroid= Asteroid(self.position.x, self.position.y, newradius)
            asteroid.velocity = vector1*1.2
            asteroid2= Asteroid(self.position.x, self.position.y, newradius)
            asteroid2.velocity = vector2*1.2

    