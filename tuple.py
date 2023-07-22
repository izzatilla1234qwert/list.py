# # thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# # print(thistuple)


# # thistuple = ("apple",)
# # print(type(thistuple))

# #NOT a tuple
# # thistuple = ("apple")
# # print(type(thistuple))



# # tuple1 = ("apple", "banana", "cherry")
# # tuple2 = (1, 5, 7, 9, 3)
# # tuple3 = (True, False, False)


# # tuple1 = ("apple", "banana", "cherry")
# # tuple2 = (1, 5, 7, 9, 3)
# # tuple3 = (True, False, False)

# # mytuple = ("apple", "banana", "cherry")
# # print(type(mytuple))

# # thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# # print(thistuple)

# new_tuple =('a','b','c','d')

# del list(new_tuple)

# # new_tuple.append('e')    #ERROR


# print(new_tuple.count('c'))

# print(new_tuple.index('d'))




# Mashinalr = ("lacetti","Ferrari",'tesla',"Mercedes benz","lamb")

# print(Mashinalr.count('lacetti') > 0 )
# print(Mashinalr.count('BMW') > 0 )
# print(len(Mashinalr))

# # print(Mashinalr('tesla'))

# print(Mashinalr[0:3])

# print(Mashinalr[2])

# print(Mashinalr[-1])

Uzafto = ("lacetti","Ferrari",'tesla',"Mercedes benz","lamb")
BMW = ("lamb","Ferrari",'tesla',"Mercedes benz","lacetti")
Uzafto1 = list(Uzafto)
BMW1 = list(BMW)   

Uzafto1.extend(BMW1)
print(Uzafto1)

del Uzafto1[2]
print(Uzafto1)

del BMW1[2]
print(BMW1)

BMW1.append('toyota')
print(BMW1)

Uzafto1.append('toyota')
print(Uzafto1)  


a= ('1',)

print(type(a))
