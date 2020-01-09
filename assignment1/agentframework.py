# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:35:11 2020

@author: 戴尔
"""
import random
class Agent:
    def __init__(self,environment,agents,neighbourhood,x,y):
        self.environment = environment
        if (x == None):
            self.x = random.randint(0,99)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,99)
        else:
            self.y = y
        self.store = 0
        self.agents = agents
        self.neighbourhood = neighbourhood
        
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        return (self.x, self.y)
    
    def distance_between(self,agent):
        return (((self.x - agent.x)**2)+((self.y - agent.y)**2))**0.5
    
    def share_with_neighbourhoods(self):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= self.neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
               
