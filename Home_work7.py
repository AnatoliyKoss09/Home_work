
# 1
text = "“Don't let the noise of others' opinions drown out your own inner voice.”" "Steve Jobs"


def print_text():
    print("“Don't let the noise of others\n"
          "       opinions drown out your\n"
          "                own inner voice.”\n"
          "                        Steve Jobs")


print_text()


# 2
def check_number2(number1, number2):
    try:

        for i in range(number1, number2 + 1):
            if i % 2 == 0:
                print(f"{i} Paired number!")
            elif i % 2 != 0:
                print(f"{i} Not Paired number!")

    except TypeError:
        print("Invalid Data")

    finally:
        print(f"Programm completed")


check_number2(12,20)

#OR
def check_number(number):
    try:
        if number % 2 == 0:
            print(f"{number} Paired number!")

        elif number % 2 != 0:
            print(f"{number} Not paired number!")

    except TypeError:
        print("Invalid data")

    else:
        print("Good luck!")

    finally:
        print("-Function completed-")

check_number(2)



#3
def lines_symbol(lenght_lines, directions, symbol):
    if directions == "horizontal":
        print(symbol * lenght_lines)
    elif directions == "vertical":
        for i in range(lenght_lines):
            print(symbol)
    else:
        print("Wrong directions")
lines_symbol(3,"vertical","!")

# 4
def max_number(number1, number2, number3, number4):
    print(max(number1, number2, number3, number4))

max_number(1, 2, 7, 99)

#5
def sum_number(number1, number2):
    suma = 0
    for i in range(number1, number2 + 1):
        suma += i
    return suma

print(f"Sum of numbers of range: {sum_number(2, 4)}")

#6
def simple_number(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(simple_number(9))

#7
def happy_number(happy_number):

    if 100000 <= happy_number <= 999999:

        first_number = happy_number // 1000
        last_number = happy_number % 1000
        sum_first_number = sum(map(int, str(first_number)))
        sum_last_number = sum(map(int, str(last_number)))

        return sum_first_number == sum_last_number
    else:
        return False


print(happy_number(123420))


