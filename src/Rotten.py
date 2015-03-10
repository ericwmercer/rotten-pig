'''
Created on Sep 28, 2010

@author: ericmercer
'''
import string

def rot13(w):
    #Translates the letters in a given string to their ROT13 equivalent
    letters = []
    for n in range(0, len(w)):
        letters.append(w[n])
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    b = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    for n in range(0, len(letters)):
        if w[n] in string.letters:
            letters[n] = b[(a.find(letters[n]))]
    translation = ""
    for n in range(0, len(letters)):
        translation += letters[n]        
    return translation

def rotateList(words):
    #Returns a new list, based on parameter list but in which each string of parameter list is represented by its ROT13 equivalent
    nlist = []
    for w in words:
        nlist.append(rot13(w))
    return nlist

def printList(words, outfile):
    #Prints each element of words, a list, on a single line and writes that line with spaces between words to an outfile
    for w in words:
        print w
        outfile.write(w + " ")

def rotateFile(file, outfile):
    #File is translated to its ROT13 equivalent, printed, and written to an outfile on a line-by-line basis
    for line in file:
        uline = rotateList(line.split())
        printList(uline, outfile)
        outfile.write("\n")

def rotate(filename, outfilename):
    #Filename is the name of the file to be translated to ROT13
    file = open(filename, "r")
    outfile = open(outfilename, "w")
    rotateFile(file, outfile)
    file.close()
    outfile.close()

if __name__ == "__main__":
    rotate("input/poe.txt", "output-rot/rot-poe.txt")
    rotate("input/romeo.txt", "output-rot/rot-romeo.txt")
    
    rotate("output-rot/rot-poe.txt", "output-rot/unrot-poe.txt")
    rotate("output-rot/rot-romeo.txt", "output-rot/unrot-romeo.txt")

