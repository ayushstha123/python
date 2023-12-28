#list are collection datatypes.they carry many values
users =['Dave','Ayush','Sam']
data =['Ayush',42,True]
emptyList=[]

print("Dave" in emptyList)# is dave in empty list?
print(users[0])
print(users[-1])
print(users[-1])
print(users.index('Sam'))#to know the position of the data
print(users[0:])
users.append('Elsa')
print(users)

users+=['Json','Superman']
print(users)

users.extend(['Robert','Aayusha','Jimmy'])
print(users)

users.insert(0,'Boob')
print(users)