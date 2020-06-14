old_num = "500"
new_num = "10"

remaining_num = int(old_num) - int(new_num)
print(remaining_num)

old_code = "40.3"
new_code = "60.8"

total_code = float(old_code) + float(new_code)
print(total_code)

my_float = "4.6"
my_int = "6"

total = float(my_float) + int(my_int)
print(total)

value_str = "python world"
value_list = list(value_str)
print(value_list)
print("Type of value_str is: ", type(value_str))
print("Type of valeu_list is: ", type(value_list))

list((1, 2, 3, 4, 5))

my_tuple = ("Apple", "Orage", "Mango", "Banana")
print(my_tuple)
print(type(my_tuple))

my_list = list(my_tuple)
print(my_list)
print(type(my_list))

value_str = "python world"
value_tup = tuple(value_str)
print(value_tup)
print(type(value_tup))

my_list = ["Apple", "Orage", "Mango", "Banana"]
print(type(my_list))
print(my_list)
5
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple)

age_list = [["William", 50], ["Henry", 60], ["James", 90]]
age_tuple = tuple(age_list)
print(type(age_tuple))
print(age_tuple)

age_tuple = tuple(age_tuple[0])
print(type(age_tuple))
print(age_tuple)

print("Type of age_list: ", type(age_list))
print("Tyep of age_tuple: ", type(age_tuple))

pet_list = [("Dog", 1), ("Cat", 2), ("Cow", 3), ("Goat", 4)]
pet_tuple = tuple(pet_list)
print(pet_tuple)

age_tuple = ("Leo", 18,
             "Aaron", 25,
             "Easton", 34,
             "Jordan", 30)
print(age_tuple)

age_tuple = (("Leo", 18),
             ("Aaron", 25),
             ("Easton", 34),
             ("Jordan", 30))
print(dict(age_tuple))

age_tuple2 = (("Leo", 18),
             ("Aaron", 25),
             ("Easton", 34),
             (["Jordan", "John"], 30))
print(age_tuple2)
# print(dict(age_tuple2))

age_tuple3 = (("Leo", 18),
             ("Aaron", 25),
             ("Easton", 34),
             ("Jordan", ["John", 30]))
print(age_tuple3)

age_list = [["Willam", 50], ["Joanne", 60], ["Maria", 90]]

print(age_list)
age_dict =dict(age_list)
print(age_dict)
print("Type of age_list: ", type(age_list))
print("Type of age_dict: ", type(age_dict))

set("apple")
fruit_tuple = ("Apple", "Orage", "Mango", "Banana", "Banana")
fruit_set = set(fruit_tuple)
print(fruit_set)
print(fruit_tuple)
print(type(fruit_set))

print(hex(50))
print(hex(60))
print(oct(50))
print(oct(9))
print(bin(5))
print(bin(10))

print(int("0b1010", 2))
print(int("0b1010", 0))
print(int("0x101", 16))
print(ord("a"))
print(ord("A"))
print(chr(100))
print(chr(97))

print(complex(1j))
print(complex(10))
print(complex(1,2))