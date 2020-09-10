import random


dict = {}
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
paragraph_arr = words.split()

# for every word keep track of the word after it
count = 0
while count < len(paragraph_arr):
    starting_word = paragraph_arr[count]
    dict[starting_word] = starting_word
    count += 1
print(dict)
    

# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

