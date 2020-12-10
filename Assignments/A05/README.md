## Assignment 5 - Vigenere Cracking

You will be given 1 or more encrypted files. You know the files were encrypted using the Vigenère method. You also know that the key used is an english dictionary word with a length 2-16 inclusive.
Write a python program that will 1) discover the size of that dictionary word (keylength) and then determine which word was used to encrypt your file(s).
To find the keylength you can use the Index of Coincidence (I.C.) described breifly below, but more thoroughly at the link provided.
Incidence of Coincidence

Dictionary Attack
Using the dictionary provided here and your newly discovered keylength, find all words in the dictionary of same length and proceed to brute force your way into decrypting the ciphertext. How will you know when you have achieved your decryption? Maybe this will help: https://www.python-course.eu/naive_bayes_classifier_introduction.php. You don't have to use the bayes classifier but it will make life easier. You could simply write your own probability function that assigns a value between 0,1 based on how many words you find in the dictionary .... expensive!

## Requirements
  You will be given one or more file(s) with an encrypted message in the file.
  Process each file and:
  print the key-length first
  print the keyword when found
  print the first 50 words of the message after decryption
  You must run your program like the following:  python break_vig.py input_file=input 

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/break_vig.py" > break_vig.py | break_vig.py      |
|   2   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/vigenere.py" > vigenere.py | vigenere.py      |
|   3   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/frequency.py" > frequency.py | frequency.py      |
|   4   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/encrypted.txt" > encrypted.txt | encrypted.txt      |
|   5   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/decrypted.txt" > decrypted.txt | decrypted.txt      |
|   6   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/dictionary_words.txt" > dictionary_words.txt | dictionary_words.txt      |
|   7   | <a href="https://github.com/Kyrie-Ma/4663-Cryptography-Ma/blob/master/Assignments/A05/words-by-frequency.txt" > words-by-frequency.txt | words-by-frequency.txt      |

