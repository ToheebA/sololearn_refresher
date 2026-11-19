#comment1

#tuples
colors = ["red", "yellow", "blue"]
print(color[1])

colors = ["yellow", "red", "blue"]
print("Original list:")
print(colors)

#making changes


b_day = (21, "May", 2024)
coordinates = (48.8584, 2.2945)
print(coordinates[1])


sizes = (15, 44, 5)
print(sizes[2])

ids = (1906, 9375, 5674)
users = ["Mery", "Anna", "Bob"]
message = "Registered"
count_ids = len(ids)

scores = (7, 9, 9, 8, 9)
print("# of 7:", scores.count(7))
print("# of 9:", scores.count(9))
print("# of 2:", scores.count(2))

point = (12, 14, 9, 10, 9)
winner = max(points)
for point in points:
  if point > 10:
    print(point, ": passed")

birthday_date = (12, "August", 1993)
day, month, year = birthday_date
print(day)
print(month)

scores = (98, 96, 95, 87, 94)
winner, *rest = scores
print(winner)
print(rest)

#dictionaries
contact = {
  "name" : "John",
  "number" : 0817771881
}

car = {
  "brand" : "audi",
  "model" : "Q5"
}

app_settings = {
  "dark mode" : True
}

contact = {
  "name" : "John",
  "company" : "Google"
}
print(contact[company])
contact.get(company)
info_keys = contact.keys()
info_values = contact.values()
info = contact.items()

user = {
  "Name":"Albert",
  "Age":29
}
user["Age"] = 30

print(user["Age"])

student["faculty"] = "Arts"

car.update({"Color": "red"})

car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
car.update({"Color": "blue",
"Year": 2018})

results.pop("Math")

"red" in car.values()

for i in student:
  print(i)

for i in car.values():
  print(i)


#list comprehension

nums = [x for x in range(1,51)]
print(nums)

doubled_nums = [x*2 for x in range(10)]
print(doubled_nums)

tags = ["travel", "vacation", "journey"]
hashtags = ["#" + x for x in tags]
print(hashtags)

users = ["Brandon", "Emma", "Brian", "Sophia", "Bella", "Ethan", "Ava", "Benjamin", "Mia", "Chloe"]
group = [x for x in users if x[0] == "B"]
print(group)