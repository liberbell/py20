# human_age = int(input("Enter dog's age in human years: "))
# if human_age < 0:
#     print("Age must be a positive number.")
#     exit()
# if human_age <= 2:
#     dog_age = human_age * 10.5

# else:
#     dog_age = 21 + (human_age - 2) * 4
# print("The dog's age in numan years is ", dog_age)

letter = input("Enter a letter of the alphabet: ")
letter = letter.lower()

if letter in ('a', 'i', "u", "e", "o"):
    print("%s is a vowel." % letter)