#1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
sum = num1 + num2 + num3
print(f"You result: {sum}.")

#2
num = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
sum_min = min(num, num2, num3)
sum_max = max(num, num2, num3)
sum_mean = ((num + num2 + num3) / 3)
print(f"Minimum of three numbers: {sum_min}.")
print(f"Max of three numbers: {sum_max}.")
print(f"Average of three numbers: {sum_mean}.")

inputs = input("Enter 3 numbers separated by a space: ").split()
a, b, c = int(inputs[0]), int(inputs[1]), int(inputs[2])
print("Enter 1 for maximum, 2 - minimum, 3 - average: ")
choice = int(input())
if choice == 1:
    print(max(a, b, c))
elif choice == 2:
    print(min(a, b, c))
elif choice == 3:
    print((a + b + c) / 3)
else:
    print("Ups...")

#3
day = int(input("Enter any day of the week 1 -7 : "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("F-R-I-D-A-Y")
elif day == 6:
    print("S-A-T-U-R-D-A-Y")
elif day == 7:
    print("S-U-N-D-A-Y")
else:
    print("Something went wrong")

print("Thank You! Good Luck!")

#4
month = int(input("Enter number YOU favorite MONTH 1 - 12 : "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Something went wrong")

print("Thank You! Good Luck!")

#5
num_5 = int(input("Enter any number: "))
if num_5 > 0:
    print("Number is positive")
elif num_5 < 0:
    print("Number is negative")
elif num_5 == 0:
    print("Number is equal to zero")
else:
    print("Program completed")

#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a != b and a < b:
    print(b,a)
elif a != b and a > b:
    print(a,b)
else:
    print("You entered the same numbers")

#7
start = int(input("Enter number for start: "))
end = int(input("Enter number for end: "))

for i in  range(start,end):
    if i % 7 == 0:
        print(i)

#8 -  з допомогою інтернет ресурсів
def print_info():

   print("Enter the start and of the range")

   start = int(input("Start: "))
   end = int(input("End: "))
   print("All numbers range:")
   for i in range(start, end + 1):
       print(i, end=" ")
   print()
   print("All numbers range by decline:")
   for i in range(end, start - 1, -1):
       print(i, end=" ")
   print()
   print("All numbers are multiples of 7:")
   for i in range(start, end + 1):
       if i % 7 == 0:
           print(i, end=" ")
   print()
   print("The number of multiples 5:")
   count = 0
   for i in range(start, end + 1):
       if i % 5 == 0:
           count += 1
   print(count)
if __name__ == "__main__":
   print_info()

#9 - з допомогою інтернет ресурсів
def print_info2():

   start = int(input("Enter start of range: "))
   end = int(input("Enter end of range: "))
   for i in range(start, end + 1):
       if i % 3 == 0 and i % 5 == 0:
           print("Fizz Buzz")
       elif i % 3 == 0:
           print("Fizz")
       elif i % 5 == 0:
           print("Buzz")
       else:
           print(i)
if __name__ == "__main__":

   print_info2()