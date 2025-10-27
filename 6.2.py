def task1():
    print("\n=== ЗАДАЧА 1 ===")
    print("Работа с массивом вещественных чисел")
    try:
        n = int(input("Введите размер массива N: "))
        if n <= 0:
            print("Размер массива должен быть положительным числом!")
            return
        arr = []
        print(f"Введите {n} вещественных чисел:")
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Элемент [{i + 1}]: "))
                    arr.append(num)
                    break
                except ValueError:
                    print("Ошибка! Введите вещественное число.")
        min_abs_element = min(arr, key=abs)
        min_abs_index = arr.index(min_abs_element)
        print(f"\nИсходный массив: {arr}")
        print(f"Минимальный по модулю элемент: {min_abs_element}")
        print(f"Его индекс: {min_abs_index}")
        print(f"Массив в обратном порядке: {arr[::-1]}")
    except ValueError:
        print("Ошибка ввода! Убедитесь, что вводите корректные числа.")


def task2():
    print("\n=== ЗАДАЧА 2 ===")
    print("Работа с массивами A и B")
    try:
        print("Введите 10 элементов для массива A:")
        A = []
        for i in range(10):
            while True:
                try:
                    num = int(input(f"A[{i + 1}]: "))
                    A.append(num)
                    break
                except ValueError:
                    print("Ошибка! Введите целое число.")

        print("\nВведите 10 элементов для массива B:")
        B = []
        for i in range(10):
            while True:
                try:
                    num = int(input(f"B[{i + 1}]: "))
                    B.append(num)
                    break
                except ValueError:
                    print("Ошибка! Введите целое число.")
        print(f"\nИсходный массив A: {A}")
        print(f"Исходный массив B: {B}")
        A, B = B, A
        print("\nПосле обмена содержимым:")
        print(f"Массив A: {A}")
        print(f"Массив B: {B}")
    except ValueError:
        print("Ошибка ввода! Убедитесь, что вводите корректные целые числа.")

def task2_demo():
    """Демонстрационная версия задачи 2 с заранее заданными массивами"""
    print("\n=== ЗАДАЧА 2 (демо) ===")
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("Исходные массивы:")
    print(f"Массив A: {A}")
    print(f"Массив B: {B}")
    A, B = B, A
    print("\nПосле обмена содержимым:")
    print(f"Массив A: {A}")
    print(f"Массив B: {B}")
def main():
    print("ПРОГРАММА ДЛЯ РАБОТЫ С МАССИВАМИ")
    print("=" * 50)
    while True:
        print("\nВыберите задачу:")
        print("1 - Работа с массивом вещественных чисел")
        print("2 - Обмен содержимым массивов A и B (ручной ввод)")
        print("3 - Обмен содержимым массивов A и B (демо)")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task2_demo()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")
if __name__ == "__main__":
    main()