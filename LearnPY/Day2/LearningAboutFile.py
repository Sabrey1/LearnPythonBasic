#open file
'''
"r" = read
"w" = write
"a" = append
"b" = binary ("rb" = read binary, "wb" = write binary)
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
# print("Append Insert")
# lines = ["Fourth Line.\n","Fifth Line.\n"]
# file_object = open(file="test.txt",mode="a")
# file_object.writelines(lines)

#read
# print("Append Insert")
# file_object = open(file="test.txt",mode="r")
# print(file_object.readline()) #read one line, First Line
# line = file_object.readlines()
# file_object.close()
# print(line,type(line)) #read one line, First Line
# print(file_object.read()) #read all line

#use with = close file automatically
# with open(file="test.txt",mode="r") as file_object:
#     content = file_object.read()
#     print(content)

#read binary
with open('image.png','rb') as image_file:
    image_data = image_file.read()
    print(image_data)
#write binary
with open('copied_image.png','wb') as new_image_file:
    new_image_file.write(image_data)