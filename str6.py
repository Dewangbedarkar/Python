sentence = input("Enter a sentence: ")


words = sentence.split()
print(words)

reversed_words = words[::-1]
print(reversed_words)
reversed_sentence = ' '.join(reversed_words)

print("Reversed sentence:", reversed_sentence)