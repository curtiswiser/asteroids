import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, obj):
        distance = self.position.distance_to(obj.position)
        return distance <= self.radius + obj.radius
        
        
        
        # radius_1 = self.radius 
        # radius_2 = obj_2.radius 



        # r_distance = radius_1 + radius_2
        # distance = self.position.distance_to(obj_2.position)  

        # if r_distance >= distance:
        #     return True
        # else: 
        #     return False
