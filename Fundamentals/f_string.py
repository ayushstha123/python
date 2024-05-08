person="Dave"
coins=3

print("\n" +person +" has " +str(coins)+" coins")
message = "\n%s has %s coins" %(person ,coins)
message2 = "\n{} has {} coins" .format(person ,coins)
message3 = "\n{1} has {0} coins" .format(person ,coins) #index
message4 = "\n{person} has {coins} coins" .format(person=person ,coins=coins)

#dictionary
player={'person':'Ayush','coins':3}
message5 = "\n{person} has {coins} coins" .format(**player)

print(message)
print(message2)
print(message3)
print(message4)
print(message5)

#f string 
message6 = f"\n{person} has {coins} coins" 
print(message6)

message6 = f"\n{person} has {2*3} coins" 
print(message6)

message6 = f"\n{player['person']} has {2*3} coins" 
print(message6)

num=10
print(f"2.25 times {num} is {2.25*num:.2f}")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25*num:.2f}")


