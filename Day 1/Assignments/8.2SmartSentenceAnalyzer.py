sentence = input("enter the statement")
vowel, consonant = 0, 0

for word in sentence:
    if word == '!': 
        break
    if word == ' ':
        continue
    if word.isalpha():
        if word in "aeiouAEIOU":
            vowel +=1
        else: 
            consonant +=1


print("Vowels:", vowel)
print("Consonants:", consonant) 