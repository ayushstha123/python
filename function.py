def hello():
    print("hello world")

hello()

def sum(num1,num2):
    if(type(num1)is not int or type(num2) is not int):
        return
    return print(num1+num2)

total=sum("a",4)
print(total)

# The * symbol is used in Python to denote variable number of arguments. When you call multiple_items("Ayush", "Suman", "Sabin"), the *args in the function definition collects all the arguments into a tuple. 
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Ayush","Suman","Sabin")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(name="ayush",last="shrestha")