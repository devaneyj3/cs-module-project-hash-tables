# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# dictionary of our cryptography translation
table = {
    "A" : "H",
    "B" : "Z",
    "C" : "Y",
    "D" : "W",
    "E" : "O",
    "F" : "R",
    "G" : "J",
    "H" : "D",
    "I" : "P",
    "J" : "T",
    "K" : "I",   
    "L" : "G",   
    "M" : "L",   
    "N" : "C",   
    "O" : "E",
    "P" : "X",   
    "Q" : "K",   
    "R" : "U",   
    "S" : "N",   
    "T" : "F",
    "U" : "A",   
    "V" : "M",   
    "W" : "B",   
    "X" : "Q",   
    "Y" : "V",
    "Z" : "S"
}

with open("ciphertext.txt") as f:
    words = f.read()

    chiper = ''
    # loop through each index of the words array
    for char in words:
        if char.isspace():
            chiper += ' '
        # we need to ignore special characters that do not have values
        if table.get(char) is not None:
        # if char does not have a key for ex, .,! continue
            chiper += table[char.upper()]
    print(chiper)
