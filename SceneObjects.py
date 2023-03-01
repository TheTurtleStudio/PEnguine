if __name__ == "__main__":
    quit()
from MainEngine import EngineUtils
from MainEngine import Types
from MainEngine.Engine import Engine
from MainEngine import EngineCore
from Behaviors import Generic
from Behaviors import FrameCounter

from pygame.math import Vector3
from pygame.math import Vector2
import pygame

class Objects(EngineCore.EngineObjects):
    def __init__(self, engine: Engine):
        self.ObjectList = []
        self._engine = engine
        self.EngineCore(engine)

        
        StarterObject = Generic.Create(engine)
        StarterObject.gameObject.size = engine._Globals._display
        StarterObject.gameObject.position = Vector3(0, 0, 0)
        StarterObject.gameObject.name = "Starter Object"
        StarterObject.gameObject.description = "This object is to show the basic structure of object instantiation."
        StarterObject.gameObject.color = (200, 200, 200)
        
        Counter = FrameCounter.Create(engine)


        #Subscribes all instantiated objects
        for var in dir():
            exec(f"""if (type({var}).__name__) == 'Create': self.ObjectList.append({var})""")

    def get(self):
        return tuple(self.ObjectList)

class Injections(): #Where we change attributes of the window and do custom thingies
    caption = "PEnguine Framework"
    dimensions = (314, 314)
    icon = "_ROOT\\NOTEXTURE.png"
    targetFrameRate = 60
    abstract = [
        "#This is raw code to be after all other injections are made",
        "#Put every piece of code encapsulated in a string as a new item in the list.",
        "print(\"Injections complete\") #This is for debugging though!",
    ]
