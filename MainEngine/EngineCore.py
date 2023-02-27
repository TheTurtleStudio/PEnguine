class EngineObjects():
    def EngineCore(self, engine):
        engine.SetUniversal("STARTED", False)
        engine.AddImageAsset("NOTEXTURE", "_ROOT\\NOTEXTURE.png")
        engine.AddImageAsset("NOTEXTURE_GRAYSCALE", "_ROOT\\NOTEXTUREGRAYSCALE.png")
        engine.AddAnimation("NOTEXTURE", ["NOTEXTURE"], framerate=1, loop=False)
