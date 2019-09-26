# Reversible Sneaky Algorithm #0

## Description

125 points

Yavan sent me these really large numbers... what can they mean? He sent me the cipher "c", the private key "d", and the public modulus "n". I also know he converted his message to a number with ascii. For example:

"nactf" --> \x6e61637466 --> 474080310374

Can you help me decrypt his cipher?

The20thDuck

Hint: Read about RSA at https://en.wikipedia.org/wiki/RSA_(cryptosystem)

Hint: If you're new to RSA, you may want to try this tool: https://www.dcode.fr/modular-exponentiation

If you like python, try the pow() function!

rsa.txt

## Approach

We are given rsa.txt which contains n, d, and c. With these three numbers, we can decrypt the ciphertext c into plaintext with the operation c ^ d mod n. In python, we can use the pow function. pow(c,d,n) will raise c to the power of d and take the remainder after dividing by n. Then, we can convert the number to ascii by using int.to_bytes function and specify big endian byte order.

## Solution

Run RSA#0 script and we get the flag nactf{w3lc0me_t0_numb3r_th30ry}