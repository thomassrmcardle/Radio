import datetime
import fileManager

def GetUTC():
    return str(datetime.datetime.now())

def GetIndexPath():
    basePath = fileManager.GetBaseDirectory("sequencing")
    filePath = fileManager.formatPath(basePath + "/indexTrack.txt")
    return filePath

def CheckIndex(cur):
    filePath = GetIndexPath()
    fileManager.forcePathExists(filePath)
    try:
        file = open(filePath,'r')
        playing = file.read()
        file.close()
        if playing == cur:
            return True
        else:
            return False
    except:
        return True

def SetIndex():
    cur = GetUTC()
    filePath = GetIndexPath()
    fileManager.forcePathExists(filePath)
    file = open(filePath,'w')
    file.write(cur)
    file.close()
    return cur