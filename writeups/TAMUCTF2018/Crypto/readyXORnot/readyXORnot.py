#python3
from base64 import b64decode 
def decrypt(encrypted, key):
    decrypted = ""
    for i in range(len(encrypted)):
        decrypted += chr(encrypted[i] ^ key[i % len(key)])
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
key = xorBytes(originalData, decodedEncryptedData)
print('key: {}'.format(key))
decodedEncryptedFlag = b64decode(encryptedFlag)
flag = decrypt(decodedEncryptedFlag, key)
print('flag: {}'.format(flag))