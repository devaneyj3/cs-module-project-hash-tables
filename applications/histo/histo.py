import collections

d = collections.OrderedDict()
with open("robin.txt") as f:
    words = f.read()
    
words = words.split()

# Print a histogram showing the word count for each word, one hash mark for every occurrence of the word.
for word in words:
    # Ignore each of the following characters:
    # " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    word = word.strip('":;,.-+=/\\|[]{}()*^&!?''')
    # Case should be ignored, and all output forced to lowercase.
    word = word.lower()
    if word in d:
        d[word] = d[word] + '#'
    else: 
        d[word] = '#'

# The hash marks should be left justified two spaces after the longest word.
# find longest word
longest_word = '' 
for key in d.keys():
    if len(key) > len(longest_word):
        longest_word = key
# Output will be first ordered by the number of words, then by the word (alphabetically).
# get dictionary sorted by values
for w in sorted(d, key=d.get, reverse=False):
    # How do I do this based on the longest word
    print(f'{w:<20} {d[w]}')

# If the input contains no ignored characters, print nothing.