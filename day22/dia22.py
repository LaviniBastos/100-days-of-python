def max_list(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


print(max_list([1,4,6,30]))
print(max_list([3,40,60,50,500]))