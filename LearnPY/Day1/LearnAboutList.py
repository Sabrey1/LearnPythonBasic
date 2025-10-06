#Learning about List (Data Struture)
#list = 
#int, string,float, boolean, list

#list method

#syntx 
#my_list = []
my_list = [1,"apple",True,3.14,"mango",190]
print(my_list)
#my_list.append("banana") #.append add element to list
my_list.remove("mango") #.remove remove element to list
print(my_list)
#indexing
# print(my_list[3])
#slicing 
# print(my_list[1:4])

#sorting list
print("Sorting List")
my_list1 = [2,5,8,1,3,9,4,6,7]
# my_list1.sort()
print(my_list1)

#reverse
my_list1.reverse()
print(my_list1)

#check length of list1
# length = len(my_list1)
# print(length)

#check index of list1
# [2, 5, 8, 1, 3, 9, 4, 6, 7]
index = my_list1.index(5)
print(index) #index of 5 is 1

