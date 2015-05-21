import modules
from random import randint

def main(command):
    if command.lower().startswith("is") or command.lower().startswith("really") or command.lower().startswith("are you sure"):

        # create random number and choose either yes, no, or maybe

        num = randint(1,10)

        if num < 5:
            return "NO."
        elif num > 5:
            return "YES."
        else:
            return "MAYBE."

    else:
    	return False
