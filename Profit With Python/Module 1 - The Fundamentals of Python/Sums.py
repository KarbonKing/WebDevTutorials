#Sum of numbers

rand_numbers = [6, 10, 20, 47, 69, 11, 50, 230]


def count_numbers(numbers):
    count = 0
    for number in numbers:
        count = count + number
    return count


print(count_numbers(rand_numbers))
#Or make it a string so that you can append "SUM:"
print("SUM: "  + str(count_numbers(rand_numbers)))