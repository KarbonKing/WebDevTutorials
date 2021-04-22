#Lists
#Lists are filled with multiple "Elements"
groceries = ["apple", "banana", "oranges"]

print(groceries[0:2])

print("John likes " +groceries[2]+ ".")

for item in groceries:
    print(item)

groceries.append("grapes")
groceries.append("mangos")
print(len(groceries))
print(groceries)