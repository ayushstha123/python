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

users+=['Json','Superman']
print(users)

users.extend(['Robert','Aayusha','Jimmy'])
print(users)

users.insert(0,'Bob')
print(users)

users[0:1]=['Casio','Omega']
print(users)

users.remove('Casio')

print(users)

users.pop()
print(users)

del users[0];
print(users)

# del users;# deletes the whole data
# print(users)

data.clear()
print(data)

users[1:2]=['davey']

users.sort()
print(users)#['Aayusha', 'Dave', 'Elsa', 'Json', 'Robert', 'Sam', 'Superman', 'davey']

users.sort(key=str.lower)
print(users)#['Aayusha', 'Dave', 'davey', 'Elsa', 'Json', 'Robert', 'Sam', 'Superman']

nums=[1,4,6,3,234,5]
nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)


