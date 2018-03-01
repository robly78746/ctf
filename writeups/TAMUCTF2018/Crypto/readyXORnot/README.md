# readyXORnot

## Description

original data: "El Psy Congroo"
encrypted data: "IFhiPhZNYi0KWiUcCls="
encrypted flag: "I3gDKVh1Lh4EVyMDBFo="

The flag is not in the traditional gigem{flag} format.

## Approach

From the name of the challenge, we can guess the data is encrypted with an [XOR cipher](https://en.wikipedia.org/wiki/XOR_cipher). We can get the key by xor'ing the original data with the decoded encrypted data because of the following rules of xor: x ^ x = 0; x ^ 0 = x; and x ^ y = y ^ x. In this case, plaintext ^ key = ciphertext and (plaintext ^ key) ^ plaintext = key ^ plaintext ^ plaintext = key ^ 0 = key. Therefore, ciphertext ^ plaintext will give us the key. We can use this key to decrypt the encrypted flag by xor'ing the decoded encrypted flag with the key.  

## Solution

```
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
key = xorBytes(originalData, decodedEncryptedData)
print('key: {}'.format(key))
decodedEncryptedFlag = b64decode(encryptedFlag)
flag = decrypt(decodedEncryptedFlag, key)
print('flag: {}'.format(flag))
```
```
key: b'e4Bne4Bne4Bne4'
flag: FLAG=Alpacaman
```
The flag is Alpacaman.