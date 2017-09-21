dong = ['201동', '202동', '203동']
room = ['101호', '102호', '201호', '202호',
        '301호', '302호', '401호', '402호']

hello = {'dong':['201동', '202동', '203동'],
         'room':['101호', '102호', '201호', '202호',
                 '301호', '302호', '401호', '402호']}

for dong in hello['dong']:
    for room in hello['room']:
        print(dong, room)

int_arr = [7,1,9,5,2,11,84,2,7,6,4]
print(max(int_arr))
print(min(int_arr))

max_value = int_arr[0]
for value in int_arr[1:]:
    if value > max_value:
        max_value = value
print(max_value)