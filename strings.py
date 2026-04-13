
from os import name

sentence = input("Enter a sentence: ")
character = input("Enter a character: ")

character_count = len(sentence)


word_count = len(sentence.split())

upper_case = sentence.upper()

print(f"The number of characters in the sentence is: {character_count}")
print(f"The number of words in the sentence is: {word_count}")
print(f"The sentence in uppercase is: {upper_case}")

if character in sentence:
    print(f"The character '{character}' is present in the sentence.")
else:
    print(f"the character '{character}' is not present in the sentence.")
