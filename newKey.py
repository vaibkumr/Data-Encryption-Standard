import numpy
from generate_keys import Key

if __name__ == "__main__":
    # Init keys
    key = Key()
    key.generate_keys()
    key.save_keys('files/keys.des')
