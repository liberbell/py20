fruit_list = ["apple", "orange", "grape", "banana", "avocado"]
if "grape" in fruit_list:
    print("Yes, grape is in the fruit list.")

else:
    print("No, grape is not in the fruit list.")

if "strawberry" in fruit_list:
    print("strawberry is in the fruit list.")
elif "orange" in fruit_list:
    print("orange is in the fruit list.")
else:
    print("Both strawberry and orange are not in the fruit list.")

if fruit_list[1] == "orange":
    print("True")
else:
    print("False")

if fruit_list[4] == "avocado":
    print("Yes, avocado is at the fourth index.")
    print("Replacing avocado with strawberry at the fourth index.")

    fruit_list[4] = "strawberry"
    print(fruit_list)

else:
    print("avocado is not at the fourth index.")

car_tuple = ["Toyota Camry", "Honda Accord", "Honda Civic", "Toyota Corolla"]

if "Honda Accord" in car_tuple:
    print("Honda Accord is present in our car tuple.")
else:
    print("Honda Accord is not present in our car tuple.")

if "Ducati monster" in car_tuple:
    print("Ducati Monster is a car.")
else:
    print("ducati Monster is not a car.")

if "Ducati Monster" in car_tuple and "Honda Accord" in car_tuple:
    print("Ducati Monster and Honda Accord are both cars.")
else:
    print("At least one of Ducati Monster and Honda Accord is not a car.")

if "Ducati Monster" in car_tuple or "Honda Accord" in car_tuple:
    print("At least one of Ducati Monster and Honda Accord is a car.")
else:
    print("Neither Ducati Monster nor Honda Accord is a car.")

salary_details = {"Lisa": 25000,
                  "Jason": 45000,
                  "Cooper": 35000,
                  "Elias": 23000,
                  "Jordan": 77000}
print(salary_details)

if "Lisa" in salary_details:
    print("We have the salary details for Lisa.")
else:
    print("We don`t have the salary details for Lisa.")

if "Cora" in salary_details:
    print("We have the salary detail for Cora.")
else:
    salary_details["Cora"] = 31000
    print("Cora`s annual income is %s."%salary_details["Cora"])

print(salary_details)