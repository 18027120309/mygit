import os
def find():
    name=input('file name:')
    output = os.system('for /r .\ %i in ('+name+') do @echo %i')
