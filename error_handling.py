#exceptions

print("New message)

salary = 50000
role = analyst
Age -> 50
print(salary)

#bugs
name = "Mery"
surname = "Osbourne"
print(name + surname)

#exception

#NameError
name = "Anna"
print(surname)

#SyntaxError
score = 85
if score >= 80
  print("Passed")

#IndexError
cars = ["BMW", "Tesla", "Ford"]
print(cars[3])

#TypeError
number = 5
length = len(number)

#ValueError
data = "1A45"
num_data = int(data)


#exception handling

prices = [340, 200, "240", 300]
try:
  total = sum(prices)
  print(total)

color = "Green"
try:
  print(size)
except NameError:
  print("Check the variable name")

colors = ["Red", "Yellow", "Green"]
try:
  print(colors[10])
except IndexError:
  print("Out of range")

try:
  print(len(5))
except NameError:
  print("Variable is not defined")
except TypeError:
  print("Not iterable")

choice = int(input())
coffees = ["latte", "macchiato", "espresso"]
try:
  print(coffees[choice])
except IndexError:
  print("Choose 0, 1 or 2")