from MainEngine import ImageManipulation
from MainEngine import Types
from MainEngine.Engine import Engine
from Behaviors import Generic

from pygame.math import Vector3
import pygame

class Objects():
    def __init__(self, engine: Engine):
        self.ObjectList = []
        self._engine = engine

        #START OF ENGINE NEEDED, DO NOT REMOVE OR BAD THINGS MAY HAPPEN
        engine.SetUniversal("STARTED", False)
        engine.AddImageAsset("NOTEXTURE", "_ROOT\\NOTEXTURE.png")
        engine.AddImageAsset("NOTEXTURE_GRAYSCALE", "_ROOT\\NOTEXTUREGRAYSCALE.png")
        engine.AddAnimation("NOTEXTURE", ["NOTEXTURE"], framerate=1, loop=False)
        #END OF ENGINE NEEDED

        Template = Generic.Create(engine)
        Template.gameObject.size = engine._Globals._display
        Template.gameObject.position = Vector3(0, 0, 0)
        Template.gameObject.name = "Template"
        Template.gameObject.description = "This template is to show the basic structure of object instantiation."
        Template.gameObject.color = (200, 200, 200)
        self.ObjectList.append(Template)

    def get(self):
        return tuple(self.ObjectList)

class Injections(): #Where we change attributes of the window and do custom thingies
    caption = "PEnguine Framework"
    dimensions = (314, 314)
    icon = "_ROOT\\NOTEXTURE.png"
    abstract = [
        "#This is raw code to be after all other injections are made",
        "#Put every piece of code encapsulated in a string as a new item in the list.",
        "print(\"Injections complete\") #This is for debugging though!",
    ]
