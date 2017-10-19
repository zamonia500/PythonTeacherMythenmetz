def get_hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return -1

    hd = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hd += 1
    return hd

str1 = "karolin"
str2 = "kathrin"

a = get_hamming_distance(str1, str2)
print(a)