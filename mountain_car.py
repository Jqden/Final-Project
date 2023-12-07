import math
import random

# Hill has shape sin(3x) and the car starts at the bottom of the hill

class MountainCar():
    def __init__(self):
        self.x = random.uniform(-0.6, -0.4)
        self.v = 0
    
    def act(self, a):
        """
        Updates the MountainCar's state according to action a and returns the reward.
        a = -1 -> reverse
        a = 0  -> neutral
        a = 1  -> forward
        """
        if not self.is_terminal():
            self.v += 0.001*a - 0.0025 * math.cos(3*self.x)
            self.x += self.v
            # Clip x and v if they're out of range
            if self.x < -1.2 or self.x > 0.5:
                self.v = 0
            self.x = max(self.x, -1.2)
            self.x = min(self.x, 0.5)
            self.v = max(self.v, -0.7)
            self.v = min(self.v, 0.7)
        
        if self.is_terminal():
            return 0
        return -1
        
    def is_terminal(self):
        return self.x >= 0.5