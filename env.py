import numpy as np
import random

class Environment:
    def __init__(self):
        self.width=10
        self.height=10

        self.bg_color = np.zeros((10,10), int)
        self.bg_color[3, :4] = 1
        self.bg_color[3, 5:7] = 1
        self.bg_color[3, 8:10] = 1
        self.sprite = np.zeros(2, int)
        self.sprite[0], self.sprite[1]=9, random.randint(0,9)
        self.target = np.array([0, 9-self.sprite[1]])

    def update(self, action):
        newstate = self.sprite + action

        if newstate[0] < 0 or newstate[0] > 9 or newstate[1] < 0 or newstate[1] > 9:
            return
        if newstate[0]==3:
            if (0 <= newstate[1] < 4) or (5 <= newstate[1] < 7) or (8 <= newstate[1] < 10):
                return
        self.sprite=newstate