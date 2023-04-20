from shift_cipher import ShiftCipher
from permutation_cipher import PermutationCipher
from playfair_cipher import PlayfairCipher
from hill_cipher import HillCipher
from affine_cipher import AffineCipher
from substitution_cipher import SubstitutionCipher


# Auxiliary functions
def print_results(plaintext, ciphertext, deciphered_text):
    print(f"      Plain Text:  {plaintext}\n"
          f"     Cipher Text:  {ciphertext}\n"
          f" Deciphered Text:  {deciphered_text}\n")


def print_attack_results(plaintext, ciphertext, key):
    print(f"      Plain Text:  {plaintext}\n"
          f"     Cipher Text:  {ciphertext}\n"
          f"     Cracked Key:  {key}\n")


# Cipher test functions
def shift_cipher():
    plaintext = "This is how the shift cipher works"
    cipher = ShiftCipher(key=3)
    print(f"Shift Cipher example - Key: {cipher.key}")

    ciphertext = cipher.encipher(plaintext)
    deciphered_text = cipher.decipher(ciphertext)

    print_results(plaintext, ciphertext, deciphered_text)


def permutation_cipher():
    plaintext = "She sells seashells by the seashore"
    cipher = PermutationCipher(key_length=5)
    print(f"Permutation Cipher example - Key: {cipher.key}")

    ciphertext = cipher.encipher(plaintext)
    deciphered_text = cipher.decipher(ciphertext)

    print_results(plaintext, ciphertext, deciphered_text)


def playfair_cipher():
    plaintext = "She sells seashells by the seashore"
    cipher = PlayfairCipher(key="Monarchy")
    print(f"Playfair Cipher example - Key: {cipher.key}")

    ciphertext = cipher.encipher(plaintext)
    deciphered_text = cipher.decipher(ciphertext)

    print_results(plaintext, ciphertext, deciphered_text)


def hill_cipher():
    # 2x2 matrix
    plaintext = "She sells seashells"

    cipher_1 = HillCipher(key=[[7, 3], [2, 1]])
    print(f"Hill Cipher example 1 - Key:\n{cipher_1.key}")

    ciphertext_1 = cipher_1.encipher(plaintext)
    deciphered_text_1 = cipher_1.decipher(ciphertext_1)

    print_results(plaintext, ciphertext_1, deciphered_text_1)

    # 3x3 matrix
    cipher_2 = HillCipher(key=[[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    print(f"Hill Cipher example 2 - Key:\n{cipher_2.key}")

    ciphertext_2 = cipher_2.encipher(plaintext)
    deciphered_text_2 = cipher_2.decipher(ciphertext_2)

    print_results(plaintext, ciphertext_2, deciphered_text_2)


def affine_cipher():
    plaintext = "This is how the Affine cipher works"
    cipher = AffineCipher(key=(5, 17))
    print(f"Affine Cipher example - Key: (a, b) = {cipher.key}")

    ciphertext = cipher.encipher(plaintext)
    deciphered_text = cipher.decipher(ciphertext)

    print_results(plaintext, ciphertext, deciphered_text)


def substitution_cipher():
    plaintext = "Hello world"
    cipher = SubstitutionCipher()
    print(f"Substitution Cipher example Key: = {cipher.key}")

    ciphertext = cipher.encipher(plaintext)
    deciphered_text = cipher.decipher(ciphertext)

    print_results(plaintext, ciphertext, deciphered_text)


def crack_shift_cipher():
    print(f"Shift Cipher attack example")

    plaintext = "Classical encryption techniques are not secure"
    ciphertext = "FODVVLFDOHQFUBSWLRQWHFKQLTXHVDUHQRWVHFXUH"
    key = ShiftCipher.crack_cipher(plaintext, ciphertext)

    print_attack_results(plaintext, ciphertext, key)


def crack_affine_cipher():
    print(f"Affine Cipher attack example")

    plaintext = "Classical encryption techniques are not secure"
    ciphertext = "UXCIIWUCXMPUZKHRWYPRMUNPWQAMICZMPYRIMUAZM"
    key = AffineCipher.crack_cipher(plaintext, ciphertext)

    print_attack_results(plaintext, ciphertext, key)


def crack_hill_cipher():
    plaintext = "she sells eggs"

    print(f"Hill Cipher attack example - 3x3 matrix")
    ciphertext = "TYBWKTBZPEME"
    key = HillCipher.crack_cipher(plaintext, ciphertext, 3)

    print_attack_results(plaintext, ciphertext, key)


def main():
    print("Encryptions Samples:")
    shift_cipher()
    permutation_cipher()
    playfair_cipher()
    affine_cipher()
    hill_cipher()
    substitution_cipher()

    print("Cipher Attacks:")
    crack_shift_cipher()
    crack_affine_cipher()
    crack_hill_cipher()


if __name__ == "__main__":
    main()
