# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import collections

d = collections.OrderedDict()
with open("ciphertext.txt") as f:
    words = f.read()
    
words = words.split()

# loop through each index of the words array
for word in words:
    # loop through each letter in tha index
    for letter in word:
        print(letter)
        # For every letter find the replacement letter of it based on frequency analysis
# print(words)


# Your code here

