#open file
'''
"r" = read
"w" = write
"a" = append
"b" = binary
'''

#single insert
# print("Single Insert")
# file_object = open(file="test.txt",mode="w")
# file_object.write("Hello World.\n")
# file_object.write("This is Second Line.\n")

#multiple insert
# print("Multiple Insert")
# lines = ["First Line.\n","Second Line.\n","Third Line.\n"]
# file_object = open(file="test.txt",mode="w")
# file_object.writelines(lines)

#append insert
print("Append Insert")
lines = ["Fourth Line.\n","Fifth Line.\n"]
file_object = open(file="test.txt",mode="a")
file_object.writelines(lines)

