from create import create
from find import find
from remove import remove
from rename import rename
while True:
    module=input('Select Module(use help to get help):')
    if module=='create':
        create()
    elif module=='find':
        find()
    elif module=='rename':
        rename()
    elif module=='remove':
        remove()
    elif module=='help':
        print('''help document
        modules:
            create
            find
            remove
            rename
            help
        ''')
    else:
        print('Module Not Found. Please Watch Help.')