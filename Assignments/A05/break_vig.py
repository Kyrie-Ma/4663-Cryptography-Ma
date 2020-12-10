import sys
import os
from frequency import Frequency
from math import log

freqWords = open("Assignments/A05/wordsByFrequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(freqWords)))) for i,k in enumerate(freqWords))
maxword = max(len(x) for x in freqWords)

def mykwargs(argv):
    args = []
    kargs = {}
    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def usage(message=None):    
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename]")
    print(f"Example:\n\t python {name} input=encrypted output=decrypted \n")
    sys.exit()

def English(message, words):
    tokens = message.split()
    score = 0
    for tok in tokens:
        if tok.upper() in words:
            score += 1
    return score / len(tokens)

def getKeyLength(ciphertext):
    ic_table=[]
    for guess_len in range(16):
      ic_sum=0.0
      avg_ic=0.0
      for i in range(guess_len):
        sequence=""
        # breaks the ciphertext into sequences
        for j in range(0, len(ciphertext[i:]), guess_len):
          sequence += ciphertext[i+j]
        
        # calls incidence_of_coincidence function for each sequence
        ic_sum+=incidence_of_coincidence(sequence)
      # don't want to divide by zero
      if (guess_len != 0):
        avg_ic=ic_sum/guess_len
      ic_table.append(avg_ic)

    # returns the index of most probable key length (highest IC)
    best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
    second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])
    
    if best_guess % second_best_guess == 0:
      return second_best_guess
    else:
      return best_guess
   
def getKey(keylength, check_Attempt,words):
    for i in range(len(words)):
        words[i] = words[i].strip()
    rightLength = []
    count = 0
    for word in words:
        if len(word) == keyLength:
            count += 1
            rightLength.append(word)
    key = rightLength[check_Attempt]
    return key

def incidenceOfCoincidence(sequence):
    if (len(sequence) > 1):
      F = Frequency()
      F.count(sequence)
      IncOfCoinc = 0
      FreqNum = 0
      length = len(sequence)
      for i in range(0,26):
        FreqNum = F.getNthNum(i)
        IncOfCoinc = IncOfCoinc + (FreqNum*(FreqNum - 1))
      IncOfCoinc = (IncOfCoinc / (length*(length - 1)))
      return IncOfCoinc
    else:
      return 0

def decrypt(ciphertext, key, plaintext):
    plaintext = ""
    ciphertext = ciphertext.lower()
    key = key.lower()
    i = 0
    for letter in ciphertext:
        a = ord(letter)-97
        b = ord(key[i])-97
        plaintext += chr(((a-b)%26) + 97)
        i = (i + 1) % len(key)
    return plaintext

def inferSpaces(s):
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k
    return " ".join(reversed(out))

if __name__=='__main__':
    _,params = mykwargs(sys.argv[1:])
    infile = params.get('input',None)
    outfile = params.get('output',None)
    if not infile and not outfile:
      usage()
    with open("Assignments/A05/words","r") as f:
      words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()
    with open(infile) as f:
        ciphertext = f.read()
    plaintext = ""
    keyLength = getKeyLength(ciphertext)
    check_Again = 1
    check_Attempt = 0
    while (check_Again == 1):
      check_Attempt = check_Attempt + 1
      key = getKey(keyLength, check_Attempt, words)
      plaintext = decrypt(ciphertext, key, plaintext)
      plaintext = inferSpaces(plaintext)
      ratio = English(plaintext,words)
      if (ratio >= 0.8):
        check_Again = 0     
    print(plaintext)
