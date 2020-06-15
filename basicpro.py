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

cars_list = ["Toyota Camry", "Honda Accord", "Honda Civic", "Toyota Corolla"]
print("List of cars before the swap: ", cars_list)

car_list_temp = cars_list[0]
cars_list[0] = cars_list[2]
cars_list[2] = car_list_temp

print("List of cars after the swap: ", cars_list)