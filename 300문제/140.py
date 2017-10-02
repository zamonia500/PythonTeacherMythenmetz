def remove_duplication(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)

    return result


items = [1,1,2,3,4,4,6,6,7]
result = remove_duplication(items)
print(result)