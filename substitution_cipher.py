
import random
import re


class SubstitutionCipher:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self):
        self.key = self.generate_key()
        self.inverse_key = self.generate_inverse_key()

    def generate_key(self):
        key = self.alphabet.copy()
        random.shuffle(key)
        return dict(zip(self.alphabet, key))

    def generate_inverse_key(self):
        inverse_key = {}
        for key, value in self.key.items():
            inverse_key.update({value: key})
        return inverse_key

    def encipher(self, plaintext):
        plaintext = plaintext.lower()
        plaintext = re.sub("[^a-z]+", "", plaintext)

        ciphertext = ""
        for letter in plaintext:
            ciphertext += self.key[letter]

        return ciphertext.upper()

    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()

        plaintext = ""
        for letter in ciphertext:
            plaintext += self.inverse_key[letter]

        return plaintext

