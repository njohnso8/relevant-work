import os

def safe_open(filename, mode):

    # the input filename datatype is a string
    if type(filename) != str:
        return None

    # Open for reading
    if mode == 'r':

        # The file must exist on disk
        if not(os.path.isfile(filename)):
            print("File", filename, "not found.")
            return None

    # Open for reading
    elif mode == 'w':
        
        # Are we overwriting?
        if os.path.isfile(filename):
            print("Overwriting", filename)

    # Open for appending        
    elif mode == 'a':
        
        # The file does not yet exist on disk
        if not(os.path.isfile(filename)):
            print("Warning: Appending to empty file", filename)
        
    return open(filename, mode)