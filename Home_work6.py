# 1

with open("test1.txt", "r") as file1:
    a = set(file1)

with open("test2.txt", "r") as file2:
    b = set(file2)

c = a.difference(b)
d = b.difference(a)
print(c, d)

# OR

with open("test1.txt", "r") as f1:
    lines1 = f1.readlines()

with open("test2.txt", "r") as f2:
    lines2 = f2.readlines()

for line1, line2 in zip(lines1, lines2):
    if line1.strip() != line2.strip():
        print(f'Рядок з test1.txt: {line1}')
        print(f'Рядок з test1.txt: {line2}')

# 2

with open("file_test1.txt", "r") as ft1:
    a = ft1.read()
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

char_count = len(a)
line_count = a.count("\n") + 1
sum_vowels = sum(1 for char in a if char in vowels)
sum_consonants = sum(1 for char in a if char in consonants)
numbers = [int(s) for s in a.split() if s.isdigit()]
num_numbers = len(numbers)

with open("test_file2.txt", "w") as ft2:
    ft2.write(f"Кількість символів: {char_count}\n")
    ft2.write(f"Кількість рядків: {line_count}\n")
    ft2.write(f"Кількість голосних: {sum_vowels}\n")
    ft2.write(f"Кількість приголосних: {sum_consonants}\n")
    ft2.write(f"Кількість цифр: {num_numbers}\n")
print("Statistics saved to file 'ft2'")

# 3

with open("file_test1.txt", "r") as ft1:
    lines = ft1.readlines()
    lines = lines[-1]

with open("file_test2.txt", "w") as ft2:
    ft2.writelines(lines)

# 4
with open("file_test2.txt", "r") as ft2:
    b = ft2.readlines()
    max_b = max(b)
    print(f"Довжина найдовшого рядка у файлі 'file_test2.txt':{max_b}")

# OR
f = open("file_test2.txt", "r+")
ab = f.readlines()
max_ab = max(ab)
print(f"Longest line: {max_ab}")
f.close()
