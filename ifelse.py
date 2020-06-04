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

num = 19
print("Num before expression: ", num)

num = num - 20 if num > 20 else num + 20
print("Num after expression: ", num)

