#while loop
# value=1
# while value<=10:
#     print(value)
#     if value==5:
#         break
#     value+=1

#contine
# value=1
# while value<=10:
#     value+=1
#     if value==5:
#         continue
#     print(value)
# else:
#     print("value is now equal to "+str(value))

# output
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# 11



#for loop
value=1
# names=["Ayush","Sam","John"]
# for x in names:
#     print(x)
# for x in "Nepal": #output : "N" "e" "p" "a" "l"
#     print(x)

# for x in names:
#     if x=="John":
#         break
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2,5):
#     print(x)

for x in range(0,100,5): #go from 0 to 100 but increment by 5 
    print(x)
else:
    print("Glad thats \'s over")


names=["Ayush","Sam","John"]
actions=["eats","sleeps","meditate"]

for name in names:
    for action in actions:
        print(name + " " + action+ ".")
# output
# Ayush eats.
# Ayush sleeps.
# Ayush meditate.
# Sam eats.
# Sam sleeps.
# Sam meditate.
# John eats.
# John sleeps.
# John meditate.