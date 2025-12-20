#from src.cli.cli_tools import 

def tokenizer(cmd):
    tokens = cmd.split()
    
    if "/model" in tokens or "/mdl" in tokens:
        if "/model" in tokens:
            index = tokens.index("/model") + 1
        elif "/mdl" in tokens:
            index = tokens.index("/mdl") + 1    
    
    if "/list" in tokens or "/ls" in tokens:
        pass