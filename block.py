import numpy as np
from block_function import BlockFunction

def concatentate(x1, x2):
    return np.append(x1, x2)

def swap(x1, x2):
    return concatentate(x2, x1)

def xor(x1, x2):
    return 1 * np.logical_xor(x1, x2)

class Block():
    def __init__(self, directory=''):
        self.directory = directory

    def compute(self, x, key):
        left, right = x[:32], x[32:]
        return swap(right, xor(left, BlockFunction().compute(right, key)))


if __name__ == "__main__":
    obj = Block()
    x = np.random.randint(2, size=(64,))
    key = np.random.randint(2, size=(48,))
    print(f"f: {len(x)}")
    print(f"key: {len(key)}")
    a = obj.compute(x, key)
    print(a)
    print(len(a))
    print(len(x))
