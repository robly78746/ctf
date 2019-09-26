# Vyom's Soggy Croutons

## Description

50 points

Vyom was eating a CAESAR salad with a bunch of wet croutons when he sent me this:

ertkw{vk_kl_silkv}

Can you help me decipher his message?

The20thDuck

Hint: You don't have to decode it by hand -- Google is your friend!

## Approach

From the description of the challenge, we can guess Vyom used a Caesar cipher. We can google for a decoder and brute force the shift until we get a plaintext in the format of the flag.

## Solution

I used [Cryptii](https://cryptii.com/pipes/caesar-cipher) to decode. I incremented the shift until the plaintext was nactf{et_tu_brute}. This cipher had a shift of 17.