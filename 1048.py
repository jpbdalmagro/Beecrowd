salary = float(input())

def salary_reajust(salary):
    if salary <= 400:
        percentual = 15
    elif salary <= 800:
        percentual = 12
    elif salary <= 1200:
        percentual = 10
    elif salary <= 2000:
        percentual = 7
    else:
        percentual = 4
    earned = salary * percentual / 100
    return salary + earned, percentual, earned

new_salary, percentual, earned = salary_reajust(salary)

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {earned:.2f}")
print(f"Em percentual: {percentual} %")
