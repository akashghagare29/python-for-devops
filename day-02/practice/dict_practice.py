info = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "Married": True,
    "skills": ["Python", "JavaScript", "SQL"]
}
print(type(info))
print("I live in " + info["city"])
print("I have skills: ", info.get("skils", "Not Found"))
info.update({"country": "India"})
print("Updated Info:", info)
print(dir(info))
print(info.get.__doc__)

# Iterate through the dictionary and print key-value pairs
for key,value in info.items():
    print(key, ":", value)