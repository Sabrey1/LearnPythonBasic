#loop 

#for loop
#while loop

#for loop
fruits = ["apple","banana","mango"]
for ele in fruits:
    print(ele)

#while loop
count =1
while count <=3:
    print("Counting:",count)
    count +=1

#Break statement
print("Break statement")
for number in range(5):
    if number ==3:
        break
    print(number)

#Continue statement
print("Continue statement")
for numbers in range(5):
    if numbers == 3:
        continue
    print(numbers)
