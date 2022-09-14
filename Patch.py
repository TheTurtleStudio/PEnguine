import os, sys
from _ROOT.PEnguineLogger import print
from _ROOT import PEnguineLogger
def Validate():
    PEnguineLogger.clear()
    try:
        validations = ["Assets", "_ROOT", "Behaviors"]
        for entry in validations:
            if not os.path.isdir(entry):
                print(f"Created missing directory \"{entry}\"")
                os.mkdir(entry)
    except Exception as E:
        ThrowError(E)

def ThrowError(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
  
if __name__ == "__main__":
    Validate()
