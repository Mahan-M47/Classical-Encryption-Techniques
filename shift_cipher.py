
class ShiftCipher:
    def __init__(self, key):
        self.key = key % 26

    def set_key(self, key):
        self.key = key % 26

    def encipher(self, plaintext):
        plaintext = plaintext.lower()
        ciphertext = ""

        for letter in plaintext:
            letter_num = ord(letter) - 97               # the ascii number of 'a' is 97
            letter_num = (letter_num + self.key) % 26
            ciphertext += chr(letter_num + 97)

        return ciphertext.upper()

    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        for letter in ciphertext:
            letter_num = ord(letter) - 97               # the ascii number of 'a' is 97
            letter_num = (letter_num - self.key) % 26
            plaintext += chr(letter_num + 97)

        return plaintext

    @staticmethod
    def crack_cipher(plaintext, ciphertext):
        p = plaintext[0].lower()
        c = ciphertext[0].lower()
        key = (ord(c) - ord(p)) % 26
        return key

