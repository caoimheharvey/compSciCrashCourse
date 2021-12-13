"""

Goat Latin is a made-up language based off of English, sort of like Pig Latin.

 The rules of Goat Latin are as follows:
 1. If a word begins with a consonant (i.e. not a vowel), remove the first
 letter and append it to the end, then add 'ma'.
 For example, the word 'goat' becomes 'oatgma'.
 2. If a word begins with a vowel (a, e, i, o, or u), append 'ma' to the end of the word.
 For example, the word 'I' becomes 'Ima'.
 3. Add one letter "a" to the end of each word per its word index in the
 sentence, starting with 1. That is, the first word gets "a" added to the
 end, the second word gets "aa" added to the end, the third word in the
 sentence gets "aaa" added to the end, and so on.

 Write a function that, given a string of words making up one sentence, returns
 that sentence in Goat Latin. For example:

 string_to_goat_latin('I speak Goat Latin')

 would return: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
"""


def string_to_goat_latin(string):
    VOWELS = ["a", "e", "i", "o", "u"]
    goat_latin_string = ""
    words = string.split()
    for i in range(len(words)):
        if words[i][0].lower() not in VOWELS:
            words[i] = words[i][1:] + words[i][0] + "ma"
        elif words[i][0].lower() in VOWELS:
            words[i] = words[i] + "ma"
        for n in range(i + 1):
            words[i] = words[i] + "a"
        goat_latin_string = goat_latin_string + words[i] + " "
    return goat_latin_string


print(string_to_goat_latin("I speak Goat Latin"))

