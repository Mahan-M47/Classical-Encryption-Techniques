
import sympy as sp


class AffineCipher:
    def __init__(self, key):
        self.key = (key[0] % 26, key[1] % 26)


    def encipher(self, plaintext):
        plaintext = plaintext.lower()
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

        a_1 = sp.mod_inverse(self.key[0], 26)
        print(a_1)
        b = self.key[1]

        for letter in ciphertext:
            letter_num = ord(letter) - ord('a')               # the ascii number of 'a' is 97
            letter_num = a_1*(letter_num - b) % 26
            plaintext += chr(letter_num + ord('a'))

        return plaintext


    @staticmethod
    def crack_cipher(plaintext, ciphertext):
        p = plaintext[0].lower()
        c = ciphertext[0].lower()
        key = (ord(c) - ord(p)) % 26
        return key

