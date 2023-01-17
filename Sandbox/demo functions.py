
def print_goodmorning(name = 'stranger', repeat = 1):
    for _ in range(repeat):
        print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi

def add(n1: int, n2: int) -> int:
    return n1 + n2


# --------------------------------------------

print_goodmorning('Peter')
print_goodmorning('Frank', 10)
print_goodmorning()

print(calculate_bmi(90, 1.80))

print(add(23, 34))
print(add('23', '34'))
print(add([1,2], [3,4]))
