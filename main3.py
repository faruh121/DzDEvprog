import time

def find_min_iterative(numbers):
    """Находит минимальный элемент обычным способом."""
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def find_min_recursive(numbers, n):
    """Находит минимальный элемент рекурсивным способом."""

    if n == 1:
        return numbers[0]
    else:

        return min(numbers[n - 1], find_min_recursive(numbers, n - 1))


try:
    n = int(input("Введите размер списка (n): "))
    if n <= 0:
        raise ValueError("Размер списка должен быть положительным.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
    exit(1)


numbers = []
for i in range(n):
    try:
        num = float(input(f"Введите число {i + 1}: "))
        numbers.append(num)
    except ValueError:
        print("Ошибка: введено не числовое значение.")
        exit(1)


start_time_iterative = time.time()
min_iterative = find_min_iterative(numbers)
end_time_iterative = time.time()
time_iterative = end_time_iterative - start_time_iterative


start_time_recursive = time.time()
min_recursive = find_min_recursive(numbers, n)
end_time_recursive = time.time()
time_recursive = end_time_recursive - start_time_recursive


with open('results.txt', 'w', encoding='utf-8') as f:
    f.write(f"Минимальное значение (обычно): {min_iterative}\n")
    f.write(f"Время выполнения (обычно): {time_iterative:.6f} секунд\n")
    f.write(f"Минимальное значение (рекурсивно): {min_recursive}\n")
    f.write(f"Время выполнения (рекурсивно): {time_recursive:.6f} секунд\n")

print("Результаты записаны в файл 'results.txt'.")