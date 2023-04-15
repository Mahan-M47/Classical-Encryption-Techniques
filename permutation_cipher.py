import random


class PermutationCipher:
    def __init__(self, key_length):
        self.key_length = key_length
        self.key = self.generate_key()
        self.inverse_key = self.generate_inverse_key()

    def generate_key(self):
        key = list(range(self.key_length))
        random.shuffle(key)
        return key

    def generate_inverse_key(self):
        inverse_key = [None]*self.key_length
        for i in range(self.key_length):
            inverse_key[self.key[i]] = i

        return inverse_key

    def encipher(self, plaintext):
        ciphertext = ""
        for i in self.key:
            ciphertext += plaintext[i]

        return ciphertext.upper()

    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()

        plaintext = ""
        for i in self.inverse_key:
            plaintext += ciphertext[i]

        return plaintext

