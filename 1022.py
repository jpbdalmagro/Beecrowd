def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def sum(n1: int, n2: int, d1: int, d2: int) -> str:
    numerator = n1 * d2 + n2 * d1
    denominator = d1 * d2
    
    return f'{numerator}/{denominator} = {simplify(numerator, denominator)}' 

def minus(n1: int, n2: int, d1: int, d2: int) -> str:
    numerator = n1 * d2 - n2 * d1
    denominator = d1 * d2
    
    return f'{numerator}/{denominator} = {simplify(numerator, denominator)}' 

def multiply(n1: int, n2: int, d1: int, d2: int) -> str:
    numerator = n1 * n2
    denominator = d1 * d2
    
    return f'{numerator}/{denominator} = {simplify(numerator, denominator)}'

def divide(n1: int, n2: int, d1: int, d2: int) -> str:
    numerator = n1 * d2
    denominator = n2 * d1
    
    
    return f'{numerator}/{denominator} = {simplify(numerator, denominator)}' 

def simplify(numerator: int, denominator: int) -> str:
    divisor = gcd(numerator, denominator)
    numerator = numerator // divisor
    denominator = denominator // divisor
    
    return f'{numerator}/{denominator}'

cases = int(input())

for _ in range(cases):
    expression = input().split()
    operation = expression[3]
    numbers = list(filter(lambda x: x.isnumeric(), expression))
        
    match(operation):
        case '+':
            print(sum(int(numbers[0]), int(numbers[2]), int(numbers[1]), int(numbers[3])))
        case '-':
            print(minus(int(numbers[0]), int(numbers[2]), int(numbers[1]), int(numbers[3])))
        case '*':
            print(multiply(int(numbers[0]), int(numbers[2]), int(numbers[1]), int(numbers[3])))
        case '/':
            print(divide(int(numbers[0]), int(numbers[2]), int(numbers[1]), int(numbers[3])))
