import time

def print_rules():
    print("\nЕсли я отгадал напиши '=', \nесли число меньше напиши '<', \nесли число больше напиши '>'")

a, b = 1, 100
print(f'Загадай число от {a} до {b}')
time.sleep(3)
print('Загадал?')
time.sleep(1)
print('Тогда поехали!')
time.sleep(1)
print_rules()
steps = 0

while True:
    number = (a + b) // 2
    print(f'Это {number}?')
    znak = input()
    steps += 1

    if a == b or a > b:
        print('Упс, что-то пошло не так')
        print('На всякий случай напомню правила игры')
        print_rules()
        steps -= 1

    if znak == '=':
        print('Это было легко)')
        print(f'Твое число: {number}')
        print(f'Количество шагов: {steps}')
        break
    
    if znak == '>':
        a = (a + b) // 2

    if znak == '<':
        b = (a + b) // 2