import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# ========== ЗАДАЧА 1 ==========
print("=== ЗАДАЧА 1: ДЕЛЕНИЕ ДРОБЕЙ ===")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))
numerator = A * D
denominator = B * C
common_divisor = gcd(numerator, denominator)
simplified_num = numerator // common_divisor
simplified_den = denominator // common_divisor
print(f"Результат: {A}/{B} ÷ {C}/{D} = {simplified_num}/{simplified_den}")
# ========== ЗАДАЧА 2 ==========
print("\n=== ЗАДАЧА 2: ТОЧКИ В ОКРУЖНОСТИ ===")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
R = float(input("Введите R: "))
p1 = float(input("Введите p1: "))
p2 = float(input("Введите p2: "))
f1 = float(input("Введите f1: "))
f2 = float(input("Введите f2: "))
l1 = float(input("Введите l1: "))
l2 = float(input("Введите l2: "))
points_inside = 0
if (p1 - a)**2 + (p2 - b)**2 < R**2:
    points_inside += 1
    print("Точка P находится внутри окружности")
else:
    print("Точка P находится снаружи окружности")
if (f1 - a)**2 + (f2 - b)**2 < R**2:
    points_inside += 1
    print("Точка F находится внутри окружности")
else:
    print("Точка F находится снаружи окружности")
if (l1 - a)**2 + (l2 - b)**2 < R**2:
    points_inside += 1
    print("Точка L находится внутри окружности")
else:
    print("Точка L находится снаружи окружности")
print(f"Всего точек внутри окружности: {points_inside}")