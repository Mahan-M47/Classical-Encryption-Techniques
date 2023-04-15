from shift_cipher import ShiftCipher
from permutation_cipher import PermutationCipher
from playfair_cipher import PlayfairCipher
from hill_cipher import HillCipher
from affine_cipher import AffineCipher


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def shift_cipher():
    pass


def permutation_cipher():
    pass


def playfair_cipher():
    pass


def main():
    pass


if __name__ == "__main__":
    # cipher = PermutationCipher(5)
    # print(cipher.encipher('hello'))
    # print(cipher.decipher(cipher.encipher('hello')))

    # cipher = PlayfairCipher('Monarchy')
    # print(cipher.encipher('hellomynameismahan'))
    # print(cipher.decipher('CFSUUSNOGYROFKLAOBRA'))

    # cipher = HillCipher([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    # print(cipher.encipher('shesellsa'))
    # print(cipher.decipher('TYBWKTTRR'))

    # cipher = HillCipher([[7, 3], [2, 1]])
    # print(cipher.encipher('shesellsa'))
    # print(cipher.decipher('KJMEYXJZUX'))

    cipher = AffineCipher((3,3))
    print(cipher.encipher("abcd"))
    print(cipher.decipher("DGJM"))

    main()
