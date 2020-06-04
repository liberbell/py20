if 10 > 20:
    print("10 is greater than 20")
    print("if block activated.")
else:
    print("10 is less than 20")
    print("else block activated.")

bike_price = 7160
print(bike_price)

if bike_price <= 8000:
    print("It`s a cheap bike.")
    print("If block activated.")

else:
    print("It`s an expensive bike.")
    print("Else block activated.")

bike_price = 9000

if bike_price <= 8000:
    print("It`s a cheap bike.")

else:
    print("It`s an expensive bike.")

num = 50
print("Num before expression: ", num)

num = num - 20 if num > 20 else num + 20
print("Num after expression: ", num)

num = 50
print("Num before expression: ", num)

if num > 20:
    num = num - 20
else:
    num = num + 20

print("Num after expression: ", num)

num = 100
print("Number before expression: ", num)

result = num /5 if num < 50 else num *5
print("Number after expression: ", result)

if 15 > 20:
    print("15 is greater than 20.")
    print("if block activated.")

elif 15 < 20:
    print("15 is less than 20.")
    print("elif blcok activated.")

else:
    print("Both are equal.")
    print("else block activated.")

a = 45
b = 45
if b > a:
    print("b is greater than a.")
    print("if block activated.")
elif b == a:
    print("a and b are equal.")
    print("elif block activated.")
else:
    print("b is less than a.")
    print("else block activated.")

bike_price = 20000
if bike_price < 6000:
    print("It`s a cheap bike.")
elif bike_price >= 6000 and bike_price < 10000:
    print("It`s a moderately priced bike.")
else:
    print("It`s a somewhat expensive bike.")