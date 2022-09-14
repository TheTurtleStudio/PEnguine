import threading
import os
import Patch
import SceneObjects
class Globals:
  engine = None
  
  
class Main():
  def __init__(self, initialStart=True):
    self._PRESTART(initialStart=initialStart)
    
  def Reload(self):
    del Globals.engine
    self.__init__(initialStart=False)
    Globals.engine.Start(self)

  def _PRESTART(self, initialStart=True):
    Patch.Validate()
    from MainEngine import Types
    from MainEngine import Engine
    Globals.engine = None
    Globals.engine = Engine.Engine(initialStart=initialStart)
    settings = Engine.PregameSettings(Globals.engine)
    settings.SetScreenDimensions(Types.Vector2(SceneObjects.Injections.dimensions[0], SceneObjects.Injections.dimensions[1]))
    del settings

  def _APPENDSCENEOBJECT(self, objectTuple):
    for _object in objectTuple:
      Globals.engine.CreateNewObject(_object)
    
  def _POSTSTART(self):
    Globals.engine.SetCaption(SceneObjects.Injections.caption)
    Globals.engine.SetIcon(SceneObjects.Injections.icon)
    for rawCode in SceneObjects.Injections.abstract:
      exec(rawCode)
    objects = SceneObjects.Objects(Globals.engine)
    self._APPENDSCENEOBJECT(objects.get())

if __name__ == "__main__":
  main = Main()
  Globals.engine.Start(main)
