#dictionary are used to store data values that are in key value pairs
band={ #1 st way to make dictionary
    "vocals":"Ayush",
    "guitar":"Sam",
}
print(band)

band2=dict(vocals='Ayush',guitar='Sam')# 2nd way to make dictionary
print(band2)

#---------how can we access dictionary values
#1st method
print(band["vocals"])
#2nd method
print(band.get("guitar"))

#list only keys
print(band.keys())

#list only values
print(band.values())

#list key/value in the form of tuples
print(band.items())

#to verify a key is in the dictionary
print("guitar" in band)
print("triagnle" in band)

#changes
band["vocals"] ="Ayushstha"
band.update({"bass":"Shusu"}) #adding items

print(band)

#removing itemsclear
print(band.pop("bass"))
print(band)

band["drums"]="bohemsn"
print(band)

print(band.popitem()) #returns tuple
print(band)

#delete and clear item
band["drums"]="bottom"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
# band2=band #create a reference
# print("badcopy")
# print(band2)

# print(band)

# band2["drums"]="Ayushaa"
# print(band)


#how to copy dict
band2=band.copy()
band2["drums"]="Agugu"
print("Good copy")
print(band)
print(band2)

#or use the dict() constructor function to make a copy
band3=dict(band)
print("good copy")
print(band3)

#nested dictionaries
member1={
    "name":"Ayush",
    "instrument":"vocals"
}
member2={
    "name":"pogo",
    "instrument":"guitar"
}
band={
    "member1":member1,
    "member2":member2
}
print(band)
print(band["member1"]["name"]) # to drill down the dictionary and get the specified value


#sets

nums={1,2,3,4}
nums2=set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))

#no dublicates allowed
nums={1,2,2,4} #sets ignores the dublicate
print(nums)

#true is a dupe of 1, False is a dupe of zero
nums={1,True,2,0,False,4,5,67,22,12}
print(nums)

#check if a value is in sets
print(2 in nums)
print(67 in nums)

#but you cannot refer to an element in the set with an index position or a key
#adding a new element to a set
nums.add(8)
print(nums)

#to add elements from one sets to another
morenums={99,100,200}
nums.update(morenums)
print(nums)

#you can use update with list ,tuples and dictionaries too

#merge two sets to create a new sets
one={1,2,3}
two={4,5,6}
mynewset=one.union(two)
print(mynewset)

#keep only the dublicate in the merged sets
one={1,2,3}
two={2,3,6}

one.intersection_update(two)
print(one)

#keep everything except the dublicate in the merged sets
one={1,2,3}
two={2,3,6}

one.symmetric_difference_update(two)
print(one)
