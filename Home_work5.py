#1 list
def calculate():

   first = float(input("Enter first number: "))

   operation = input("Enter operation(+-*/): ")

   second = float(input("Enter second number: "))

   if operation == "+":
       result = first + second
   elif operation == "-":
       result = first - second
   elif operation == "*":
       result = first * second
   elif operation == "/":
       result = first / second
   else:
       print("Something went wrong...")
       return
   print(f"Result:{result}")

calculate()

#OR(був ще один варіант але він чомусь не спрацював)

#expression = input("Enter arithmetic exspression (Example 2*2): ")

#parts = expression.split()

#if len(parts) == 3:

  #num1 = float(parts[0])
  #operat = parts[1]
  #num2 = float(parts[2])

  #if operat == "+":
     #result = num1 + num2

  #elif operat == "-":
     #result = num1 - num2

  #elif operat == "*":
     #result = num1 * num2

  #elif operat == "/":
     #result = num1 / num2

  #else:
      #print("ops...")

 #print(f"Your result: {result}")


#2 list
from random import randint

number = [randint(-20,20) for _ in range(20)]

print(number)

pos=sum([i>0 for i in number])

zero=number.count(0)

print(f'max = {max(number)}\nmin = {min(number)}\npositive = {pos}\nzero = {zero}\nnegative = {len(number)-pos-zero}')

#3 list

list1 = [1,1,2,3,4,5,6]
list2 = [1,7,7,8,9,10]

list3 = list1 + list2
print(list3)

list3 = list(set(list1 + list2))
print(list3)

list3 = list(set(list1) & set(list2))
print(list3)

list3 = list(set(list1) ^ set(list2))
print(list3)

list3 = min(list1),max(list1),min(list2),max(list2)
print(list3)

#4 tuple
tuple1 = ("Hello world!!",122,-12)

print(tuple1,type(tuple1))

tuple2 = (12,34,[22,33],89,178)

print(tuple2[2])

tuple2[2].append(1000)

print(tuple2,type(tuple2))

#5 dict
value = ("Price 1600$","Quantity 100")
value2 = ("Price 40$","Quantity 41")

product = dict(Macbook=value)
product["Keyboard"] = value2

print(product,type(product))

book = ("Erich Remark",1938)
book2 = ("Erich Remark",1929)
book3 = ("Ivan Bagraniy",1944)

books = dict(Tree_comrades = book,Im_Westen_nichts_Neueus = book2,Тигролови = book3)
print(books.get("Тигролови"))


student = ("Derevyanchuck",12.6)
student2 = ("Radchenko",19.9)
student3 = ("Borsh",49.1)

students = dict(Griroriy = student,Marina = student2,Evgeniy = student3)
students.popitem()
print(students,type(students))

#6 set
set1 = {1,2,3,5,6,9,10,12,14,16,19,20}
set2 = {1,2,20,21,22,189}

set_union = set1.union(set2)
set_difference = set1.difference(set2)
set_intersections = set1.intersection(set2)

print(set_union)
print(set_difference)
print(set_intersections)

se1 = {1,2,8,9}
se2 = {1,3,8}
se3 = se1.issubset(se2)
print(se3)


alphabet = {"a","b","c","d"}
alphabet1 = {"a","b","c","d","e","f","g","h","i"}
alphabet_union = alphabet.union(alphabet1)
alphabet_difference = alphabet.difference(alphabet1)
alphabet_intersections = alphabet.intersection(alphabet1)
print(alphabet_union)
print(alphabet_difference)
print(alphabet_intersections)

word = {"hello","name","first open","world","word"}
word.add("football")
word.remove("first open")
print(word)




