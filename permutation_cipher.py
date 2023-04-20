
import random
import re


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
        inverse_key = [0 for i in range(self.key_length)]
        for i in range(self.key_length):
            inverse_key[self.key[i]] = i

        return inverse_key


    def encipher(self, plaintext):
        plaintext = plaintext.lower()
        plaintext = re.sub("[^a-z]+", "", plaintext)

        while len(plaintext) % self.key_length != 0:
            plaintext += 'x'

        ciphertext = ""
        for i in range(0, len(plaintext), self.key_length):
            block = plaintext[i:i+self.key_length]

            for j in self.key:
                ciphertext += block[j]

        return ciphertext.upper()


    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()

        if len(ciphertext) % self.key_length != 0:
            raise Exception("Invalid cipher text")

        plaintext = ""
        for i in range(0, len(ciphertext), self.key_length):
            block = ciphertext[i:i+self.key_length]

            for j in self.inverse_key:
                plaintext += block[j]

        return plaintext

