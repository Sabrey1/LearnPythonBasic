#learning about string

#Single-quoted string
single_quote_str = 'Hello World'
print(type(single_quote_str))

#Double-quoted string
double_quote_str = 'Hello World'
print(type(double_quote_str))

#Connect String
print("+++++++++++Connect String+++++++++++")
#1- Concatenation (combine)

first_name = "Sabrey"
last_name = "Lim"
fullName = first_name + " " + last_name
print(fullName)

#2- Repetition
print("+++++++++++Repetition+++++++++++")
# print("+++++++++++វិធីទទួល​ string ដដែលច្រើនដង+++++++++++")
echo = "Hello " * 3
print(echo)

#3- Indexing - start from 0
#Learn about index String
print("+++++++++++Learn about index String+++++++++++")
text = "ABC"

print(text[0])#print A
print(text[-1])#print C [-] count from Back

#4- slicing - start from 0
text2 = "Mango"
print(text2[:3]) #start from 0 -> index 3
print(text2[2:5])
print(text2[2:]) #count 2-end

#5- string method
#.upper() convert text form Uppercase
#.lower() convert text form Lowercase
#.title() convert text form first word to Uppercase
text3 = "Hello world"
print(text3.upper())
print(text3.lower())
print(text3.title())

#6- format string
name = "Sabrey"
age = 20

greeting = "Hello, {}. Your are {} years old.".format(name,age)
# Hello, Sabrey. You are 20 years old.
print(greeting)

print("Format string using f")
greeting1 = f"Hello, {name}. Your are {age} years old."
print(greeting1)