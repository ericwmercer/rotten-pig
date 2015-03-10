Rotten Pig
==========

Two simple Python modules for transforming text into [Pig Latin](http://en.wikipedia.org/wiki/Pig_Latin) or encoding text using a [ROT13 cipher](http://en.wikipedia.org/wiki/ROT13)

Overview
--------
This was my very first programming assignment for CS101 (Intro to Computer Science). The goal was to create two Python modules - `PigLatin.py` and `Rotten.py` - that could each read in a text file and produce a Pig-Latinized or ROT13-encoded version written to an output file. Additionally, each module needed to be able to take a transformed output file and revert it back to the original text (or at least as close as possible for Pig Latin due to a small amount of information loss during the initial transformation).

Each module includes a ``main()`` function that reads in the two sample files in the ``input/`` directory (`poe.txt` and `romeo.txt`) and writes the transformed text for each to new  ``<TRANSFORM>-<INPUT>.txt`` files in the appropriate ``output-<TRANSFORM>/`` directory. These transformed text files are then un-transformed back to their original text, with the resulting ``un<TRANSFORM>-<TEXT>.txt`` files also placed in the appropriate ``output-<TRANFORM>/`` directory.

Pig Latin Rules
---------------
Treat every letter as either a vowel or not-a-vowel and treat all other characters as punctuation. It's possible that different words will be transformed to the same Pig Latin word (e.g. "it" and "wit" will both be transformed to "it-way" using the rules below).

1. If a word begins with 'a', 'e', 'i', 'o', or 'u', then append the string "-way" to form the Pig Latin equivalent.

   Word    | Pig Latin Equivalent
--------|---------------------
anchor  | anchor-way
elegant | elegant-way
oasis   | oasis-way
isthmus | isthmus-way
only    | only-way

2. If a word begins with a non-vowel, move the prefix before the first vowel to the end with "ay" appended. Use a hyphen and treat 'y' as a vowel. If 'y' is the first letter of a word it should be considered a consonant.

   Word      | Pig Latin Equivalent
----------|--------------------
computer  | omputer-cay
slander   | ander-slay
spa       | a-spay
pray      | ay-pray
yesterday | esterday-yay
strident  | ident-stray
rhythm    | ythm-rhay 

3. Words that begin with a 'qu' should be treated as though the 'u' is a consonant.

   Word  | Pig Latin Equivalent
------|---------------------
quiet | iet-quay
queue | eue-quay
quay  | ay-quay

4. If a word contains no vowels, it should be treated as though it starts with a vowel.

   Word | Pig Latin Equivalent
-----|---------------------
zzz  | zzz-way

ROT13 Rules
-----------
Replace each letter with the letter that appears 13 places after it in the alphabet. Leave all other characters as-is.
