import os

from bitglitter.config.config import config

# These functions are for end users.

def outputStats(path):
    '''Writes a text file to a file path outlining usage statistics.'''

    activePath = os.path.join(os.getcwd(), path)
    with open(activePath + '\\Statistics.txt', 'w') as writer:
        writer.write(str(config.statsHandler))


def clearStats():
    '''Resets statistics back to zero in all fields.'''

    config.statsHandler.clearStats()
    config.saveSession()


def clearSession():
    '''Tries to remove the session pickle if it exists, clearing all statistics and custom colors.'''

    try:
        os.remove('config.pickle')
    except:
        pass


def removePartialSave(hash):
    '''Removes the PartialSave object from partialReadHolder in config as well as removes the folder containing any
    fragments.
    '''

    config.saveSession()


def clearPartialSaves():
    '''Removes all PartialSave objects and removes all data saved.'''

    config.saveSession()