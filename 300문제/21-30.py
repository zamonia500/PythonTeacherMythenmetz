print('number:21')
companies = ['NAVER', 'KAKAO', 'SK', 'SAMSUNG']
print(';'.join(companies))


print('number:21')
companies = '000660;060310;0133340;095570;068400;006840'
print(companies.split(';'))

print('number:30')
letters = "introducing python"
str_length = len(letters)
half = str_length // 2
print(letters[:half], letters[half:], sep='\n')