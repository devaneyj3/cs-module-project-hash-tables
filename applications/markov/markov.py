import random
def review_generator():
    with open("input.txt") as f:
        words = f.read()
    # converting array to string with join operator 
    reviews = ''.join([i for i in words if str(i)]).replace("\n", " ").split(' ')
    
    index = 1
    chain = {}
    count =  input('How word would you like to add? ')
    
    
    for word in reviews[index:]:
        key = reviews[index-1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < ord('a'):
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    return message
print(review_generator())

# dict = {}
# # 1. Read the file `input.txt` and split it into words.
# with open("input.txt") as f:
#     words = f.read()
# paragraph_arr = words.split()
# print(paragraph_arr)
# for word in paragraph_arr:
#     # dict[word] = word
    
# # 3. Choose a random "start word" to begin.
# # random_word = random.choice(dict[word])
# # print(random_word)
# # print(dict)
#     for same_word in paragraph_arr:
#         # if two words in a sentence are identical
#         # dict[word] 
#         if word == same_word:
#             # if only one occurrence the word after it is its value  
#             dict[word] = same_word
# print(dict)



# 2. Analyze the text, building up the dataset of which words can follow
#    particular words.

#    (Hint: leave duplicates in for this part. If a the word `and` is seen
#    following the word `goats` multiple times, include all those `and`s.
#    It'll give more convincing results because it is modelling the
#    _frequency_ of _how often_ a word follows another word.)


# 4. Loop through:
# Hints:

# * `random.choice()` can choose a random word out of a list.
# * `print(s, end=" ")` will print a space after every word instead of a
#   newline.

    

