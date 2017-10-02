def calc_monthly_salary(annual_salary):
    result = annual_salary // 12

    return (result // 100) * 100

result = calc_monthly_salary(13000000)
print(type(result))
print(result)