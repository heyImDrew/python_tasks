"""
Edward Snowden knows that NSA agents use the following algorithm to cypher their messages.

1) They delete all spaces and punctuation marks.
2) They replace all successive identical letters by one such letter.
3) They insert two identical letters at an arbitrary place many times.

Snowden has intercepted some messages which are "meaningless" sequences of letters that NSA agent
 Bob has sent to other NSA agent Alice about possible Snowden's location. He wants to be able to restore
 the message as it was after step 2). Help Snowden write a program in Python that removes all pairs of
 identical letters from the message inserted at the third step. 

The program should be executed by calling 'python snowden.py cipheredmessage.txt' from
 Unix shell where "cipheredmessage.txt" is the name of a file with a ciphered message sent by Bob. 
 The message consists of lowercase English letters and its length is at most 100 000. Output the 
 message after step 2). The program should produce an answer in less than a few seconds.

Example
Execute: python snowden.py somefile.txt
somefile.txt: wwsndaadowffdennn
Output: snowden
"""

txt = 'wwsndaadowffdennn' #Our text

#Here we are trying to found at least one pair at text, if found return its index, if not returns -1
def havePairAt(text): 
    for index in range(len(text)-1):
        if text[index]==text[index+1]:
            return index
    return -1

#Using havePairAt(text) function removing all the pairs step by step
def step_3(text):
    text = [letter for letter in text]
    while havePairAt(text)!=-1:
        for index in range(len(text)):
            if index==havePairAt(text):
                text[index]=''
                text[index+1]=''
                text = [letter for letter in text if letter != '']
                break
    return ''.join(text)

#Working example
print(step_3(txt))