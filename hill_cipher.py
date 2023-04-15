
import numpy as np
import sympy as sp


class HillCipher:
    def __init__(self, key):
        self.key = np.array(key)
        self.block_size = self.key.shape[0]

        if self.is_key_valid():
            self.inverse_key = np.array( sp.Matrix(self.key).inv_mod(26) )
        else:
            raise Exception("Invalid key")


    def is_key_valid(self):
        shape = self.key.shape
        return len(shape) == 2 and shape[0] == shape[1] and np.linalg.det(self.key) != 0


    def encipher(self, plaintext):
        plaintext = plaintext.lower()

        while len(plaintext) % self.block_size != 0:
            plaintext += 'x'

        ciphertext = ""

        for i in range(0, len(plaintext)//self.block_size):

            char_array = np.array([])
            for j in range(i*self.block_size, (i + 1)*self.block_size):
                letter_num = ord(plaintext[j]) - 97             # the ascii number of 'a' is 97
                char_array = np.append(char_array, letter_num)

            result = np.matmul(char_array, self.key) % 26

            for letter_num in result:
                ciphertext += chr(int(letter_num) + 97)

        return ciphertext.upper()


    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        if len(ciphertext) % self.block_size != 0:
            raise Exception("Invalid cipher text")

        for i in range(0, len(ciphertext), self.block_size):

            char_array = np.array([])
            for j in range(i, i + self.block_size):
                letter_num = ord(ciphertext[j]) - 97            # the ascii number of 'a' is 97
                char_array = np.append(char_array, letter_num)

            result = np.matmul(char_array, self.inverse_key) % 26

            for letter_num in result:
                plaintext += chr(int(letter_num) + 97)

        return plaintext


    @staticmethod
    def crack_cipher(plaintext, ciphertext):
        p = plaintext[0].lower()
        c = ciphertext[0].lower()
        key = (ord(c) - ord(p)) % 26
        return key

