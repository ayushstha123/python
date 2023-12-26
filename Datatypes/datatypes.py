#string data type

#literal assignment
first ="ayush"
last="shrestha"
# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))

#construction function
# pizza=str("pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

#CONCATINATION
# fullname=first + " "+last
# print(fullname)
# fullname+= "!!"
# print(fullname)

#casting a number to a string
decade=str(1980)
print(type(decade))

statement="i like rock music from the "+ decade+"s"
print(statement)

#multiple lines
multipleline='''

hey how are you ?

i was just cheeking in bro 

            all good

'''
print(multipleline)


#escaping special characters
sentence='I\'m back at work !\t hey \n hellowww \\ located ?'
print(sentence)

#string method
print(first)
print(first.lower())
print(first.upper())
print(first)


print(len(multipleline))

#concat
multipleline+='              '
print(len(multipleline))

#to remove whitespace
print(len(multipleline.strip()))
print(len(multipleline.lstrip()))#removing whitespace from left 
print(len(multipleline.rstrip()))#removing whitespace from right 

print("")

title="menu".upper()
print(title.center(30,'-')) #to put the menu in the center 
print("Coffee".ljust(25,'.') + "Rs.20".rjust(4)) #ljust=left justify //// rjust=right justify
print("Muffin".ljust(25,'.') + "Rs.40".rjust(4))
print("Chiya".ljust(25,'.') + "Rs.90".rjust(4))


#string index value
print("")
#first=ayush
print(first[1])# -->y
print(first[-1]) #-->h
print(first[1:-1])# Ayush --> yus (range of value) start from y and end in h
print(first[1:])# from a specific point to last

#some methods return boolean data
print(first.startswith("a"));#--true 
print(first.endswith("a"));#--false

print("")
#Boolean data type
myvalue=True #dont use true small letter t
x=bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#Numeric data type
#integer type
print("")
price=100
bestPrice=int(80)
print(type(price))
print(type(bestPrice))
print(isinstance(bestPrice,int));

#Float type
print("")
gpa=3.27
y=float(1.4)
print(type(gpa))
print(type(y))
print(isinstance(gpa,float));

#complex type
comp_value=5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print(abs(gpa))
print(round(gpa))
print(round(gpa,1))

print("")

import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

zipcode='10001'
zip_value=int(zipcode)
print(type(zip_value))
