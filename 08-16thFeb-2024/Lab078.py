# Dict
# key and value
name = "Prachitosh"
# key -> name


value = "Prachitosh"
# A dictionary is an unordered collection of data.
# in  a key-value pair format


my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))

phone_book = {"Batman": 9876876890, "Superman": 8908908907, "Wonder": 98760987}
print(len(phone_book))
print(phone_book["Batman"])

phone_book2 = dict(batman=123, cersei=342, GB=323)
print(phone_book2)
print(phone_book2["GB"])  # 323
print(phone_book2['GB'])  # 323
print(phone_book2.get('GB'))  # 323
print(phone_book2.get("GB"))  # 323

prachitosh_details = dict(name="Prachitosh", age="28", isMale=True, Address="Puri")
prachitosh_details2 = {"name": "Prachitosh", "28": 34.34, "isMale": True, "Address": "Puri"}
print(prachitosh_details2.get("28"))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(len(my_dict))
print(my_dict)
