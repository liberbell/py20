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
    print("Replacing avocado with strawberry at the forth index.")