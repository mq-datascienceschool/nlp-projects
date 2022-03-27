import re
from collections import Counter

# function to tokenise words
def words(document):
    "Convert text to lower case and tokenise the document"
    return re.findall(r'\w+', document.lower())

# create a frequency table of all the words of the document
all_words = Counter(words(open(r'C:\Users\raiso\Desktop\NLP Projects\NLP-1\nlp-projects\sedd_doc.txt').read()))
# check frequency of a random word, say, 'chair'
print(all_words['chair'])
# look at top 10 frequent words
print(all_words.most_common(10))

# The edits_one() function creates all the possible words that are one edit distance away from the input word. 
def edits_one(word):
    "Create all edits that are one edit away from `word`."
    alphabets    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])                   for i in range(len(word) + 1)]
    deletes    = [left + right[1:]                       for left, right in splits if right]
    inserts    = [left + c + right                       for left, right in splits for c in alphabets]
    replaces   = [left + c + right[1:]                   for left, right in splits if right for c in alphabets]
    transposes = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right)>1]
    return set(deletes + inserts + replaces + transposes)

# The edits_two() function creates a list of all the possible words that are two edits away from the input word.
def edits_two(word):
    "Create all edits that are two edits away from `word`."
    return (e2 for e1 in edits_one(word) for e2 in edits_one(e1))

# The known() function filters out the valid English word from a list of given words. 
# It uses the frequency distribution as a dictionary that was created using the seed document. 
# If the words created using edits_one() and edits_two() are not in the dictionary, they’re discarded.
def known(words):
    "The subset of `words` that appear in the `all_words`."
    return set(word for word in words if word in all_words)

'''
the function possible_corrections() returns a list of all the potential words that can be the correct alternative spelling. 
For example, let’s say the user has typed the word ‘wut’ which is wrong. 
There are multiple words that could be the correct spelling of this word such as ‘cut’, ‘but’, ‘gut’, etc. 
This functions will return all these words for the given incorrect word ‘wut’.

It works as follows:

1. It first checks if the word is correct or not, i.e. if the word typed by the user is a present in the dictionary or not. 
If the word is present, it returns no spelling suggestions since it is already a correct dictionary word.

2. If the user types a word which is not a dictionary word, then it creates a list of all the known words that are one edit distance away. 
If there are no valid words in the list created by edits_one() only then this function fetches a list of all known words that are two edits away from the input word

3. If there are no known words that are two edits away, then the function returns the  original input word. 
This means that there are no alternatives that the spell corrector could find. Hence, it simply returns the original word.

'''
def possible_corrections(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits_one(word)) or known(edits_two(word)) or [word])

'''
The function returns the probability of an input word. This is exactly why you need a seed document instead of a dictionary. 
A dictionary only contains a list of all correct English words. But, a seed document not only contains all the correct words but it could also be used to create a frequency distribution of all these words. 
This frequency will be taken into consideration when there are more than one possibly correct words for a given misspelled word. 
'''
def prob(word, N=sum(all_words.values())): 
    "Probability of `word`: Number of appearances of 'word' / total number of tokens"
    return all_words[word] / N

def spell_check(word):
    "Print the most probable spelling correction for `word` out of all the `possible_corrections`"
    correct_word = max(possible_corrections(word), key=prob)
    if correct_word != word:
        return "Correct spelling is: " + correct_word
    else:
        return "Correct spelling."

# testing above functions
# print(len(set(edits_one("monney"))))
# print(edits_one("monney"))

# print(known(edits_one("monney")))

# Let's look at words that are two edits away
# print(len(set(edits_two("monney"))))
# print(known(edits_one("monney")))

# Let's look at possible corrections of a word
# print(possible_corrections("monney"))

# Let's look at probability of a word
# print(prob("money"))
# print(prob("monkey"))

# print(spell_check("monney"))
