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
