def calculator(operation: str, num1: float, num2: float) -> float:
    """
    Выполняет основные математические операции (+, -, *, /) над двумя числами.

        Примеры использования:
        >>> calculator('+', 5, 5)
        10.0
        >>> calculator('-', 9, 4)
        5.0
        >>> calculator('*', 9, 8)
        72.0
        >>> calculator('/', 10, 2)
        5.0
        >>> calculator('/', 3, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Деление на ноль невозможно.
        >>> calculator('%', 5, 1)
        Traceback (most recent call last):
            ...
        ValueError: Недопустимая операция '%'. Допустимые операции: +, -, *, /.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return num1 / num2
    else:
        raise ValueError(f"Недопустимая операция '{operation}'. Допустимые операции: +, -, *, /.")


# Использования функции
if __name__ == "__main__":
    # Ввод от пользователя
    try:
        
        op = input("Введите операцию (+, -, *, /): ").strip()
        n1 = float(input("Введите первое число: "))
        n2 = float(input("Введите второе число: "))

        # Выполнение операции и вывод результата
        result = calculator(op, n1, n2)
        print(f"Результат: {result}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except ZeroDivisionError as zde:
        print(f"Ошибка: {zde}")