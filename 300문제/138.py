def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)

    return result


result = pickup_even([1,2,3,4])

print(result)
