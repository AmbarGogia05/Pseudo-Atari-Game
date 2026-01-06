import pygame
from env import Environment
from renderer import Renderer
import numpy as np

game_over = False
clock = pygame.time.Clock()
env=Environment()
renderer = Renderer(env)
action = np.zeros(2, int)
flag = np.ones(2, int)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                action = np.array([-1, 0])
            if event.key == pygame.K_DOWN:
                action = np.array([1, 0])
            if event.key == pygame.K_LEFT:
                action = np.array([0, -1])
            if event.key == pygame.K_RIGHT:
                action = np.array([0, 1])
            if event.key == pygame.K_ESCAPE:
                game_over = True
        env.update(flag*action)
        action = np.array([0, 0])
    renderer.render_bg()
    if np.array_equal(env.sprite, env.target):
        flag = np.array([0,0])
    clock.tick(60)

