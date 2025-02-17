# Напишите программу на Python для получения суммы неотрицательных целых чисел с помощью рекурсии.

# Вам поможет различные операции деления, такие как: % (нахождение остатка от деления) и // (целочисленное деление)
def sum_of_non_negative_integers(n):
    if n == 0:
        return 0

    else:
        return n + sum_of_non_negative_integers(n - 1)

number = int(input("Введите неотрицательное целое число: "))
if number < 0:
    print("Пожалуйста, введите неотрицательное целое число.")
else:
    result = sum_of_non_negative_integers(number)
    print(f"Сумма всех неотрицательных целых чисел от 0 до {number} равна {result}.")