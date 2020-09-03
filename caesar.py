import sys

def user_input(init_key):

    key = init_key
    message = raw_input("Enter message to encode\n$ ")

    c = 0
    if key > 26:
        c = key / 26
        c = (key - (26 * c))
        key = c

    return key, message


def encrypt(key, message):
    crypt_message = ""

    for i in range(0, len(message)):

        if message[i].isalpha():
            if ord(message[i]) + key > 90 and ord(message[i]) < 97:
                x = ord(message[i]) + key - 90
                crypt_message = crypt_message + chr(64 + x)
            elif ord(message[i]) + key > 122:
                x = ord(message[i]) + key - 122
                crypt_message = crypt_message + chr(96 + x)
            else:
                crypt_message = crypt_message + chr(ord(message[i]) + key)
        else:
            crypt_message = crypt_message + message[i]

    return crypt_message


def decrypt(key, crypt_message):
    decrypt_message = ""

    x=0
    for i in range(0, len(crypt_message)):

        if crypt_message[i].isalpha():

            if ord(crypt_message[i]) - key < 65:
                x = ord(crypt_message[i]) - 65
                x = 91 - (key - x)
                decrypt_message = decrypt_message + chr(x)

            elif ord(crypt_message[i]) - key < 97 and ord(crypt_message[i]) > 96:
                x = ord(crypt_message[i]) - 97
                x = 123 - (key - x)
                decrypt_message = decrypt_message + chr(x)

            else:
                decrypt_message = decrypt_message + chr(ord(crypt_message[i]) - key)

        else:
            decrypt_message = decrypt_message + crypt_message[i]

    return decrypt_message