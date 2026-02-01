import datetime

def GetUTC():
    return str(datetime.datetime.now())

def CheckIndex(cur):
    try:
        file = open('indexTrack.txt','r')
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
    file = open('indexTrack.txt','w')
    file.write(cur)
    file.close()
    return cur