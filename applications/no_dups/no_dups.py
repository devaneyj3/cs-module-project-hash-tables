import re 
def no_dups(s):
    no_repeats = {}
    # seperate into an array
    seperate = re.split('\s+', s)
    for word in seperate:
        # check if the subsequent word is not in no_repeats and add to 
        if word not in no_repeats:
            no_repeats[word] = word
        # if words are the same, force it to check again
        else: continue
    # convert into string on commas and replace commas with space
    no_repeats = ','.join(no_repeats).replace(',', ' ')
    return no_repeats



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))