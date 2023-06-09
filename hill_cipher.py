
import numpy as np
import sympy as sp
import re


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
        plaintext = re.sub("[^a-z]+", "", plaintext)

        while len(plaintext) % self.block_size != 0:
            plaintext += 'x'

        ciphertext = ""

        for i in range(0, len(plaintext)//self.block_size):

            char_array = np.array([])
            for j in range(i*self.block_size, (i + 1)*self.block_size):
                letter_num = ord(plaintext[j]) - ord('a')             # the ascii number of 'a' is 97
                char_array = np.append(char_array, letter_num)

            result = np.matmul(char_array, self.key) % 26

            for letter_num in result:
                ciphertext += chr(int(letter_num) + ord('a'))

        return ciphertext.upper()


    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        if len(ciphertext) % self.block_size != 0:
            raise Exception("Invalid cipher text")

        for i in range(0, len(ciphertext), self.block_size):

            char_array = np.array([])
            for j in range(i, i + self.block_size):
                letter_num = ord(ciphertext[j]) - ord('a')
                char_array = np.append(char_array, letter_num)

            result = np.matmul(char_array, self.inverse_key) % 26

            for letter_num in result:
                plaintext += chr(int(letter_num) + ord('a'))

        return plaintext


    @staticmethod
    def crack_cipher(plaintext, ciphertext, key_dimension):
        plaintext, ciphertext = plaintext.lower(), ciphertext.lower()
        plaintext = re.sub("[^a-z]+", "", plaintext)
        ciphertext = re.sub("[^a-z]+", "", ciphertext)

        # Define the coefficients of the equations in the form AX=B
        A = np.zeros((key_dimension, key_dimension)).astype('int')
        B = np.zeros((key_dimension, key_dimension)).astype('int')

        for i in range(key_dimension):
            for j in range(key_dimension):
                A[i][j] = ord(plaintext[i*key_dimension + j]) - ord('a')
                B[i][j] = ord(ciphertext[i*key_dimension + j]) - ord('a')

        A %= 26
        B %= 26

        # Solve the system of equations
        A_inverse = np.array(sp.Matrix(A).inv_mod(26))
        X = np.matmul(A_inverse, B) % 26
        return X

