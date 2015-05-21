import os
import importlib

def execute(command):

    # get this folder's content
    contents = os.listdir(os.curdir + '/modules')

    # import all .py files except for this file
    for i in contents:
        if i.endswith('.py') == True and i != '__init__.py':

            imported = importlib.import_module('modules.' + i[:-3])

            # if module returned something, return it back
            if imported.main(command) != False:
                return imported.main(command)
            del imported

    del i
