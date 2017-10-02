def pickup_even_by_iter(items):
    for item in items:
        if item % 2 == 0:
            yield item



items = [1,2,3,4,5,6]
for item in pickup_even_by_iter(items):
    print(item)

