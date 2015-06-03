#!/usr/bin/python
import sys
import os
import modules

def respond(response):
    print response + "\n"
    os.system("espeak -v en-us -p 0 -s 150 \"" + response + "\"")

exit = False

print # Initialize program with blank line
respond("MY NAME IS FINN. HOW CAN I HELP YOU?")

while exit is not True:

    command = raw_input()

    # set the return value of modules' execute function to a variable so we don't run it more than once
    response = modules.execute(command)

    if(response != None):
        respond(response)
    else:
        if command.lower() == "exit":
            respond("EXITING.")
            exit = True
        elif command != "":
            respond("SORRY, I DON'T UNDERSTAND WHAT YOU MEAN.")

sys.exit(0)
