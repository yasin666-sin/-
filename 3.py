def Задача_1():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    for i in range(a, b + 1):
        print(i)

def Задача_2():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    if a <= b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)

def Задача_3():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    start = a if a % 2 != 0 else a - 1
    for i in range(start, b - 1, -2):
        print(i)

def Задача_4():
    n = int(input("Введите количество чисел N: "))
    numbers = []
    for _ in range(n):
        num = int(input("Введите число: "))
        numbers.append(num)
    print(sum(numbers))

def Задача_5():
    n = int(input("Введите n: "))
    result = sum(i**3 for i in range(1, n + 1))
    print(result)

def Задача_6():
    n = int(input("Введите n: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

def Задача_7():
    n = int(input("Введите n: "))
    total_sum = 0
    current_factorial = 1
    for i in range(1, n + 1):
        current_factorial *= i
        total_sum += current_factorial
    print(total_sum)

def Задача_8():
    n = int(input("Введите n: "))
    for i in range(1, n + 1):
        print(''.join(map(str, range(1, i + 1))))

def Задача_9():
    def fibonacci_sum(n):
        if n == 0 or n == 1:
            return n
        prev = 0
        curr = 1
        result = 1
        for _ in range(2, n + 1):
            next_num = prev + curr
            result += next_num
            prev, curr = curr, next_num
        return result
    n = int(input("Введите N: "))
    print(fibonacci_sum(n))

Задачи = {
    Задача_1 : '1',
    Задача_2 : '2',
    Задача_3 : '3',
    Задача_4 : '4',
    Задача_5 : '5',
    Задача_6 : '6',
    Задача_7 : '7',
    Задача_8 : '8',
    Задача_9 : '9',
}

while True:
    choice = input("""
Выберите номер задачи:
1. Все числа от A до B
2. Числа от A до B по порядку возрастания или убывания
3. Нечётные числа от A до B в обратном порядке
4. Сумма введённых N чиселСумма введённых N чисел
5. Кубическая сумма от 1 до n
6. Факториал числа n
7. Сумма факториалов от 1 до n
8. Лесенка чисел
9. Сумма первых N чисел Фибоначчи
quit. Выход
Ваш выбор: """)
    if choice.lower() == 'q':
        break
    elif choice not in Задачи:
        print("Неверный выбор.")
    else:
        Задачи[choice]()