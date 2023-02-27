from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from Behaviors.Template import Template
from Behaviors.Template import Create as TemplateCreate
import CustomTypes
import pygame

class Generic(Template): #Change this to the name of your behavior
    def Start(self):
        #Do stuff when instantiated
        pass
    def Update(self):
        #Do stuff every frame
        pass


class Create(TemplateCreate):
    def __init__(self, engine):
        self.obj: Generic = Generic(engine) #Replace both "Generic"s with the name of your behavior
        self.obj.creator = self
