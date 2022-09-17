from MainEngine import Types
import pygame

class Sheets():
    @staticmethod
    def Disect(engine, sheetPath: str, spriteDimensions: pygame.math.Vector2, amount: int, offset: int=0,):
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
