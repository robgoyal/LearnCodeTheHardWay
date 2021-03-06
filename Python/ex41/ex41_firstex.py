#!/usr/bin/env/python

# ex41.py
# Code written by Robin Goyal
# Created on 08-08-2016
# Last updated on 08-08-2016

import random
from urllib import urlopen
import sys

# Link to open
WORD_URL = "http://learncodethehardway.org/words.txt"

# Empty List
WORDS = []

# Dict of phrases
PHRASES = {
        "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
        "*** = %%%()":
        "Set *** to an instance of class %%%.",
        "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
        }


# Checks if there are 2 arguments and that the second one is english
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# open link and strip the whitespace while appending the words from the link to the list WORDS
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
            random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        # Access the keys in phrases and store them in the snippets list
        snippets = PHRASES.keys()
        # Randomly shuffle through the snippets list
        random.shuffle(snippets)

        # Loop through snippets
        for snippet in snippets:
            # Access the value of the key
            phrase = PHRASES[snippet]
            # Get the question and answer from the convert function
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer

except EOFError:
    print "\nBye"
