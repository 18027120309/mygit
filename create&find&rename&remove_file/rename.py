import os
def rename():
    Oname=input('file name now:')
    Nname=input('file name New:')
    os.system('move '+Oname+' '+Nname)