
def my_name():
    name = "jenan"
    print("My name is", name)

my_name()

def my_meal(food, drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal('cookies', "milk")

def cube(number):
   # return number*number*number
   return pow(number,3)

print(cube(9))

def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
print(by_three(4))