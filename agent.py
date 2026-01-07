import numpy as np
import pygame
from game import Game
import time

class Agent:
    def __init__(self, epsilon=0.2):
        self.state = np.array([0, 0])
        self.Q = np.random.uniform(low=0, high=10.0, size=(4, 10, 10)) #Q(s,a)
        self.policy = np.zeros((10, 10), int)
        self.greedy = np.zeros((10, 10), int)
        self.epsilon = epsilon
        self.game = Game()
        self.prob = np.array([epsilon/3, epsilon/3, epsilon/3, epsilon/3])
        self.alpha = 0.3
        self.gamma = 0.9

    def get_state(self):
        self.state = self.game.env.sprite

    def QL(self, episodes=100):
        arr = np.array([0,1,2,3])
        for episode in range(episodes):
            self.game = Game()
            while self.game.counter < 150 and not self.game.game_over:
                self.get_state()
                old_state = self.state
                self.greedy = np.argmax(self.Q, axis=0)
                num=np.random.uniform(0,1)
                if num<self.epsilon:
                    self.policy[self.state[0]][self.state[1]] = np.random.randint(0,3)
                else:
                    self.policy[self.state[0]][self.state[1]] = self.greedy[self.state[0],self.state[1]]
                    #epsilon-greedy policy from Q has been derived
                match self.policy[self.state[0]][self.state[1]]:
                    case 0:
                        keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
                        pygame.event.post(keydown)
                    case 1:
                        keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
                        pygame.event.post(keydown)
                    case 2:
                        keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
                        pygame.event.post(keydown)
                    case 3:
                        keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
                        pygame.event.post(keydown)
                self.game.step()
                self.get_state()
                a=self.policy[old_state[0]][old_state[1]]
                Q_sa = self.Q[a][old_state[0]][old_state[1]]
                Q_next = np.max(self.Q[:,self.state[0],self.state[1]], axis = 0)
                self.Q[a][old_state[0]][old_state[1]] = Q_sa + self.alpha * (self.game.reward + self.gamma * Q_next - Q_sa)
                time.sleep(0.1)
agent = Agent(0.2)
agent.QL(20)