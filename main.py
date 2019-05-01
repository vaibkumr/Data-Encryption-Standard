from block import Block
from utils import Permutation
from generate_keys import Key
import numpy as np

class DES():
    def __init__(self):
        pass

    def string_to_binary(self, plaintext):
        plaintext = ''.join([bin(ord(x))[2:].zfill(8) for x in plaintext])
        extras = len(plaintext) % 64
        if extras:
            plaintext += '0'*(64-extras)
        return np.array([elem for elem in plaintext])

    def binary_to_string(self, binary):
        if not isinstance(binary, np.ndarray):
            binary = np.array([x for x in binary])
        N = len(binary)/8
        string = ""
        for x in np.split(binary, N):
            character = ''.join([str(t) for t in x])
            character = chr(int(character, 2))
            string += character
        return string

    def encrypt(self, plaintext, save_file = False):
        plaintext = self.string_to_binary(plaintext)
        perm = Permutation(load=True)
        keys = Key().load_keys()
        #break file into chunks of 8 bytes
        N = len(plaintext)/64
        ciphertext = np.array([], dtype=int)
        for x in np.split(plaintext, N):
            f = perm.permute(x).astype(int)
            block = Block()
            for i in range(16):
                key = keys[f"key_{int(i)}"]
                f = block.compute(f, key)
            f = perm.reverse_permute(f)
            ciphertext = np.append(ciphertext, f)
        if save_file:
            with open(save_file, 'wb') as handle:
                handle.write(ciphertext)
        return ciphertext

    def decrypt(self, ciphertext):
        perm = Permutation(load=True)
        keys = Key().load_keys()
        N = len(ciphertext)/64
        plaintext = np.array([], dtype=int)
        for x in np.split(ciphertext, N):
            f = perm.permute(x).astype(int)
            block = Block()
            for i in range(16):
                key = keys[f"key_{int(15-i)}"]
                f = block.compute(f, key)
            f = perm.reverse_permute(f)
            plaintext = np.append(plaintext, f)
        return self.binary_to_string(plaintext)

if __name__ == "__main__":
    obj = DES()
    encrypted = obj.encrypt("ignorance is bliss; ignorance is a sin",
                                save_file='encrypted/ignorance_bliss_sin.dsa')
    decrypted = obj.decrypt(encrypted)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
