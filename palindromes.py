
"""
Find palindromes (letter palingrams) in a dictionary file.
"""

import load_dictionary

word_list = load_dictionary.load('words.txt')

pali_list = []


for word in word_list:
	if len(word) > 1 and word == word == word[::-1]:
		pali_list.append(word)


print(f"Number of palindromes found = {len(pali_list)} .")

print(*pali_list, sep ='\n')


