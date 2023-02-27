import pygame
from MainEngine import Types


class Collision():
    def __init__(self, engine):
        self.engine = engine
        self.CollisionLayersRef = Types.CollisionLayer
    def RectCollide(self, obj, layers=None):
        if (layers == None):
            layers = [self.CollisionLayersRef.NONE]
        return pygame.Rect.collidelistall(obj.gameObject.sprite.rect, self._GrabList(layers))
    def PointCollide(self, point, layers=None):
        if (layers == None):
            layers = [self.CollisionLayersRef.NONE]
        collisionList = []
        for potentialCollision in self._GrabList(layers):
            if pygame.Rect.collidepoint(potentialCollision, point):
                collisionList.append(potentialCollision)
        return collisionList
    def _GrabList(self, layers):
        returnList = []
        for obj in self.engine._Globals.sceneObjectsArray:
            if (obj.gameObject.collisionLayer in layers):
                if (obj.gameObject.renderEnabled is True):
                    returnList.append(obj.gameObject.sprite.rect)
        return returnList


class MathTools():
    @staticmethod
    def SquaredDistance(pos1, pos2):
        return ((pos1[0]-pos2[0])**2) + ((pos1[1]-pos2[1])**2)
    @staticmethod
    def Distance(pos1, pos2):
        return MathTools.SquaredDistance(pos1, pos2)**0.5
    class QuickSort():
        class Regular():
            @staticmethod
            def _partition(arr, low, high):
                i = (low-1)
                pivot = arr[high]
                for j in range(low, high):
                    if arr[j] <= pivot:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]
         
                arr[i+1], arr[high] = arr[high], arr[i+1]
                return (i+1)
            @staticmethod
            def QuickSort(arr, low, high):
                if len(arr) == 1:
                    return arr
                if low < high:
                    pi = Regular._partition(arr, low, high)
                    Regular.QuickSort(arr, low, pi-1)
                    Regular.QuickSort(arr, pi+1, high)
        class LinkedObject(): #Same as the above quicksort class. This one just attaches another list and sorts alongside the first. Used in render function to determine render priority more efficiently.
            @staticmethod
            def _partition(arr, linkedObjArr, low, high):
                i = (low-1)
                pivot = arr[high]
                for j in range(low, high):
                    if arr[j] <= pivot:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]
                        linkedObjArr[i], linkedObjArr[j] = linkedObjArr[j], linkedObjArr[i]
             
                arr[i+1], arr[high] = arr[high], arr[i+1]
                linkedObjArr[i+1], linkedObjArr[high] = linkedObjArr[high], linkedObjArr[i+1]
                return (i+1)
            @staticmethod
            def QuickSort(arr, linkedObjArr, low, high):
                if len(arr) == 1:
                    return (arr, linkedObjArr)
                if low < high:
                    pi = LinkedObject._partition(arr, linkedObjArr, low, high)
                    LinkedObject.QuickSort(arr, linkedObjArr, low, pi-1)
                    LinkedObject.QuickSort(arr, linkedObjArr, pi+1, high)


class Sheets():
    @staticmethod
    def Disect(engine, sheetPath: str, spriteDimensions: pygame.math.Vector2, amount: int, offset: int=0,): #Extracts images from spritesheets and outputs an array.
        if (type(spriteDimensions) == pygame.math.Vector3):
            spriteDimensions = pygame.math.Vector2(spriteDimensions.x, spriteDimensions.y)
        if (type(spriteDimensions) == tuple):
            spriteDimensions = pygame.math.Vector2(spriteDimensions[0], spriteDimensions[1])

        sheet = engine.GetImageAsset(sheetPath)
        if (sheet == None):
            sheet = pygame.image.load(sheetPath)
        sheet.convert_alpha()

        spriteList = []
        sheetRect = sheet.get_rect()
        rows = sheetRect.size[0] / spriteDimensions.x
        collumns = sheetRect.size[1] / spriteDimensions.y

        if not (rows.is_integer() and collumns.is_integer()):
            print(f"CANNOT CONVERT \"{sheetPath}\" TO SPRITES, INVALID DIMENSIONS")
            return []

        rows = int(rows)
        collumns = int(collumns)
            
        for y in range(collumns):
            for x in range(rows):
                currentIndex = ((y * rows) + x)
                if currentIndex >= amount + offset:
                    break
                if currentIndex >= offset:
                    image = pygame.Surface(spriteDimensions.whole, pygame.SRCALPHA).convert_alpha()
                    image.blit(sheet, (0, 0), pygame.Rect(x * spriteDimensions.x, y * spriteDimensions.y, spriteDimensions.x, spriteDimensions.y))
                    spriteList.append(image)
        return spriteList


class InputHandler(): #To test for events, use "self.engine.Input.TestFor.EVENT_HANDLER_HERE"
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