import re
def word_count(s):
    dict = {}
    special_characters = '":;,.-+=/\\|[]{}()*^&'
    word_split = s.lower().split()
    for word in word_split:
        # ignore \":;,.-+=/\|[]{}()*^& and get rid of ' in between start and finish of any word
        word = word.strip(special_characters)
        if not word:
            break
        # skips repeated word
        if word in dict:
            dict[word] = dict[word] + 1
        else: 
            dict[word] = 1
    return dict
# from collections import Counter
# def word_count(string):
#     # split input string separated by space
#     if ":;,.-+=/\\|[]{}()*^&'" not in string:
#         return dict
#     string = string.split(" ")
#     # joins two adjacent elements in iterable way
#     for i in range(0, len(string)):
#         string[i] = "".join(string[i])
#     # now create dictionary using counter method
#     # which will have strings as key and their frequencies as value
#     UniqW = Counter(string)
#     # joins two adjacent elements in iterable way
#     s = " ".join(UniqW.keys())
#     return s


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))