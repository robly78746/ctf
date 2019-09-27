# Reversible Sneaky Algorithm #1

## Description

275 points

Lori decided to implement RSA without any security measures like random padding. Must be deterministic then, huh? Silly goose!

She encrypted a message of the form nactf{****} where the redacted flag is a string of 4 lowercase alphabetical characters. Can you decrypt it?

As in the previous problem, the message is converted to a number by converting ascii to hex.

The20thDuck

Hint: The flag seems pretty short... can you brute-force it?

[ReversibleSneakyAlgorithm.txt](./ReversibleSneakyAlgorithm.txt)

## Approach

We are given the public key, e and the modulus n, and the ciphertext c. Since the length of the unknown part of the flag is so short and we are told the missing piece is 4 lowercase alphabetical characters, we can brute force the flag by encrypting a guess and comparing it to the ciphertext c. In python, we can use itertools product method with the letters a-z and set the repeat parameter to 4. The cartesian product ensures we try sequences of repeated letters like 'aabb' and all permutations.

## Solution

Run the code and we get nactf{pkcs}