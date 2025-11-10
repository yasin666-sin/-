def calculate_term_recursive(x: float, n: int) -> float:
    """
    Вычисляет выражение x^n / n! с помощью рекурсии (без циклов).
    
    Параметры:
    x (float): Основание степени.
    n (int): Показатель степени и аргумент факториала (натуральное число).
    
    Возвращает:
    float: Значение выражения x^n / n!.
    """
    
    # Проверка на натуральное число (n >= 0)
    if n < 0:
        raise ValueError("N должно быть натуральным числом (или нулем).")

    # Базовый случай: x^0 / 0! = 1 / 1 = 1
    if n == 0:
        return 1.0
    
    # Рекурсивный шаг: 
    # Текущий член = Предыдущий член * (x / n)
    # Предыдущий член: x^(n-1) / (n-1)!
    
    # Рекурсивный вызов для получения предыдущего члена
    prev_term = calculate_term_recursive(x, n - 1)
    
    # Вычисление текущего члена
    current_term = prev_term * (x / n)
    
    return current_term

# --- Тестирование программы ---

X_val = 2.0
N_val = 5

try:
    result = calculate_term_recursive(X_val, N_val)
    print(f"Дано X = {X_val}, N = {N_val}")
    print(f"Результат (X^N / N!): {result}")
    
    # Проверка (2^5 / 5! = 32 / 120 ≈ 0.26666...)
    
    X_val_2 = 3.0
    N_val_2 = 3
    result_2 = calculate_term_recursive(X_val_2, N_val_2)
    print(f"\nДано X = {X_val_2}, N = {N_val_2}")
    print(f"Результат (X^N / N!): {result_2}")
    # Проверка (3^3 / 3! = 27 / 6 = 4.5)
    
except ValueError as e:
    print(f"Ошибка: {e}")