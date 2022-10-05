from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import CustomTypes
import pygame
class Generic(): #Change this to the name of your behavior
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None

    def Destroy(self):
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        self.gameObject.sprite.kill()
        del self.gameObject
        self.engine = None
        del self.creator
        self.creator = None


class Create():
    def __init__(self, engine):
        self.obj: Generic = Generic(engine) #Replace both "Generic"s with the name of your behavior
        self.obj.creator = self
    
    @property
    def gameObject(self):
        return self.obj.gameObject
