import numpy as np

def generate_key(text):
    return [hex(e)[2:] for e in np.random.randint(0, 255, len(text))]

def encrypt(text1, text2):
    print("Text1:", text1)
    print("Text2:", text2)
    
    hex_text1 = [char.encode("cp1251").hex() for char in text1]
    hex_text2 = [char.encode("cp1251").hex() for char in text2]
    print("Text1 [hex]: ", *hex_text1)
    print("Text2 [hex]: ", *hex_text2)
    
    key = generate_key(text1)
    print("Hex key: ", *key)
    
    hex_encrypted_text1 = ["{:02x}".format(int(key[i], 16)^int(hex_text1[i], 16)) for i in range(len(hex_text1))]
    hex_encrypted_text2 = ["{:02x}".format(int(key[i], 16)^int(hex_text2[i], 16)) for i in range(len(hex_text2))]
    print("Encrypted text1 [hex]: ", *hex_encrypted_text1)
    print("Encrypted text2 [hex]: ", *hex_encrypted_text2)
    
    encrypted_text1 = bytearray.fromhex("".join(hex_encrypted_text1)).decode("cp1251")
    encrypted_text2 = bytearray.fromhex("".join(hex_encrypted_text2)).decode("cp1251")
    print("Encrypted text1: ", encrypted_text1)
    print("Encrypted text2: ", encrypted_text2)
    
    return key, encrypted_text1, encrypted_text2

def decrypt(encrypted_text1, encrypted_text2, text1):
    print("Encrypted text1:", encrypted_text1)
    print("Encrypted text2:", encrypted_text2)
    print("Text1:", text1)

    hex_encrypted_text1 = [char.encode("cp1251").hex() for char in encrypted_text1]
    hex_encrypted_text2 = [char.encode("cp1251").hex() for char in encrypted_text2]
    hex_text1 = [char.encode("cp1251").hex() for char in text1]
    print("Encrypted text1 [hex]: ", *hex_encrypted_text1)
    print("Encrypted text2 [hex]: ", *hex_encrypted_text2)
    print("Text1 [hex]: ", *hex_text1)
        
    hex_text2 = ["{:02x}".format(int(hex_encrypted_text1[i], 16)^int(hex_encrypted_text2[i], 16)^int(hex_text1[i], 16)) for i in range(len(hex_text1))]
    print("Text1 [hex]: ", *hex_text2)
  
    text2 = bytearray.fromhex("".join(hex_text2)).decode("cp1251")
    
    print("Text2:", text2)
    return text1, text2

test1 = "Some randome message #1"
test2 = "Another one text #18479"
test_key, test1_encrypted, test2_encrypted = encrypt(test1, test2)

test1_decrypted, test2_decrypted = decrypt(test1_encrypted, test2_encrypted, test1)

print("=========================")
print(test1)
print(test2)
print(test1_decrypted)
print(test2_decrypted)
print("=========================")
