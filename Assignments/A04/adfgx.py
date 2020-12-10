# python3 Assignments/A04/adfgx.py input="Assignments/A04/plaintext" output="Assignments/A04/cipherText" op=encrypt key1=superbad key2=campus
import sys
import math
import os
from polybius import AdfgxLookup

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

def getMessage(text, key1):
    A = AdfgxLookup(key1)
    lookup = A.build_polybius_lookup()
    A.sanity_check()
    message = ''
    for c in text:
      message = (message + ' ' + lookup[c] + ' ')
    print("")
    message = message.replace(' ','')
    print(message)
    return message

def encryptMessage(message):
    key2_length = len(key2)             
    message_length = len(message)       
    rows = math.ceil(float(message_length)/float(key2_length))
    matrix = {}
    for k in key2:
          matrix[k] = []
    i = 0
    for m in message:
        matrix[key2[i]].append(m)
        i += 1
        i = i % len(key2)      
    print("")
    printMatrix(matrix,rows)
    temp_matrix = sorted(matrix.items())
    print("")
    sorted_matrix = {}
    for item in temp_matrix:
        sorted_matrix[item[0]] = item[1]
    printMatrix(sorted_matrix,rows)
    print("")
    printMessage(sorted_matrix,key2)
    
def encrypt():
    with open(input) as f:
      text = f.read()
    text = text.lower()
    print("Plain text: " + text)
    text = text.replace(' ','')
    codedMessage = getMessage(text, key1)
    encryptMessage(codedMessage)

def printMatrix(matrix,rows):
    for k in matrix:
        print(k, end = '_')
    print("")
    for k in matrix:
        print('-',end=' ')
    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")
   
def printMessage(matrix,key2word):
    ofile = open(output, "w")
    i = 1
    for k in sorted(key2word):
      for d in matrix[k]:
        print(d,end='') 
        ofile.write(d)
        if i % 2 == 0:
            print(' ',end='')
            ofile.write(' ')
        i += 1
    print("")

def decrypt():
    with open(output) as f:
      cipherText = f.read()
    cipherText = cipherText.replace(' ','')
    infile = open(input, "w")
    print("")
    print("Cyphered Text is " + cipherText)
    print("")
    key2_length = len(key2)
    cipherText_length = len(cipherText)
    rows = math.ceil(float(cipherText_length)/float(key2_length))
    matrix = {k: [] for k in sorted(list(key2))}
    long_cols = cipherText_length % key2_length
    col_length = cipherText_length // key2_length
    long_cols_lookup = []
    short_cols_lookup = []
    for index, column in enumerate(key2):          
      if index < long_cols:
        long_cols_lookup.append(key2[index])
      else:
        short_cols_lookup.append(key2[index])
    tempKey2 = sorted(key2)
    long_cols_length = col_length + 1
    i = 0
    for index, column in enumerate(tempKey2): 
      if tempKey2[index] in long_cols_lookup:
        for _ in range(long_cols_length):
          matrix[column].append(cipherText[i])
          i += 1
      if tempKey2[index] in short_cols_lookup:
        for _ in range(col_length):
          matrix[column].append(cipherText[i])
          i += 1
    printMatrix(matrix, rows)
    print("")
    temp_matrix = { k: matrix[k] for k in key2 }
    printMatrix(temp_matrix,rows)
    print("")
    message = ''
    for r in range(rows):
        for k in temp_matrix:
            if r < len(temp_matrix[k]):
                message = message + temp_matrix[k][r]
    print("Message is " + message)
    pText = getPlaintext(message, key1)
    print("Plain text is " + pText)
    infile.write(pText)

def getPlaintext(text, key1):
    B = AdfgxLookup(key1)
    lookup2 = B.build_polybius_lookup()
    reverse_lookup = {value : key for (key, value) in lookup2.items()}
    B.sanity_check()
    pText = ''
    twoLetters = ""
    i = 1
    for c in text:
      twoLetters = twoLetters + c
      mod = i % 2
      if mod == 0:
        newLetter = reverse_lookup[twoLetters]
        pText = (pText + newLetter)
        twoLetters = ""
      i = i + 1
    print("")
    print(pText)
    return pText
    
def usage():
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename] [key=string] [op=encrypt/decrypt]")
    print(f"Example:\n\t python {name} input=INPU output=OUTPU op=encrypt key1=machine key2=trex \n")
    sys.exit()

if __name__ == "__main__":
    _,params = mykwargs(sys.argv[1:])
    input = params.get("input", None)
    output = params.get("output", None)
    operation = params.get("op", None)
    key1 = params.get("key1", None)
    key2 = params.get("key2", None)
    if not input and not output and not operation and not key1 and not key2:
        usage()
    if operation == "encrypt":
        encrypt()
    elif operation == "decrypt":
        decrypt()
    else:
        usage()
