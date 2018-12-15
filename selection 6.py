#Skeleton file for HW6 - winter 2016 - extended intro to CS

#Add to this file your implementation.

#Change the name of the file to your ID number (extension ".py").



#QUESTION 1
def extend_fingerprints(text, fingers, length, basis=2**8, r=2**17-1):
    for i in range(len(fingers)-1):
        fingers[i] = (fingers[i] * basis + ord(text[i + length - 1])) % r
    fingers.pop() 


def make_hashtable(fingers, table_size):
    table = [ [] for i in range(table_size)]
    for i in range(len(fingers)):
        table[fingers[i]].append(i)
    return table


def has_match(text1, text2, fingers1, fingers2, t, r):
    fngHash1 = make_hashtable(fingers1, r)
    for i in range(len(fingers2)):
        for index in fngHash1[fingers2[i]]:
            subText1 = text1[index:index+t]
            subText2 = text2[i:i+t]
            if subText1 == subText2:
                return subText1
    return None
    

def find_longest(text1,text2,basis=2**8,r=2**17-1):
    match = ''
    l = 0 #initial "window" size
    #fingerprints of "windows" of size 0 - all are 0
    fingers1 = [0]*(len(text1)+1)
    fingers2 = [0]*(len(text2)+1)

    while match != None: #there was a common substring of len l
        l += 1
        extend_fingerprints(text1, fingers1, l, basis, r)
        extend_fingerprints(text2, fingers2, l, basis, r)
        match = has_match(text1,text2,fingers1,fingers2,l,r)
        print(match)
    return l-1


def format_text(text):
    return ''.join([c for c in text.lower() if c in "abcdefghijklmnopqrstuvwxyz.,!?:-"])


def test():
    
    fingers = [0,0,0,0,0,0]
    extend_fingerprints("hello", fingers, 1)
    if (fingers != [104, 101, 108, 108, 111]):
        print("error in extend_fingerprints")
    extend_fingerprints("hello", fingers, 2)
    if (fingers != [26725, 25964, 27756, 27759]):
        print("error in extend_fingerprints")
    extend_fingerprints("hello", fingers, 3)
    if (fingers != [26016, 93342, 27813]):
        print("error in extend_fingerprints")

    if (make_hashtable([0,0,1,2,1,2,1,2,3,3,3,0,0], 4) != [[0, 1, 11, 12], [2, 4, 6], [3, 5, 7], [8, 9, 10]]):
         print("error in make_hashtable")

    
