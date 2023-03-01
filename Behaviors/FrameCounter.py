from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from Behaviors.Template import Template
from Behaviors.Template import Create as TemplateCreate
import CustomTypes
import pygame
import time

class FrameCounter(Template): #Change this to the name of your behavior
    

    def Start(self):
        self.lastFrameTime = time.time()
    def Update(self):
        currentTime = time.time()
        if (currentTime == self.lastFrameTime):
            print("Division by 0, could not count framecount.")
        else:
            print(1/(currentTime - self.lastFrameTime))
        self.lastFrameTime = currentTime


class Create(TemplateCreate):
    def __init__(self, engine):
        self.obj: FrameCounter = FrameCounter(engine)
        self.obj.creator = self
