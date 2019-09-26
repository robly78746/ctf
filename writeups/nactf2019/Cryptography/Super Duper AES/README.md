# Super Duper AES

## Description

250 points

The Advanced Encryption Standard (AES) has got to go. Spencer just invented the Super Duper Advanced Encryption Standard (SDAES), and it's 100% unbreakable. AES only performs up to 14 rounds of substitution and permutation, while SDAES performs 10,000. That's so secure, SDAES doesn't even use a key!

The20thDuck

Hint: Spencer used this video as inspiration for Super Duper AES: https://www.youtube.com/watch?v=DLjzI5dX8jc

[cipher.txt](./cipher.txt)
[sdaes.py](./sdaes.py)

## Approach

After looking at the code in sdaes.py and looking at the video in the hint, we can see that each operation in the super duper AES is invertible. We can reverse the substitute, permute, and round methods. Writing and testing these separately made the process simple. Reversing the methods mainly involved changing indexing the array to finding the index of the element with list's index method.

## Solution

Run the code and we decrypt the ciphertext to get nactf{5ub5t1tut10n_p3rmutat10n_n33d5_a_k3y} with padding.