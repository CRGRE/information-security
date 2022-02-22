import numpy as np

def generate_key(text):
    return [hex(e)[2:] for e in np.random.randint(0, 255, len(text))]
  
def encrypt_text(text, key):
    print("Original text: ", text)
    hex_text = [char.encode("cp1251").hex() for char in text]
    print("Original text [hex]: ", *hex_text)

    print("Key: ", *key)
    hex_crypted_text = ["{:02x}".format(int(key[i], 16)^int(hex_text[i], 16)) for i in range(len(hex_text))]
    print("Hex crypted text: ", *hex_crypted_text)
  
    crypted_text = bytearray.fromhex("".join(hex_crypted_text)).decode("cp1251")
    print("Crypted text: ", crypted_text)
    
    return crypted_text

def find_key_from_crypted(text, crypted_text):
    print("Original text: ", text, "\nCrypted Text: ", crypted_text)
    hex_text = [ch.encode("cp1251").hex() for ch in text]
    hex_crypted_text = [ch.encode("cp1251").hex() for ch in crypted_text]
    print("Hex Open Text: ", *hex_text)
    print("Hex Crypted Text: ", *hex_crypted_text)
    
    key = [hex(int(i,16)^int(j,16))[2:] for (i,j) in zip(hex_text, hex_crypted_text)]
    print("Key :", *key)
    
    return key

test = "С Новым Годом, друзья!"
test_key = generate_key(test)
test_encrypted = encrypt_text(test, test_key)

test_decrypted = encrypt_text(test_encrypted, test_key)
print("=========================")
print(test)
print(test_encrypted)
print(test_decrypted)
print("=========================")


print("=========================")
print(test)
print(test_encrypted)
print(*find_key_from_crypted(test, test_encrypted))
print("=========================")

