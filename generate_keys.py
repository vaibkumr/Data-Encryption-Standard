import numpy as np
from utils import CompactPermutation
import pickle

class Key():
    def __init__(self, filename='files/keys.des'):
        self.filename = filename
        pass

    def save_keys(self, filename=False):
        if not filename: filename = self.filename
        with open(filename, 'wb') as handle:
            pickle.dump(self.keys, handle, pickle.HIGHEST_PROTOCOL)

    def load_keys(self):
        with open(self.filename, 'rb') as handle:
            self.keys = pickle.load(handle)
        return self.keys    

    def generate_keys(self):
        keys = {}
        keys['master_key'] = self.generate_master_key()
        keys = self.generate_roundkeys(keys)
        self.keys = keys
        self.save_keys()

    def generate_master_key(self):
        '''key is of 64 bits with 8 parity bits which makes it 56 bit long'''
        key = np.random.randint(2, size=(56, ))
        key = np.append(key, np.ones(8, dtype=int)) #Parity bits
        return key

    def generate_roundkeys(self, keys):
        masterkey = keys['master_key'][:56]
        for round in range(16):
            roll_amount = np.random.randint(1,3)
            left, right = masterkey[:28], masterkey[28:]
            left, right = np.roll(left, roll_amount), np.roll(right, roll_amount)
            perm = CompactPermutation()
            left, right = perm.compute(left), perm.compute(right)
            key = np.append(left, right)
            keys[f"key_{int(round)}"] = key
        return keys

if __name__ == "__main__":
    obj = Key()
    obj.generate_keys()
