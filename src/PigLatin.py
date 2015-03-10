'''
Created on Sep 28, 2010

@author: ericmercer
'''
def toPig(w):
    #Translates a given string to its Pig Latin equivalent
    word = w + "aeiouy"
    ai = word.find('a')
    ei = word.find('e')
    ii = word.find('i')
    oi = word.find('o')
    ui = word.find('u')
    yi = word.find('y')
    vlist = [ai, ei, ii, oi, ui, yi]
    if min(vlist) == -1:
        for v in vlist:
            if v == -1:
                vlist.remove(v)
    if min(vlist) >= len(w):
        vlist = [-1]
    m = min(vlist)
    if m == -1:
        return w + "-way"
    elif w[0] in "AEIOUaeiou":
        return w + "-way"
    elif w[0:2] == "qu" or w[0:2] == "Qu" or w[0:2] == "QU":
        return w[2:] + "-" + w[0:2] + "ay"
    else:
        return w[m:] + "-" + w[0:m] + "ay"

def pigifyList(words):
    #Returns a new list, based on parameter list but in which each string of parameter list is represented by its Pig Latin equivalent
    nlist = []
    for w in words:
        nlist.append(toPig(w))
    return nlist

def printList(words, outfile):
    #Prints each element of words, a list, on a single line and writes that line with spaces between words to an outfile
    for w in words:
        print w
        outfile.write(w + " ")

def pigifyFile(file, outfile):
    #File is translated to its Pig Latin equivalent, printed, and written to an outfile on a line-by-line basis
    for line in file:
        uline = pigifyList(line.split())
        printList(uline, outfile)
        outfile.write("\n")

def pigify(filename, outfilename):
    #Filename is the name of the file to be translated to Pig Latin
    file = open(filename, "r")
    outfile = open(outfilename, "w")
    pigifyFile(file, outfile)
    file.close()
    outfile.close()

def toEnglish(w):
    #Translates a given Pig Latin string to its English equivalent
    if w[-4:] == "-way":
        return w[0:-4]
    elif w[-2:] == "ay":
        return w[w.find("-") + 1:-2] + w[0:w.find("-")]

def unpigifyList(words):
    #Returns a new list, based on parameter list but in which each string of parameter list is represented by its English equivalent
    nlist = []
    for w in words:
        nlist.append(toEnglish(w))
    return nlist

def unpigifyFile(file, outfile):
    #File is translated to its English equivalent, printed, and written to an outfile on a line-by-line basis
    for line in file:
        uline = unpigifyList(line.split())
        printList(uline, outfile)
        outfile.write("\n")

def unpigify(filename, outfilename):
    #Filename is the name of the Pig Latin file to be translated to English
    file = open(filename, "r")
    outfile = open(outfilename, "w")
    unpigifyFile(file, outfile)
    file.close()
    outfile.close()

if __name__ == "__main__":
    pigify("input/poe.txt", "output-pig/pig-poe.txt")
    pigify("input/romeo.txt", "output-pig/pig-romeo.txt")
                
    unpigify("output-pig/pig-poe.txt", "output-pig/unpig-poe.txt")
    unpigify("output-pig/pig-romeo.txt", "output-pig/unpig-romeo.txt")

