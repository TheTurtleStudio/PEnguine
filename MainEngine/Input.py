import pygame


class InputHandler():
    def __init__(self, engine):
        self.events = []
        self.engine = engine
        self.TestFor = self._TestFor(self)
    def _getEvents(self):
        return self.events
    def postEvents(self, events):
        self.events = events
    def clearEvents(self):
        self.events.clear()
    class _TestFor():
        def __init__(self, handler):
            self._InputHandler = handler
        def WINDOWFOCUSLOST(self):
            return self._testFor(pygame.WINDOWFOCUSLOST)[0]
        def WINDOWFOCUSGAINED(self):
            return self._testFor(pygame.WINDOWFOCUSGAINED)[0]
        def WINDOWLEAVE(self):
            return self._testFor(pygame.WINDOWLEAVE)[0]
        def WINDOWENTER(self):
            return self._testFor(pygame.WINDOWENTER)[0]
        def QUIT(self):
            return self._testFor(pygame.QUIT)[0]
        def MOUSEPOS(self):
            return pygame.mouse.get_pos()
        def RIGHTMOUSEDOWN(self):
            returnVal = self._testFor(pygame.MOUSEBUTTONDOWN)
            if returnVal[0]:
                if (returnVal[1].button == 1):
                    return True
            return False
        def RIGHTMOUSESTATE(self):
            return pygame.mouse.get_pressed()[0]
        def LEFTMOUSEDOWN(self):
            returnVal = self._testFor(pygame.MOUSEBUTTONDOWN)
            if returnVal[0]:
                if (returnVal[1].button == 3):
                    return True
            return False
        def LEFTMOUSESTATE(self):
            return pygame.mouse.get_pressed()[2]
        def KEYDOWN_ANY(self):
            return self._testFor(pygame.KEYDOWN)[0]
        def KEYDOWN(self, key: pygame.key):
            keys = pygame.key.get_pressed()
            if (keys[key]):
                return True
            return False
        def _testFor(self, typeOf: pygame.event) -> tuple((bool, object)):
            for i in self._InputHandler._getEvents():
                if i.type == typeOf:

                    return (True, i)
            return (False, None)

        def _testForRECURSIVE(self, typeOf):
            eventsReturnList = []
            for i in self._InputHandler._getEvents():
                if i.type == typeOf:
                    eventsReturnList.append(i)
            success = False if (eventsReturnList.count == 0) else True
            return (success, eventsReturnList)