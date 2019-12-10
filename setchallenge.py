text = "Python is a very powerful language"
vowels = frozenset("aeiou")

not_vowel_set = set(text).difference(vowels)
finalSet = sorted(not_vowel_set)
print(finalSet)
