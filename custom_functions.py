#comment 1

def hello():
  print("Hello World!")

hello()
hello()
hello()

def sayHi():
  print("HI!")

sayHi()

#function arguments
def print_double(x):
   print(2 * x)

print_double(3)

def print_mult(x,y):
  print(x * y)

print_mult(4,5)

#returning from functions
def shortest_string(x,y):
  if len(x) >= len(y):
    return x
  else:
    return y
