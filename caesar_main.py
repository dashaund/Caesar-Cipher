import sys
import caesar

if len(sys.argv) == 1:
    print("Please input the key as argument")
    sys.exit()
elif len(sys.argv) > 2:
    print("This program only takes one key as argument, please try again")
    sys.exit()
elif not sys.argv[1].isdigit():
    print("The key must be a non-zero positive integer, please try again")
    sys.exit()
elif sys.argv[1].isdigit() and int(sys.argv[1]) <= 0:
    print("The key must be a non-zero positive integer, please try again")
    sys.exit()

init_key = int(sys.argv[1])
(key, message) = caesar.user_input(init_key)
print(key)
crypt_message = caesar.encrypt(key, message)
decrypt_message = caesar.decrypt(key, crypt_message)
print(crypt_message)
print(decrypt_message)