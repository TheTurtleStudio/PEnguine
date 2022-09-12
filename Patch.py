import os, sys
def Validate():
    try:
        validations = ["Assets", "_ROOT", "Behaviors"]
        for entry in validations:
            if not os.path.isdir(entry):
                os.mkdir(entry)
    except Exception as E:
        ThrowError(E)

def ThrowError(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
  
if __name__ == "__main__":
    Validate()