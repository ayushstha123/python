# r=Read
# a=Append
# w=Write
# x=Create

# 1. Read - error if it doesn't exists
f=open("names.txt")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()


try:
    f=open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesnt exists")
finally:
    f.close()


###### 2.APPEND - creates the file if it doesnt exists
f=open("names.txt","a")
f.write("Neppa")
f.close()

f=open("names.txt")
print(f.read())

####WRITE (Overwrite)
f=open("context.txt","w")
f.write("hello i deleted all of the context available")
f.close()

f=open("context.txt")
print(f.read())


#two ways to create a new file

#opens a file for writing ,creates the file if it doesnt exist
f=open("name_list.txt","w")
f.close()

#create the specified file but returns an error if the file exists
import os
if not os.path.exists("dave.txt"):
    f=open("dave.txt","x")
    f.close()

#delete a file 
#avoid an error if it doesnt exits
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete doesnt exists")

# the with statement is used to wrap the execution of a block of code with methods defined by a context manager. 
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised during the execution of the block.
with open("moreNames.txt") as f:
    content=f.read()

with open("names.txt","w") as f:
    f.write(content)