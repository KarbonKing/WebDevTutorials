#Lets get max number from a list

invoices = [6, 10, 20, 47, 69, 11, 50, 230, 20, 24, 39, 29]

count = 0

for number in invoices:
    if count < number:
        count = number

print(invoices)
print("Max = "+ str(count))
print("")
print('_____________OR_____________')
print("")

def min_num(list):
    smallest = list[0]
    for number in list:
        if smallest > number:
            smallest = number
    return smallest

def max_num(list):
    biggest = list[0]
    for number in list:
        if biggest < number:
            biggest = number
    return biggest

mini = min_num(invoices)
maxim = max_num(invoices)

print(invoices)
print("Minimum: "+ str(mini))
print("Maximum: "+ str(maxim))