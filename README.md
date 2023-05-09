# Krypton4
A walkthrough of a solution to the Krypton4 cipher game at overthewire[.]org

# DISCLAIMER
In the spirit of the game, you will find no password here. 

# From the game's webpage:

Good job!
You more than likely used some form of FA and some common sense to solve that one.
So far we have worked with simple substitution ciphers. They have also been ‘monoalphabetic’, meaning using a fixed key, and giving a one to one mapping of plaintext (P) to ciphertext (C). Another type of substitution cipher is referred to as ‘polyalphabetic’, where one character of P may map to many, or all, possible ciphertext characters.
An example of a polyalphabetic cipher is called a Vigenère Cipher. It works like this:
If we use the key(K) ‘GOLD’, and P = PROCEED MEETING AS AGREED, then “add” P to K, we get C. When adding, if we exceed 25, then we roll to 0 (modulo 26).
P P R O C E E D M E E T I N G A S A G R E E D\
K G O L D G O L D G O L D G O L D G O L D G O\
becomes:
P 15 17 14 2 4 4 3 12 4 4 19 8 13 6 0 18 0 6 17 4 4 3\
K 6 14 11 3 6 14 11 3 6 14 11 3 6 14 11 3 6 14 11 3 6 14\
C 21 5 25 5 10 18 14 15 10 18 4 11 19 20 11 21 6 20 2 8 10 17\
So, we get a ciphertext of:
VFZFK SOPKS ELTUL VGUCH KR
This level is a Vigenère Cipher. You have intercepted two longer, english language messages (American English). You also have a key piece of information. You know the key length!
For this exercise, the key length is 6. The password to level five is in the usual place, encrypted with the 6 letter key.
Have fun!

# Approach

The game describes a polyalphabetic cipher simply. A key of length 6 is used to encrypt the plaintext, recycling the key every time the end of it is reached. 

To make a point of how a Vigenère cipher is an improvement upon a monoalphabetic cipher, lets conduct a general frequency analysis of the text. 

The Cryptanalysis.py python script in this repository conducts a generic frequency anaylsis as well as a more targeted analysis which will be discussed shortly.
Here is the output from the generic frequency analysis, similar to the one we ran in the krypton3 game:
![image](https://github.com/Keen1/Krypton4/assets/20232809/bc738d6e-b83a-4a7d-9131-a3a74fb3eb5b)

We can see the distribution of letters among the cipher text is much better, and making a guess at any letter in the key is a blind guess with just this analysis. 
We need to take into account that the key length is given. If we know the key length, a more refined frequency analysis is possible. 

At this point I must make a point to state that I may have overlooked standard python modules that accomplish the same as the Bucket class in this repository. However, this implementation suffices for the purposes of this game.

The Bucket class accounts for the fact that each letter in the key is on its own a variable, with 26 possibilities for each letter. This script compiles each found file on the game server into one in 6 letter increments, the same length as the key. 

Taking a step back, we can look at a Vigenère cipher as a monoalphabetic cipher repeated for each length of the key. If we examine and compute a frequency analysis on each "bucket" or letter variable in the key, a more telling story is told:
![image](https://github.com/Keen1/Krypton4/assets/20232809/3f75b84f-d6b9-492b-b690-9e5b95626803)

The remaining buckets are left out for brevity, but have similiar frequency distributions. We can see the frequency dstribution for the first two buckets are much more similar to the one we saw in Krypton3. This is because each bucket can be thought of as a  monoalphabetic cipher on its own, since the actual key of the Vigenère never changes; it is only iterated over for each letter of the ciphertext and repeated til the end of the file. Using the previous resources for frequency distributions of the English language, we can make guesses at the shift the key is making and attempt to decrypt the password:

![image](https://github.com/Keen1/Krypton4/assets/20232809/d649854e-c991-489b-9e94-615dd3ff8223)

We are in.

