# Data Encryption Standard
DES is an insecure, old, easily bruteforce-able, symmetric-key encryption algorithm.


DES is simple to code and helps learning about block ciphers, this is a python implementation of the same.


It uses:
- 16 blocks
- 64 bit (56 + 8 parity bits) secret key
- Bit by bit encryption

# Overview
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/DES-main-network.png/500px-DES-main-network.png)


# How to
- On first run, execute `initialize_des` to generate a new key and initialize the model
- To generate a new key, run `newKey.py`. The new key will be saved in the file `files/keys.des` (pickled dictionary)
- Permutation, S blocks and other data is stored in `files/*np` as numpy array
- Run `main.py` to test DES encryption and decryption.

# Example
![](https://i.imgur.com/Qe1kpEU.png)
* Ladies, I use arch btw

# TODO:
- Bruteforce to make evident how inscure DES is.

# UWU
![](https://i.imgur.com/v6gAND1.png)
