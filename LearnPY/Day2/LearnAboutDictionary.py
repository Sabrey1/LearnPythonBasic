#Dictionary
#store: key, value
#key must be unique, value can be duplicate, value can be any data type

#syntax
# my_dict = {"key": "value"}

persion = {"name":"sabrey","age":20,"city":"Siem Reap"}

print(persion["name"])

#adding item to dict
persion["job"] = "student"

#update item to dict
print("update item to dict")
persion["age"] = 21
print(persion)

#update mutiple item in dict
print("update mutiple item in dict")
persion.update({"age":22,"job":"Developer","city":"Phnom Penh"})
print(persion)

#remove item from dict
print("remove item from dict")
del persion['city']
print(persion)

#get key
print("get key")
print(persion.keys())

#get value
print("get value")
print(persion.values())

#method clear
print("method clear")
persion.clear()
print(persion)