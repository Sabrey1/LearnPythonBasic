#set 
#not duplicate
#syntax
#my_set = {element1,element2,element3}

fruits = {"apple","banana","mango"}
#add element to set
fruits.add("orange")
print(fruits)

#remove element to set
fruits.remove("apple")
print(fruits)

#set oparation
set1 = {1,2,3,4,5,10}
set2 = {4,5,6,7,8}
#union រួមបញ្ចូល
print(set1.union(set2))

#intersection​ យកចំនួនប្រសព្វ
print(set1.intersection(set2))

#difference​  បង្ហាញធាតុទាំងអស់ដែលមាននៅក្នុង A ប៉ុណ្ណោះ មិនមានក្នុង B ទេ។
print(set1.difference(set2))

#symmetric_difference វាត្រឡប់តម្លៃ ធាតុទាំងឡាយដែលមាននៅក្នុង set1 ឬ set2 ប៉ុណ្ណោះ តែមិនមានទាំងពីរ(duplicate)នៅពេលតែមួយ។
print(set1.symmetric_difference(set2))