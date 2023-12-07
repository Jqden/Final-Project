import pygame
import sys
import math
import random
from mountain_car import MountainCar
import numpy as np


# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (255, 255, 255)
CAR_COLOR = (0, 0, 255)
MOUNTAIN_COLOR = (0, 0, 0)
EDGE_COLOR = (255, 0, 0)
GOAL_COLOR = (0, 255, 0)
CAR_RADIUS = 15
MOUNTAIN_AMPLITUDE = 150

# Initialize the environment
mc = MountainCar()

# Initialize pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mountain Car Simulation")
clock = pygame.time.Clock()

def normalize_x(x):
    return (x + 1.5) / (0.7 + 1.5) * WIDTH
def normalize_y(y):
    return HEIGHT - (y + 1) / (1.2 + 1) * HEIGHT

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Take a random action (you should replace this with your RL algorithm)
    action = random.randint(-1, 1)
    mc.act(action)

    # Draw the environment
    screen.fill(BG_COLOR)

    # Draw the mountain
    xs = np.arange(-1.5, 0.71, 0.03)
    ys = np.sin(3*xs)
    xs = normalize_x(xs)
    ys = normalize_y(ys)
    for x1, y1, x2, y2 in zip(xs, ys, xs[1:], ys[1:]):
        pygame.draw.aaline(screen, MOUNTAIN_COLOR, (x1, y1), (x2, y2))
    
    # Draw the car
    car_x = normalize_x(mc.x)
    car_y = normalize_y(math.sin(3*mc.x))
    pygame.draw.circle(screen, CAR_COLOR, (car_x, car_y-CAR_RADIUS), CAR_RADIUS)

    # Draw the right and left barrier
    pygame.draw.rect(screen, GOAL_COLOR, (normalize_x(0.5), 0, 10, HEIGHT))
    pygame.draw.rect(screen, EDGE_COLOR, (normalize_x(-1.2)-10, 0, 10, HEIGHT))
    

    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
sys.exit()
