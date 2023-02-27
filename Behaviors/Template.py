from MainEngine import Types
import CustomTypes
import pygame
class Template():
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None

    def Start(self):
        pass

    def Update(self):
        pass

    def Destroy(self):
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        self.gameObject.sprite.kill()
        del self.gameObject
        self.engine = None
        del self.creator
        self.creator = None


class Create():
    def __init__(self, engine):
        self.obj: Template = Template(engine)
        self.obj.creator = self
    
    @property
    def gameObject(self):
        return self.obj.gameObject
