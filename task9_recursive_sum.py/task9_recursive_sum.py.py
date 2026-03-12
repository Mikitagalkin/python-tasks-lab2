#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа № 2: Структурное программирование на Python
Задание 9 (повышенной сложности): Рекурсивная сумма чисел

Демонстрирует:
- Переменные и типы данных (int, list)
- Рекурсивные функции
- Условные операторы (базовый случай рекурсии)
- Работу со списками
- Сравнение рекурсивного и итеративного подходов
- Стиль PEP8
- Модуль sys для установки глубины рекурсии
"""

import sys
import time


def recursive_sum(n):
    """
    Рекурсивное вычисление суммы чисел от 1 до n.
    
    Параметры:
        n (int): верхняя граница суммирования
        
    Возвращает:
        int: сумма чисел от 1 до n
        
    Рекуррентная формула:
        sum(n) = n + sum(n-1), при n > 0
        sum(0) = 0 (базовый случай)
    """
    # Базовый случай рекурсии
    if n <= 0:
        return 0
    
    # Рекурсивный случай
    return n + recursive_sum(n - 1)


def recursive_sum_with_trace(n, depth=0):
    """
    Рекурсивное вычисление суммы с трассировкой.
    
    Параметры:
        n (int): текущее число
        depth (int): глубина рекурсии
        
    Возвращает:
        int: сумма
    """
    indent = "  " * depth
    print(f"{indent}→ вызов recursive_sum({n})")
    
    if n <= 0:
        print(f"{indent}← базовый случай: возврат 0")
        return 0
    
    result = n + recursive_sum_with_trace(n - 1, depth + 1)
    print(f"{indent}← результат: {n} + sum({n-1}) = {result}")
    
    return result


def recursive_sum_digits(num):
    """
    Рекурсивное вычисление суммы цифр числа.
    
    Параметры:
        num (int): число
        
    Возвращает:
        int: сумма цифр
    """
    num = abs(num)  # Работаем с положительным числом
    
    # Базовый случай
    if num < 10:
        return num
    
    # Рекурсивный случай
    return num % 10 + recursive_sum_digits(num // 10)


def iterative_sum(n):
    """
    Итеративное вычисление суммы (для сравнения).
    
    Параметры:
        n (int): верхняя граница
        
    Возвращает:
        int: сумма
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def formula_sum(n):
    """
    Вычисление суммы по формуле арифметической прогрессии.
    
    Параметры:
        n (int): верхняя граница
        
    Возвращает:
        int: сумма
    """
    return n * (n + 1) // 2


def recursive_list_sum(lst):
    """
    Рекурсивное вычисление суммы элементов списка.
    
    Параметры:
        lst (list): список чисел
        
    Возвращает:
        int/float: сумма элементов
    """
    # Базовый случай: пустой список
    if not lst:
        return 0
    
    # Рекурсивный случай
    return lst[0] + recursive_list_sum(lst[1:])


def recursive_power(base, exponent):
    """
    Рекурсивное возведение в степень.
    
    Параметры:
        base (int): основание
        exponent (int): показатель степени
        
    Возвращает:
        int: base ** exponent
    """
    # Базовые случаи
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Рекурсивный случай
    return base * recursive_power(base, exponent - 1)


def measure_time(func, *args):
    """
    Измерение времени выполнения функции.
    
    Параметры:
        func: функция для измерения
        *args: аргументы функции
        
    Возвращает:
        tuple: (результат, время выполнения)
    """
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def compare_methods(n):
    """
    Сравнение различных методов вычисления суммы.
    
    Параметры:
        n (int): число для вычисления
    """
    print(f"\nСРАВНЕНИЕ МЕТОДОВ ДЛЯ N = {n}")
    print("-" * 50)
    
    # Увеличиваем глубину рекурсии для больших чисел
    if n > 1000:
        sys.setrecursionlimit(n + 1000)
    
    # Измерение времени для рекурсивного метода
    try:
        rec_result, rec_time = measure_time(recursive_sum, n)
        print(f"Рекурсивный метод:   {rec_result}, время: {rec_time:.6f} сек")
    except RecursionError:
        print(f"Рекурсивный метод:   НЕ ВЫПОЛНЕНО (превышена глубина рекурсии)")
    
    # Измерение времени для итеративного метода
    iter_result, iter_time = measure_time(iterative_sum, n)
    print(f"Итеративный метод:   {iter_result}, время: {iter_time:.6f} сек")
    
    # Измерение времени для формулы
    form_result, form_time = measure_time(formula_sum, n)
    print(f"Формула:              {form_result}, время: {form_time:.6f} сек")
    
    # Проверка совпадения результатов
    if iter_result == form_result:
        print(f"\n✓ Результаты совпадают: {iter_result}")
    else:
        print(f"\n✗ Ошибка: результаты не совпадают!")


def demonstrate_recursion_depth():
    """Демонстрация глубины рекурсии."""
    print("\nДЕМОНСТРАЦИЯ ГЛУБИНЫ РЕКУРСИИ")
    print("-" * 40)
    print(f"Текущая максимальная глубина рекурсии: {sys.getrecursionlimit()}")
    
    # Изменение глубины рекурсии
    sys.setrecursionlimit(2000)
    print(f"Установленная глубина: {sys.getrecursionlimit()}")
    
    # Тест с небольшим числом
    try:
        result = recursive_sum(10)
        print(f"recursive_sum(10) = {result}")
    except RecursionError:
        print("Ошибка рекурсии!")


def main():
    """Основная функция программы."""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Тема: Структурное программирование на Python")
    print("Задание: Рекурсивная сумма чисел")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    print("РЕКУРСИВНЫЕ ФУНКЦИИ")
    print("=" * 60)
    
    # Демонстрация глубины рекурсии
    demonstrate_recursion_depth()
    
    while True:
        print("\n" + "-" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1. Сумма чисел от 1 до N (с трассировкой)")
        print("2. Сумма чисел от 1 до N (без трассировки)")
        print("3. Сумма цифр числа")
        print("4. Сумма элементов списка")
        print("5. Возведение в степень")
        print("6. Сравнение методов")
        print("7. Тест производительности")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '0':
            print("\nПрограмма завершена. Спасибо за работу!")
            break
            
        try:
            if choice == '1':
                # Сумма с трассировкой
                n = int(input("Введите число N: "))
                if n < 0:
                    print("Число должно быть неотрицательным!")
                    continue
                    
                print(f"\nТРАССИРОВКА recursive_sum({n}):")
                result = recursive_sum_with_trace(min(n, 20))  # Ограничиваем для наглядности
                print(f"\nИтоговый результат: {result}")
                
            elif choice == '2':
                # Обычная сумма
                n = int(input("Введите число N: "))
                if n < 0:
                    print("Число должно быть неотрицательным!")
                    continue
                    
                result = recursive_sum(n)
                print(f"Сумма чисел от 1 до {n} = {result}")
                
            elif choice == '3':
                # Сумма цифр
                num = int(input("Введите число: "))
                result = recursive_sum_digits(num)
                print(f"Сумма цифр числа {num} = {result}")
                
            elif choice == '4':
                # Сумма списка
                input_str = input("Введите числа через пробел: ")
                numbers = [int(x) for x in input_str.split()]
                
                if not numbers:
                    print("Список пуст!")
                    continue
                    
                result = recursive_list_sum(numbers)
                print(f"Сумма элементов списка {numbers} = {result}")
                
            elif choice == '5':
                # Возведение в степень
                base = int(input("Введите основание: "))
                exp = int(input("Введите показатель степени: "))
                
                if exp < 0:
                    print("Показатель должен быть неотрицательным!")
                    continue
                    
                result = recursive_power(base, exp)
                print(f"{base} ** {exp} = {result}")
                
            elif choice == '6':
                # Сравнение методов
                n = int(input("Введите число для сравнения: "))
                if n < 0:
                    print("Число должно быть неотрицательным!")
                    continue
                    
                compare_methods(n)
                
            elif choice == '7':
                # Тест производительности
                print("\nТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ")
                test_values = [10, 100, 500, 1000, 5000]
                
                for n in test_values:
                    try:
                        print(f"\n--- N = {n} ---")
                        rec_result, rec_time = measure_time(recursive_sum, n)
                        iter_result, iter_time = measure_time(iterative_sum, n)
                        form_result, form_time = measure_time(formula_sum, n)
                        
                        print(f"Рекурсия:  {rec_time:.8f} сек")
                        print(f"Итерация:  {iter_time:.8f} сек")
                        print(f"Формула:   {form_time:.8f} сек")
                        
                    except RecursionError:
                        print(f"Рекурсия:  НЕ ВЫПОЛНЕНО (глубина рекурсии)")
                        
            else:
                print("Неверный выбор!")
                
        except ValueError:
            print("Ошибка: Введите корректное число!")
        except RecursionError:
            print("Ошибка: Слишком большая глубина рекурсии!")
        except KeyboardInterrupt:
            print("\n\nОперация прервана")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()