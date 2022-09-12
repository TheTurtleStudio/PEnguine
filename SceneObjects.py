from MainEngine import ImageManipulation
from MainEngine import Types
from MainEngine.Engine import Engine
from Behaviors import Generic
import pygame

class Objects():
    def __init__(self, engine: Engine):
        self.ObjectList = []
        self._engine = engine
        #START OF ROOT ALLOCATIONS, DO NOT REMOVE OR BAD THINGS MAY HAPPEN
        engine.SetUniversal("STARTED", False)
        engine.AddImageAsset("NOTEXTURE", "_ROOT\\NOTEXTURE.png") #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        engine.AddImageAsset("NOTEXTURE_GRAYSCALE", "_ROOT\\NOTEXTUREGRAYSCALE.png") #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        engine.AddAnimation("NOTEXTURE", ["NOTEXTURE"], framerate=1, loop=False) #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        #END OF ROOT ALLOCATIONS

        MainMenu = Generic.Create(engine)
        MainMenu.gameObject.size = engine._Globals._display
        MainMenu.gameObject.position = Types.Vector3(0, 0, 0)
        MainMenu.gameObject.name = "MAINMENU"
        self.ObjectList.append(MainMenu)

    def get(self):
        return tuple(self.ObjectList)

class Injections():
    caption = "PEnguine"
    dimensions = (314, 314)
    icon = "_ROOT\\NOTEXTURE.png"
    abstract = [
        "#This is raw code to be after all other injections are made",
        "#Put every piece of code encapsulated in a string as a new item in the list.",
        "print(\"Injections complete\") #This is for debugging though!",
    ]
