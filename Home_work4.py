#1
user = input("Введіть текст:")
if user == user[::-1]:
    print("Введений текст є Паліндромом")
elif user != user[::-1]:
    print("Введений текст не є Паліндромом")
else:
    print("Щось пішло не так...")

# OR

user = input("Введіть текст:")
if user == user[::-1]:
    print("Введений текст є Паліндромом")
else:
    print("Введений текст не є Паліндромом")

#2
any_text = input("Enter any text: ")
reserved_word = input("Enter reserved words with a comma:").split(",")
for word in any_text.split():
    if word.lower() in reserved_word:
        any_text = any_text.replace(word,word.upper())
print(any_text)

#3
text = input("Enter any text: ")
summa = text.count(".") + text.count("!") + text.count("?") + text.count(";")
print(f"The number of sentences in this text: {summa}")

# #* Зробити программу, яка емулює метод replace
import re
text1 = "French orthography encompasses the spelling and punctuation of the French language. It is based on a combination of phonemic and historical principles. The spelling of words is largely based on the pronunciation of Old French c. 1100–1200 AD, and has stayed more or less the same since then, despite enormous changes to the pronunciation of the language in the intervening years. Even in the late 17th century, with the publication of the first French dictionary by the Académie française, there were attempts to reform French orthography"
new_text1 = re.sub("French","England",text1,flags = re.I)
print(new_text1)