print("hello! I'm a leap Year Checker")
print("")
Year = int(input("Which year you wanna check? "))

# this will check if the year can be divided by 4(y)
x = 4
y = Year % 4
z = Year % 100
a = Year % 400

print(f"y = {y} z = {z} a = {a}")

# it's a filter that checks if the year can be divided by 100, then it checks if the year can be divided by 4 or 400
if z != 0 or a == 0:
  print("")
  if y == 0 or a == 0:
    print(f"{Year} is a leap year")
  else:
    print(f"{Year} isn't a leap year")
else:
  print(f"{Year} isn't a leap year")
