def employee(age):
    if age < 18:
        return "Not eligible for employment."
    elif age >= 18 and age <= 75:
        return "Eligible for employment."
    else:
        return "Retirement age reached."


employee_age = int(input("Enter the age of the employee: "))
result = employee(employee_age)
print(result)