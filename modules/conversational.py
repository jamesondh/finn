import modules

def main(command):

    replies = {
        "hello"                         : "HELLO THERE.",
        "hey"                           : "HEY THERE.",
        "how are you"                   : "I AM FINE, THANK YOU.",
        "what's up"                     : "NOT MUCH, WHAT IS UP WITH YOU?",
        "who are you"                   : "MY NAME IS FINN, I AM AN ARTIFICIALLY INTELLIGENT PROGRAM.",
        "what is your name"             : "MY NAME IS FINN, I AM AN ARTIFICIALLY INTELLIGENT PROGRAM.",
        "what are you"                  : "MY NAME IS FINN, I AM AN ARTIFICIALLY INTELLIGENT PROGRAM.",
        "who made you"                  : "MY CREATOR IS JAMESON HODGE.",
        "who is your creator"           : "MY CREATOR IS JAMESON HODGE.",
        "do you want to play a game"    : "VERY FUNNY."
    }

    # there's probably a cleaner way to do this, but this works for now

    replyFound = False

    # loop through replies to check if command matches
    for key in replies:
        if command.lower() == key or command.lower().startswith(key):
            replyFound = True
        if replyFound:
            return replies[key]

    # if nothing found, return false
    if replyFound == False:
        return False
