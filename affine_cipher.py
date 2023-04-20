
import sympy as sp
import numpy as np
import re
from math import gcd


class AffineCipher:
    def __init__(self, key):
        self.key = (key[0] % 26, key[1] % 26)
        if not self.is_key_valid():
            raise Exception("Invalid key. in \"ax + b\" , a must be coprime with 26.")


    def is_key_valid(self):
        return gcd(self.key[0], 26) == 1


    def encipher(self, plaintext):
        plaintext = plaintext.lower()
        plaintext = re.sub("[^a-z]+", "", plaintext)

        ciphertext = ""

        a = self.key[0]
        b = self.key[1]

        for letter in plaintext:
            letter_num = ord(letter) - ord('a')               # the ascii number of 'a' is 97
            letter_num = (a*letter_num + b) % 26
            ciphertext += chr(letter_num + ord('a'))

        return ciphertext.upper()


    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        a_inverse = sp.mod_inverse(self.key[0], 26)
        b = self.key[1]

        for letter in ciphertext:
            letter_num = ord(letter) - ord('a')
            letter_num = a_inverse*(letter_num - b) % 26
            plaintext += chr(letter_num + ord('a'))

        return plaintext


    @staticmethod
    def crack_cipher(plaintext, ciphertext):
        plaintext, ciphertext = plaintext.lower(), ciphertext.lower()
        p_1, c_1 = plaintext[0], ciphertext[0]
        p_2, c_2 = None, None

        for letter in plaintext:
            if p_1 != letter:
                p_2 = letter
                break

        for letter in ciphertext:
            if c_1 != letter:
                c_2 = letter
                break

        p_1 = ord(p_1) - ord('a')
        p_2 = ord(p_2) - ord('a')
        c_1 = ord(c_1) - ord('a')
        c_2 = ord(c_2) - ord('a')

        # Define the coefficients of the equations in the form AX=B
        A = np.array([[p_1, 1], [p_2, 1]])  # Coefficients matrix
        B = np.array([c_1, c_2])  # Constants vector

        # Solve the system of equations
        A_inverse = np.array(sp.Matrix(A).inv_mod(26))
        X = np.matmul(A_inverse, B) % 26

        X[0] %= 26
        X[1] %= 26

        key = (int(X[0]), int(X[1]))
        return key

