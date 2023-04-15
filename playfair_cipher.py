
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class PlayfairCipher:
    def __init__(self, key):
        self.key = key.lower()
        self.alphabet = alphabet.copy()

        if self.is_key_valid():
            self.key_matrix = self.generate_key_matrix()
        else:
            raise Exception("Invalid key")


    def is_key_valid(self):
        char_set = []
        if 'i' in self.key and 'j' in self.key:
            return False
        elif 'j' in self.key:
            self.alphabet.remove('i')
        else:
            self.alphabet.remove('j')

        for char in self.key:
            if char in char_set:
                return False
            else:
                char_set.append(char)
                self.alphabet.remove(char)

        return True


    def generate_key_matrix(self):
        key_matrix = [[None for i in range(5)] for j in range(5)]
        all_characters = self.key
        for char in self.alphabet:
            all_characters += char

        for i in range(5):
            for j in range(5):
                key_matrix[i][j] = all_characters[5*i+j]

        return key_matrix


    def find_char_indices(self, char):
        for i in range(5):
            for j in range(5):
                if self.key_matrix[i][j] == char:
                    return i, j


    def find_pairs(self, plaintext):
        pairs = [plaintext[2 * i:2 * (i + 1)] for i in range(len(plaintext) // 2)]

        i = 0
        while i < len(pairs):
            pair = pairs[i]
            if pair[0] == pair[1]:
                pair_0 = pair[0] + 'x'
                pair_1 = 'x' + pair[1]
                pairs.pop(i)
                pairs.insert(i, pair_0)
                i += 1
                pairs.insert(i, pair_1)
            i += 1

        return pairs


    def encipher(self, plaintext):
        plaintext = plaintext.lower()
        if 'i' in self.alphabet:
            plaintext = re.sub('j', 'i', plaintext)
        else:
            plaintext = re.sub('i', 'j', plaintext)

        ciphertext = ""

        if len(plaintext) % 2 == 1:
            plaintext += 'x'

        pairs = self.find_pairs(plaintext)

        for pair in pairs:
            i_0, j_0 = self.find_char_indices(pair[0])
            i_1, j_1 = self.find_char_indices(pair[1])

            if i_0 == i_1:
                cipher_j_0 = (j_0 + 1) % 5
                cipher_j_1 = (j_1 + 1) % 5

                cipher_i_0 = i_0
                cipher_i_1 = i_1

            elif j_0 == j_1:
                cipher_i_0 = (i_0 + 1) % 5
                cipher_i_1 = (i_1 + 1) % 5

                cipher_j_0 = j_0
                cipher_j_1 = j_1

            else:
                cipher_i_0 = i_0
                cipher_j_0 = j_1

                cipher_i_1 = i_1
                cipher_j_1 = j_0

            ciphertext += self.key_matrix[cipher_i_0][cipher_j_0] + self.key_matrix[cipher_i_1][cipher_j_1]

        return ciphertext.upper()


    def decipher(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        pairs = self.find_pairs(ciphertext)

        for pair in pairs:
            i_0, j_0 = self.find_char_indices(pair[0])
            i_1, j_1 = self.find_char_indices(pair[1])

            if i_0 == i_1:
                cipher_j_0 = (j_0 - 1) % 5
                cipher_j_1 = (j_1 - 1) % 5

                cipher_i_0 = i_0
                cipher_i_1 = i_1

            elif j_0 == j_1:
                cipher_i_0 = (i_0 - 1) % 5
                cipher_i_1 = (i_1 - 1) % 5

                cipher_j_0 = j_0
                cipher_j_1 = j_1

            else:
                cipher_i_0 = i_0
                cipher_j_0 = j_1

                cipher_i_1 = i_1
                cipher_j_1 = j_0

            plaintext += self.key_matrix[cipher_i_0][cipher_j_0] + self.key_matrix[cipher_i_1][cipher_j_1]

        plaintext = re.sub('xx', '', plaintext)
        return plaintext
