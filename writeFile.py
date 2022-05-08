import time
import os
def writeFile(path,string):
    with open(path,"w") as fp: fp.close

def tempFilename(prefix=''):
    return os.path.expandvars(R"${TEMP}" + "\\" + prefix + time.strftime("%Y%m%d-%H%M%S") + ".tmp")

if __name__ == "__main__":
    writeFile(tempFilename(prefix='X'),"")










