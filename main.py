
# def multiple_num(num1, num2):
#     if num1*num2 <= 1000:
#         return num1*num2
#     else:
#         return num1+num2
# sum = multiple_num(20,30)
# print(sum)

# def add_num(num1, num2)
# sum = 0
# i = 0
# previous = 0
# for i in range(11):
#     sum = previous + i
#
#     print("Current Number", i, "Previous Number ", previous, " Sum: ", sum)
#     previous = i
# string = input("Enter your word")
# print("original  string ", string)
# size = len(string)
# for i in range(0, size - 1, 2):
#      print("index[", i, "]", string[i])
# listx = [10,20,30,40,10]
# if listx[0] == listx[4]:
#     print(True)
# else:
#     print(False)
#     listx = [10, 20, 30, 40, 10]
#     if listx[0] == listx[4]:
#         print(True)
#     else:
#         print(False)
# new_list = [input("Enter any word")]
# print(new_list.remove())
# str_x = "Emma is good developer. Emma is a writer"
# if Emma in str_x:
# for x in range(1, 6):
#     print((str(x) *x), )
# num = (input("Enter number: "))
# print("Original number is  ",num)
# if num == num[::-1]:
#   print("Yes num is reversed")
# else:
#   print("Error")
# list_1 = [10, 20, 25, 30, 35]
# list_2 = [40, 45, 60, 75, 90]
# def odd_fun(list_1):
#   for odd in list_1:
#     if odd%2 == 1:
#       return odd
#   even_fun()
# def even_fun(list_2):
#   for even in list_2:
#     if even%2==0:
#       return even
#   sum()
# def sum(odd, even):
#   print(odd)
#   print(even)
#
#
# odd_fun(list_1)
#


# def return_num(num1, num2):
#     if num1*num2 <1000:
#         return num1*num2
#     else:
#         return num1+num2
# print(return_num(20,30))
# print(return_num(30,40))
# sum = 0
# previous = 0
# current = 0
# for current in range(0,10):
#     sum = previous+current
#     print(f"Current Number is {current} Previous Number  is {previous}  Sum is {sum}")
#     previous = current
# str_name = input("Enter your word: ")
# x = list(str_name)
# for name in str_name[::2]:
#     print(name)
# x = input("Enter your word: ")
# def remover_letter(x, n):
#         y = x[n:]
#         return y
# print(remover_letter(x, 2))
# print(remover_letter(x, 4))
# number_x = [10,20,30,40,50,10]
# number_y = [75, 65, 35, 75, 30]
# def return_fun():
#     if number_x[0] == number_x[5] and number_y[0] == number_y[4]:
#         return True
#     else:
#         return False
# print(return_fun())
# new_list = []
# list_num = [10, 20, 33, 46, 55]
# for num in list_num[::1]:
#     if num%5 == 0:
#         new_list.append(num)
#     else:
#         pass
# print(new_list)
# str_x = "Emma is good developer. Emma is a writer"
# print(" Emma is founded  times", str_x.count("Emma"))
# for x in range(6):
#     print(str(x)*x)
# n = input("Enter your num: ")
# if n[::1] == n[::-1]:
#     print("Yes ")
# else:
#     print("No")
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list_3 = []
# for num in list1[:]:
#     if num%2 != 0:
#         list_3.append(num)
#     else:
#         pass
# for num in list2[:]:
#     if num%2 == 0 :
#         list_3.append(num)
#     else:
#         pass
# print(list_3)
# number = int(input("Enter the integer number: "))
#
# while (number > 0):
#     digit = number % 10
#     number = number // 10
#     print(digit, end=" ")
# num = int(input("Enter your num: "))
# if 0 < num < 10000:
#     print(0)
# elif 10000< num <= 20000:
#     z = (num - 10000)*10/100
#     print(z)
# else:
#     z = 10000*10/100 + (num-20000)*20/100
#     print(z)
# def multiple(x,y):
#     for x in range(1,11):
#         for y in range(1,11):
#             print(x*y, end= " ")
#         print("\t\t")
# multiple(1,1)

# for x in range(5,0,-1):
#     print("*" * x)
# def pow(exponent, base):
#     print(exponent**base)
# pow(2,5)
# n = int(input("Enter your num: "))
# y = int(input("Enter your num: "))
# print(n*y)
# a = input(" Please enter your name: ").strip().title()
# first, last = a.split(" ")
# print(f"Your name is {first} {last}")
# name = input("Enter your name:")
# print("your name is: ", end='\n')
# print(name)
# x = float(input("Enter your num x: "))
# y = float(input("Enter your num y: "))
# z = x/y
# print(f"Your mathematical result {z:.6f}")

# def main():
#     x = int(input("what is x?:"))
#     print("x squared is", square(x))
#
#
# def square(n):
#     return n*n
#
#
# main()
# import sys
# from compare import goodbye
# if len(sys.argv) == 2:
#     goodbye(sys.argv[1])
# from compare import square
# def main():
#     test_square()
#
# def test_square():
#     try:
#        assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3)== 9
#     except AssertionError:
#         print("3 is not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("3 is not 9")
# if __name__ == "__main__":
#     main()
# from compare import square
# import pytest
#
#
# def test_positive():
#     assert square(2) == 4
#     assert square(3) == 9
#
#
# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9
#
#
# def test_zero():
#     assert square(0) == 0
#
# def test_str():
#     with pytest.raises(TypeError):
#         square("cat")
# from compare import hello
#
# def test_default():
#     assert hello() == "hello, world"
#
# def test_argument():
# #     assert hello("David") == "hello, David"
# from compare import hello
# def test_default():
#     assert hello() == "hello, world"
# def test_argument():
#     assert hello("Riad") == "hello, Riad"
# name = []
# for names in range(3):
#     name.append(input("Whats your name"))
# for sort in sorted(name):
#     print(f"hello, {sort}")
# import cowsay
# import sys
# if len(sys.argv) == 2:
#     cowsay.trex("Hello" + sys.argv[1])
# name = input("Enter your name: ")
# with open("names.txt", "a" ) as file:
#     file.write(f"{name}\n")
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello", line.rstrip()
# names = []
# with open("main/names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names, reverse=True):
#     print(f"Hello, {name}")
# names = []
# with open("main/names.txt") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         boys = {"name" = name, "house" = house }
#         names.append(boys)
# for name in sorted(names):
#     print(f"{[]}")
# x = int(input("Enter your number:"))
# y = int(input("Enter your number:"))
# if x > y or x < y :
#     print("x is not equal to y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x is equal to y")
# import random
# while True:
#     score = int(input("Enter your number:"))
#     if score > 90:
#         print("Your grade is A")
#     elif score >= 80:
#         print("Your grade is B")
#     elif score >= 70:
#         print("Your grade is C")
#     elif score >= 60:
#         print("Your grade is D ")
#     elif score < 60:
#         print("Your grade is F")
#
# def main():
#     x = int(input("Enter your number:"))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
#
#
# def is_even(n):
#     return n % 2 == 0
#
#
# main()
# name = input("Enter a number:")
# # match name:
# #     case "Harry" | "Hermione" | "Ron":
# #         print("Gryffindor")
# #     case "Draco":
# #         print("Slytherin")
# #     case _:
# #         print("Who")
# i = float(3)
# while i != 0:
#     print("meow")
#     i -= 0.5
# list_name = ["riad", "nadir", 1, 2, True, False]
# for i in list_name:
#     print("meow")
# while True:
#     n = int(input("What is the n?"))
#     if n > 0:
#         break
# for i in range(n):
#     print("meow")
# def main():
#     number = get_number()
# def get_number():
#     while True:
#         n = int(input("Enter your num:"))
#         if n > 0:
#             break
#     meow(n)
# def meow(n):
#     for i in range(n):
#         print("meow")
# main()
# students = ["Hermione", "Harry", "Ron"]
# students.append("Riad")
# students.pop()
# for names in range(len(students) -1):
#     print(names, students[names])
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# new_dict = {
#     "Hermy": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor"
# }
# for students in new_dict:
#     print(students, new_dict[students], sep=" ")
# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patron": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patron": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patron": "Jack Russel terrier"},
#     {"name": "Draco", "house": "Slytherin", "patron": None}
# ]
# for student in students:
#     print( student["name"], student["house"], student["patron"], sep=" ")
# def main():
#     print_square(3)
#
# def print_square(size):
#     for i in range(size):
#             print("#"*size, end = "\n")
# main()
# try:
#     print(hello)
# except NameError:
#     print("you make a mistake")
# while x = int(x):
#     try:
#         x = int(input("What's x? "))
#          print(f"Your number is{x}")

#     except ValueError:
#         print("ValueError")
# def main():
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass
#
#
# main()
# import random
# print(choice(["eagle", "nub"]))
# print(random.randint(1,1000))
# cards = ["Jack", "King", "Queen"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
# import statistics
# print(statistics.median([1,2,3,4,6,7,8,9,0,10,5]))
# print(statistics.mean([100, 95]))
# import sys
# while True:
#     try:
#         print("hello my name is", sys.argv[1])
#         break
#     except IndexError:
#         print("You have some error")
# import sys
#
# if len (sys.argv)<2:
#     sys.exit("too few arguments")
#
# for arg in sys.argv[-1:]:
#     print("hello, my name is", arg)
# import cowsay
# import sys
# if len(sys.argv) == 2:
#     cowsay.turkey("Hello,"+sys.argv[1])
# import requests
# import sys
# import json
# if len(sys.argv) !=2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term="+sys.argv[1])
# print(json.dumps(response.json(), indent=2))
# o = response.json()
# for result in o["results"]:
#     print(result["artistName"])
# def main():
#     hello("world")
#     goodbye("world")
# def hello(name):
#     print(f"hello, {name}")
# def goodbye(name):
#     print(f"goodbye, {name}")
# if __name__== "__main__":
#     main()
# def main():
#     x = (input("Whats x?: "))
#     print(f"X is ", square(x))
#
#
# def square(n):
#     return n * n
#
#
# if __name__ == "__main__":
#     main()
# def main():
#     name = input("whats your name")
#     print(hello(name))
# def hello(to ="world"):
#     return f"hello, {to}"
# if __name__ == "__main__":
#     main()
