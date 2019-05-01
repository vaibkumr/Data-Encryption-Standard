import numpy as np
from utils import ExpandPermutation, Permutation, SubstitutionBoxes

class BlockFunction():
    def __init__(self):
        pass

    def compute(self, x, key):
        f = ExpandPermutation(load=True).compute(x)
        f = 1 * np.logical_xor(f, key)
        f = SubstitutionBoxes(load=True).compute(f)
        f = Permutation(size=32, load=True,
                        filename='files/innerperm.np').compute(f)
        return f.astype(int)


if __name__ == "__main__":
    '''test'''
    obj = BlockFunction()
    x = np.random.randint(2, size=(32,))
    key = np.random.randint(2, size=(48,))
    a = obj.compute(x, key)
    print(a)
    print(len(a))
    print(len(x))
