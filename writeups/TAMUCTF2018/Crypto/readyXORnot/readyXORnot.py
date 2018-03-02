from base64 import b64decode 
def decrypt(num, key):
    decrypted = ""
    for i in range(len(num)):
        decrypted += chr(num[i] ^ key[i % len(key)])
    return decrypted
def xorBytes(bytes1, bytes2):
    result = bytearray()
    for b1, b2 in zip(bytes1, bytes2):
        result.append(b1 ^ b2)
    return bytes(result)

originalData = b'El Psy Congroo'
encryptedData = "IFhiPhZNYi0KWiUcCls="
encryptedFlag = "I3gDKVh1Lh4EVyMDBFo="
decodedEncryptedData = b64decode(encryptedData)
repeatedKey = xorBytes(originalData, decodedEncryptedData)
print('repeated key: {}'.format(repeatedKey))
key = b'e4Bn'
decodedEncryptedFlag = b64decode(encryptedFlag)
flag = decrypt(decodedEncryptedFlag, key)
print('flag: {}'.format(flag))