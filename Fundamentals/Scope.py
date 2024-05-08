#global scope
name="Ayush"
count=1
def anotherGreeting():
    color="blue"
    # count +=1
    print(count)
    def greetings(name):
        nonlocal color
        color="red"
        print(color)
        print(name)

    greetings("Ayush")
anotherGreeting()

