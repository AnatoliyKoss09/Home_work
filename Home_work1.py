# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('My friend Jack')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello")
num20 = int(input('Введите число больше 11: '))
usl1 = int(input("Введіть перше число для додавання: "))
usl2 = int(input("Введіть друге число для додавання: "))
usl3 = int(input("Введіть перше число для віднімання: "))
usl4 = int(input("Введіть друге число для віднімання: "))
usl5 = int(input("Давайте будем множити! Введіть будь-яке число: "))
usl6 = int(input("Введіть інше число для множення: "))
usl7 = int(input("Введіть перше число для ділення: "))
usl8 = int(input("Введіть перше число для ділення: "))
print("Результат додавання: ", usl1 + usl2)
print("Віднімання: ", usl3 - usl4)
print("Ваш результат множення: ", usl5 * usl6)
print("Ділення із залишком: ", usl7 / usl8)

username = input("Enter your name: ")
surname = input("Enter you surname: ")
password = input("Choose security password: ")
age = int(input("Enter you age: "))
country = input("Enter you country:")
print(
    f"Congratulations! {username} {surname}.Registration was successful! You password: {password}. You age: {age}. You country: {country}. WELCOME TO ANBOARD!!!")

a = input("Enter you name: ")
b = input("Enter you country: ")
c = input("Enter you city:  ")
d = input("Enter you proffession: ")
y = input("Enter you salary: ")
print(
    "Glad to see " + a + " you on the job search site!!We proceed to search for a job in " + b + " city: " + c + " in specialty " + d + " and with the desired level of salary: " + y + " Stay connected!")
print(
    "Glad to see{}. you on the job search site!!We proceed to search for a job in {}. city:{}. in specialty {}. and with the desired level of salary: {}. Stay connected!".format(
        a, b, c, d, y))
