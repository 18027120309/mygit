import os
def create():
    name=input('file name:')
    with open('%s.cmd'%name,'w',encoding='utf-8')as f:
        f.write('echo 傻逼，TeleVisionB，你个大傻瓜，作者弄死你>"your name.txt"')
