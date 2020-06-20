# human_age = int(input("Enter dog's age in human years: "))
# if human_age < 0:
#     print("Age must be a positive number.")
#     exit()
# if human_age <= 2:
#     dog_age = human_age * 10.5

# else:
#     dog_age = 21 + (human_age - 2) * 4
# print("The dog's age in numan years is ", dog_age)

# letter = input("Enter a letter of the alphabet: ")
# letter = letter.lower()

# if letter in ('a', 'i', "u", "e", "o"):
#     print("%s is a vowel." % letter)
# elif letter == 'y':
#     print("Y is ambiguous. It depends where it is used.")
# else:
#     print("$s is a consonant." % letter)

# month_name = input("Enter the name of the Month: ")

# if month_name == "February":
#     print("No. of days: 28/29 days")
# elif month_name in ("April", "June", "September", "November"):
#     print("No, of days: 30 days")
# elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
#     print("No. of days: 31 days")
# else:
#     print("Give a correct month name")

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a == b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or c == a:
#     print("Isosceles triangle")
# else:
#     print("\nScalene triangle")

# str_value = input("Enter the string: ")
# reversed_str = str_value[::-1]

# if (str_value == reversed_str):
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

ans = int(input("How many days are there in a leap year? "))
print("You entered: ", ans)

if ans == 366:
    print("You have cleared the first level.")

    ans = input("\nWhich month has an extra day in a leap year?").lower()