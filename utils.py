import numpy as np
import pickle
import itertools

class Permutation():
    def __init__(self, size=64, load=False, filename='files/outerperm64.np'):
        self.filename, self.size = filename, size
        if not load:
            self.permute_key = self.generate_key()
        else:
            self.permute_key = self.load_key()

    def save(self, filename):
        with open(filename, 'wb') as handle:
            np.save(handle, self.permute_key)

    def load_key(self):
        with open(self.filename, 'rb') as handle:
            return np.load(handle)

    def generate_key(self):
        return np.random.permutation(np.arange(self.size))

    def permute(self, x):
        if not isinstance(x, np.ndarray): x = np.array(x)
        return x[self.permute_key]

    def compute(self, x):
        if not isinstance(x, np.ndarray): x = np.array(x)
        return x[self.permute_key]

    def reverse_permute(self, x):
        if not isinstance(x, np.ndarray): x = np.array(x)
        rev = np.zeros(len(self.permute_key), dtype=int)
        for i, k in enumerate(self.permute_key):
            rev[k] = i
        return x[rev]


class CompactPermutation():
    def __init__(self, insize=28, outsize=24, load=False,
                                filename='files/compactperm.np'):
        self.filename, self.insize, self.outsize = filename, insize, outsize
        assert outsize < insize, "insize must be larger than outsize"
        if not load:
            self.permute_key = self.generate_key()
        else:
            self.permute_key = self.load_key()

    def save(self, filename):
        with open(filename, 'wb') as handle:
            np.save(handle, self.permute_key)

    def load_key(self):
        with open(self.filename, 'rb') as handle:
            return np.load(handle)

    def generate_key(self):
        return np.random.permutation(np.arange(self.insize))

    def permute(self, x):
        if not isinstance(x, np.ndarray): x = np.array(x)
        return x[self.permute_key]

    def compute(self, x):
        if not isinstance(x, np.ndarray): x = np.array(x)
        x = x[self.permute_key]
        return x[:self.outsize]

class ExpandPermutation():
    def __init__(self, insize=32, outsize=48, load=False,
                                filename='files/expandperm.np'):
        self.filename, self.outsize, self.insize = filename, outsize, insize
        if not load:
            self.permute_key = self.generate_key()
        else:
            self.permute_key = self.load_key()

    def save(self, filename):
        with open(filename, 'wb') as handle:
            np.save(handle, self.permute_key)

    def load_key(self):
        with open(self.filename, 'rb') as handle:
            return np.load(handle)

    def generate_key(self):
        p1 = np.random.permutation(np.arange(self.insize))
        p2 = np.random.permutation(np.arange(self.insize))
        return np.append(p1, p2)[:self.outsize]

    def compute(self, x):
        if not isinstance(x, np.ndarray): x = np.array(x)
        return x[self.permute_key]

class SubstitutionBoxes():
    def __init__(self, load=False, filename='files/subboxes.pkl'):
        self.filename = filename
        if not load:
            self.sub_dict = self.generate_subs()
        else:
            self.sub_dict = self.load_dict()

    def save(self, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(self.sub_dict, handle, pickle.HIGHEST_PROTOCOL)

    def load_dict(self):
        with open(self.filename, 'rb') as handle:
            return pickle.load(handle)

    def generate_subs(self, insize=6, outsize=4):
        allins = [list(i) for i in itertools.product([0, 1], repeat=insize)]
        for i, n in enumerate(allins):
            allins[i] = ''.join([str(t) for t in n])
        allouts = [list(i) for i in itertools.product([0, 1], repeat=outsize)]
        for i, n in enumerate(allouts):
            allouts[i] = ''.join([str(t) for t in n])
        p1 = np.random.permutation(allouts)
        p2 = np.random.permutation(allouts)
        p3 = np.random.permutation(allouts)
        p4 = np.random.permutation(allouts)
        allouts = np.append(p1, p2)
        allouts = np.append(allouts, p3)
        allouts = np.append(allouts, p4)
        return dict(zip(allins, allouts))

    def compute(self, x):
        out = ""
        for hex in np.split(x, 8):
            inp = ''.join([str(t) for t in hex])
            out += self.sub_dict[inp]
        output = []
        for char in out:
            output.append(char)
        return np.array(output)

if __name__ == "__main__":
    '''tests'''
    obj = SubstitutionBoxes()
    x = np.random.randint(2, size=(48,))
    a = obj.compute(x)
    print(a)
    print(len(a))
    print(len(x))
