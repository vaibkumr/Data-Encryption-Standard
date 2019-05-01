import numpy
from generate_keys import Key
from utils import Permutation, CompactPermutation
from utils import ExpandPermutation, SubstitutionBoxes

if __name__ == "__main__":
    # Init keys
    key = Key()
    key.generate_keys()
    key.save_keys('files/keys.des')
    # Init permutations
    # Outer permutation
    perms = Permutation()
    perms.save('files/outerperm64.np')
    # Permutation for block function (I am using same for all blocks)
    perms = Permutation(size=32)
    perms.save('files/innerperm.np')
    # Expand permutation for block function (I am using same for all blocks)
    perms = ExpandPermutation()
    perms.save('files/expandperm.np')
    # Compact permutation for block function (I am using same for all blocks)
    perms = CompactPermutation()
    perms.save('files/compactperm.np')
    # Substitution Boxes for block function (I am using same for all blocks)
    perms = SubstitutionBoxes()
    perms.save('files/subboxes.pkl')
