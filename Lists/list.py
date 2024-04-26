#list are collection datatypes.they carry many values
users =['Dave','Ayush','Sam']
data =['Ayush',42,True]
emptyList=[]

print("Dave" in emptyList)# is dave in empty list?
print(users[0])
print(users[-1])
print(users.index('Sam'))#to know the position of the data
print(users[0:])
users.append('Elsa')
print(users)

users+= ['Jason']
print(users)

users.extend(['AyushKoBudi','AyushKoChora'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'BobKochora') #users.insert(index,string)
print(users)

users[2:2] = ['Eddie','Alex'] 
print(users)

users[1:3]=['Ronny',"Jenny"]
print(users)

users.remove('BobKochora')
print(users)

#pop list
print(users.pop())
print(users)

#del list
del users[0]
print(users)

# clear data
data.clear() #clears the data list = emtpty list
print(data)

##############----------------sorting
users[1:2]=['dave'] #['Ayush', 'AyushKoBudi', 'Elsa', 'Jason', 'Jenny', 'Sam', 'dave']
users.sort()
print(users)

#sorting with the lowest string
users.sort(key=str.lower) #['Ayush', 'AyushKoBudi', 'dave', 'Elsa', 'Jason', 'Jenny', 'Sam']
print(users)

nums=[3,43,23,14,144,45] 
nums.reverse() #[45, 144, 14, 23, 43, 3]
print(nums)

nums.sort(reverse=True) #[144, 45, 43, 23, 14, 3]
print(nums)

print(sorted(nums,reverse=True))
print(nums)
 
print("")
numscopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]

mycopy.sort()
print(mycopy)

print(numscopy)
print(mynums)

print(type(nums)) #datatype
print(type(mycopy))
print(type(mynums))

mylist=list([1,"Neil",True]) #[1, 'Neil', True]
print(mylist)


#tuples = the tuples can be defined as are very mush like list except the data inside the tuples will not change and the order will not change
mytuple = tuple(('Dave',42,True))
anotherTuple=(1,2,2,3,4,5)
print(mytuple)
print(anotherTuple)
print(type(anotherTuple))
print(type(anotherTuple))

#packing tuples
newList=list(mytuple) #creates a new list out of my tuples
newList.append('Neil')
newTuple=tuple(newList)
print(newTuple)

print("")
#unpacking tuples
(one,*two,hey)=anotherTuple
print(one)
print(two)
print(hey)

#to count how mamy occurance are there in the tupes
print(anotherTuple.count(2))






