#comment 1

def shout(text):  
    return text.upper()
yell = shout
print(yell("Hello"))


def order(dish):
    return "Your order: " + dish

def process_order(dish, func):
    print(func(dish))


#pure function

def product:
  return 2*4


#lambda expressions
lambda x: x+5

lambda word: "#" + word

discount = lambda price: price * 0.9
print(discount(100))

lambda width, height: width*height

res = (lambda x, y: x*y)(2,3)
print(res)

def mult(n):
  return lambda a: a*n

doubler = mult(2)
tripler = mult(3)

a = 2
double_a = doubler(a)
triple_a = tripler(a)



#map and filter
prices = [25.99, 34.99, 27.99, 37.99, 32.99]
def discount(price):
  discounted_price = price*0.9
  return discounted_price
discounted_prices = list(map(discount, prices))

map(lambda x: x+5, scores)

filter(lambda price: price > 90, prices)


#args and kwargs
def total(numbers):
  result = 0
  for i in numbers:
    result += i
  return result

def total(*args):
  result = 0
  for arg in args:
    result += arg
  return result
print(total(1,2,3,4,5))

def show_items(category, *items):
  print("Category: ", category)
  for item in items:
    print item
show_items("Electronics", "Laptop", "Smartphone")