def nums(numbers):
    if len(numbers) < 3:
        return 0

    count = 0
    for index in numbers:
        if index != numbers[0] and index != numbers[1]:
            count += 1
    return count

s = nums([3, 6, 1, 7, 5, 4, 2, 1, 7, 8, 1, 3, 0])
print(s)
# nums = [4, 3, 2, 2, 5, 4, 3]
# output: 3