def find_max(numbers):
    if numbers:
        largest = numbers[0]
        rest = numbers[1:]
    else:
        return 0

    if rest:
        new_largest = find_max(rest)
        if largest < new_largest:
            largest = new_largest

    return largest

numbers = input()
numbers = numbers.split()
numbers = list(map(int,numbers))
print(find_max(numbers))