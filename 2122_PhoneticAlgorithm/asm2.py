# COMP 1026 â€“ Assignment 3

# Dada Nguyen

# Write a program using lists and functions to compare names using a phonetic algorithm


#  to get names from the user
def getSoundex():

	names = []
	userInput = input()
	while userInput != 'DONE':
		names.append(userInput)
		userInput = input()
	return names

# to convert names to digits
def convertDigits(name):

    decoding_list = ['aeiouyhw', 'bfpv', 'cgjkqsxz', 'dt', 'l', 'mn', 'r']
    D = ''
    for char in name:
        for key in decoding_list:
            if char in key:
                D += str(decoding_list.index(key))
    return D

# to remove repetitive digits
def repDigits(D):

    D_new = D[0]
    D_len = len(D)
    for i in range(1, D_len):
        if D[i-1] == D[i]:
            continue
        D_new += D[i]
    return D_new

# to edit the length
def soundexLength(D):
    while len(D) > 4:
        D = D[:4]
    while len(D) < 4:
        D += '0'
    return D

# to encode the names
def encodeSoundex(word):

# to put F in front of digits
    F = word[0].lower()
    D = convertDigits(word.lower())
    D = repDigits(D)

# to remove 0
    D = D.replace('0', '')
    firstDigit = convertDigits(F)

# to replace F
    if D == '':
        D = firstDigit
    elif firstDigit == D[0]:
        D = D[1:len(D)]
        D = F + D
    else:
        D = F + D
    D = soundexLength(D)
    return D

# to compare the soundex of names

def comparison():
    soundexList = []
    print('Enter names, one on each line. Type DONE to quit entering names.')

# to convert to soundex
    nameList = []
    for name in getSoundex():
        soundexTuple = (name, encodeSoundex(name))
        soundexList.append(soundexTuple)

    for i in range(len(soundexList)):
        for j in range(len(soundexList)):
            if i != j:
                # to put names in the alphabetical order
                if soundexList[i][1] == soundexList[j][1]:
                    alphaOrder1 = min(soundexList[i][0], soundexList[j][0])
                    alphaOrder2 = max(soundexList[i][0], soundexList[j][0])
                    order = '{} and {} have the same Soundex encoding.'.format(alphaOrder1, alphaOrder2)
                    if order not in nameList:
                        nameList.append(order)

# to sort
    if len(nameList) > 0:
        nameList = ('\n'.join(sorted(nameList)))
        print(nameList)

comparison()