
from fileinput import filename
import os

def GetBaseDirectory(additionalPath : str) -> str:
    baseDirectory = "C:/Radio_Application_Data" + "/" + additionalPath 
    return baseDirectory

def formatPath(path: str) -> str:
    return path.replace("/", "\\")

def forcePathExists(path: str):
    os.makedirs(path, exist_ok=True)