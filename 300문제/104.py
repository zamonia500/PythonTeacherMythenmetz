milk_order = {'101': {'서울유유(200ml)':1, '남양 요구르트': 5},
              '102': {'서울우유(500ml)':2},
              '103': {'남양우유(1L)': 1, '남양 요구르트': 10},
              '104': {'서울 요구르트': 15}
              }

for key, value in milk_order.items():
    print(key, sum(value.values()), '병')


for item in milk_order:
    print(item)

for value in milk_order.values():
    print(value)