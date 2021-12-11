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

def string_to_goat_latin(some_text):
    splitted_text = some_text.split()
    final_text = []
    counter = 0

    for s in splitted_text:
        # can also do:
        # temp_list = s.split()
        temp_list = [char for char in s]
        counter += 1
        # print(temp_list)
        if temp_list[0].lower() not in 'aeiou':
            temp_list.append(temp_list.pop(0))
            temp_list.append('m')
            temp_list.append('a')
        else:
            temp_list.append('m')
            temp_list.append('a')
        for i in range(counter):
            temp_list.append('a')
        final_text.append(''.join(temp_list))
    print(' '.join(final_text))


string_to_goat_latin('I speak Goat Latin')