import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = list.copy(chars)
random.shuffle(key)

# encrypt
plain_text = input("Enter the text you want to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"The original text is : {plain_text}")
print(f"The encrypted text is : {cipher_text}")

# decrypt
cipher_text = input("Enter the text you want to decrypt: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"The encrypted text is : {cipher_text}")
print(f"The decrypted text is : {plain_text}")
