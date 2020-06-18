# salary = int(input("Enter your salary amount: "))
# expenses = int(input("Enter your expenses: "))

# saving = salary - expenses
# print("My total savings in a month is: ", saving)

# first_num = int(input("Enter first variable: "))
# second_num = int(input("Enter second variable: "))

# first_num = first_num + second_num
# second_num = first_num - second_num
# first_num = first_num - second_num

# print("\nFirst num is: ", first_num, "\nSecond num is: ", second_num)

# num = int(input("Enter a number: "))

# tmp1 = str(num)
# tmp2 = tmp1 + tmp1
# tmp3 = tmp1 + tmp1 + tmp1

# total = num + (int(tmp2)) + (int(tmp3))
# print(tmp1, "+", tmp2, "+", tmp3, "=", total)

# num_1 = int(input("Enter first num: "))
# num_2 = int(input("Enter second num: "))
# Quotient = int(num_1 / num_2)
# print("\nQuotient: ", Quotient)

# Remainder = num_1 % num_2
# print("Remainder: ", Remainder)

# principle = float(input("Enter the priceple amount: "))
# time = int(input("Enter the time(years): "))
# rate = float(input("Enter the rate: "))

# simple_int = (principle * time * rate) / 100
# print("The simple interest is: ", simple_int)

# cm = int(input("Give the highest in centimeters: "))
# inches = 0.394 * cm
# feet = 0.0324 * cm

# print("The length in inches: ", round(inches, 2))
# print("The length in feet: ", round(feet, 2))

# 5


cars_list = ["Toyota Camry", "Honda Accord", "Honda Civic", "Toyota Corolla"]
print("List of cars before the swap: ", cars_list)

car1 = 1
car2 = 2

cars_list[car1], cars_list[car2] = cars_list[car2], cars_list[car1]
print("List of cars before the swap: ", cars_list)

list_students = ["Sofia", "Ella", "Samuel", "Ella", "Aiden", "Sofia"]
print("Student list: ", list_students)
print("Number of student: ", len(list_students))

student_set = set(list_students)
print("\nNew student list: ", student_set)
print("\nNew number of student: ", len(student_set))

print("There are %s duplicate elements."%(len(list_students) - len(student_set)))

list_str = ["Sofia", "Ella", "Samuel", "Ella", "Aiden", "Sofia"]
len_list_str = len(list_str)
len_set_str = len(set(list_str))

if len_set_str == len(set(list_str)):
    print("There are no duplicate elements.")
else:
    print("There are {} duplicate elements.".format(len_set_str - len_list_str))

num_value = 51
print("The number stored in num_value is :", num_value)

if not num_value % 2 == 0:
    print("The num is an odd number.")
else:
    print("The num is an even number.")

# Values = input("Enter some comma separated numbers: ")

# list_value = Values.split(",")
# tuple_value = tuple(list_value)

# print("List: ", list_value)
# print("Tuple: ", tuple_value)

# list_words = input("Enter some space separated words: ")

# words = list_words.split(" ")
# new_list_words = sorted(words)

# print(new_list_words)

# sentence = input("Enter some whitespace-separated words: ")
# words = sentence.split(" ")
# set_of_words = set(words)

# sorted_set_of_words = sorted(set_of_words)
# print(set_of_words)
# print(sorted_set_of_words)
# print(" ".join(sorted_set_of_words))

num_dict = dict()

num_dict[1] = 1 ** 2
num_dict[2] = 2 ** 2
num_dict[3] = 3 ** 2

print(num_dict)

# string_1 = input("Enter first string: ")
# string_2 = input("Enter second string: ")

# set_1 = set(string_1)
# set_2 = set(string_2)

# common_char = set_1.intersection(set_2)
# print("\nCommon letters: ", common_char)

list_num = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
len_of_list = len(list_num)

print("Numbers before slising %s " %list_num)
print("Length of numbers before slising: ", len_of_list)

half = int(len_of_list / 2)
list_num1 = list_num[:half]
list_num2 = list_num[half:]

print("\nFirst half: %s" %list_num1)
print("Second half: %s" %list_num2)

# num = float(input("Enter a number: "))

# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number ", num)
# else:
#     print("Negative number %s" %num)

var = 1+1j

if (type(var) == int):
    print("Type of the variable is Interger.")
elif (type(var) == float):
    print("Type of the variable is Float.")
elif (type(var) == complex):
    print("Type of the variable is Complex.")
else:
    print("Type of the variable is Unknown.")

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("%d is Even" % num)
else:
    print("%d is Odd" % num)