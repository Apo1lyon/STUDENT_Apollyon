# Инициализируем сумму
sum_of_squares = 0

# Используем цикл for в сочетании с range для вычисления суммы квадратов
for i in range(1, 11):
    sum_of_squares += i ** 2  # Добавляем квадрат числа к сумме

# Выводим результат
print("Сумма квадратов чисел от 1 до 10:", sum_of_squares)

input()