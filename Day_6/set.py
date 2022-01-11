#Program to check the length of the given string using set.
word=input("Enter the string: ")

word_set=set(word)

for char in word_set:
    print(f"{char} is {word.count(char)}")

