#For Loops



for number in range(1, 11):
    if number == 10:
        print("Boom")
    else:
        print(number)



#For loops can be used to count the number of letters in a string.

count = 0

for letter in "Helper":
    count = count + 1
print(count)

def string_length(word):
    count = 0
    for letter in word:
        count = count + 1
    return count


#return is being used to give the output of the count variable