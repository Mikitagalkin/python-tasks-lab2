#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа № 2: Структурное программирование на Python
Задание 4 (средней сложности): НОД двух чисел

Демонстрирует:
- Переменные и типы данных (int)
- Условные операторы if/elif/else
- Цикл while
- Функции: def, параметры, return
- Стиль PEP8
- Модуль math (используется для сравнения)
"""

import math  # Демонстрация импорта модуля


def gcd_euclid(a, b):
    """
    Функция для нахождения НОД с использованием алгоритма Евклида.
    
    Параметры:
        a (int): первое число
        b (int): второе число
    
    Возвращает:
        int: наибольший общий делитель
    """
    # Берем абсолютные значения для работы с отрицательными числами
    a, b = abs(a), abs(b)
    
    # Алгоритм Евклида с использованием цикла while
    while b:  # Пока b не равно 0
        # Одновременное присваивание (особенность Python)
        a, b = b, a % b
    
    return a


def gcd_math_lib(a, b):
    """
    Альтернативный способ с использованием встроенной функции math.gcd().
    Демонстрирует использование стандартной библиотеки.
    """
    return math.gcd(a, b)


def validate_input(user_input):
    """
    Проверка корректности ввода.
    
    Параметры:
        user_input (str): строка для проверки
    
    Возвращает:
        tuple: (bool, int/None) - успешность проверки и преобразованное число
    """
    try:
        num = int(user_input)
        return True, num
    except ValueError:
        return False, None


def main():
    """Основная функция программы."""
    print("=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Тема: Структурное программирование на Python")
    print("Задание: НОД двух чисел")
    print("=" * 50)
    
    # Демонстрация работы с различными типами данных
    program_info = {
        "author": "Студент",
        "group": "ИТ-11",
        "task_number": 4,
        "difficulty": "medium"
    }
    print(f"Информация: {program_info}")
    
    # Цикл для возможности повторного ввода
    while True:
        try:
            # Ввод чисел с проверкой
            print("\n" + "-" * 30)
            input1 = input("Введите первое число: ")
            input2 = input("Введите второе число: ")
            
            # Проверка корректности ввода
            is_valid1, num1 = validate_input(input1)
            is_valid2, num2 = validate_input(input2)
            
            # Использование условного оператора
            if not is_valid1 or not is_valid2:
                print("Ошибка: Пожалуйста, введите целые числа!")
                continue
            
            # Вычисление НОД двумя способами
            result_euclid = gcd_euclid(num1, num2)
            result_math = gcd_math_lib(num1, num2)
            
            # Вывод результатов
            print(f"\nРезультаты для чисел {num1} и {num2}:")
            print(f"  НОД (алгоритм Евклида): {result_euclid}")
            print(f"  НОД (функция math.gcd): {result_math}")
            
            # Проверка совпадения результатов
            if result_euclid == result_math:
                print("  ✓ Результаты совпадают")
            
            # Дополнительная информация
            if result_euclid == 1:
                print("  Числа являются взаимно простыми")
            
            # Проверка на кратность
            if num2 != 0 and num1 % num2 == 0:
                print(f"  {num1} кратно {num2}")
            elif num1 != 0 and num2 % num1 == 0:
                print(f"  {num2} кратно {num1}")
            
            # Вопрос о повторении
            repeat = input("\nХотите продолжить? (д/н): ").strip().lower()
            if repeat not in ['д', 'да', 'y', 'yes']:
                print("\nПрограмма завершена. Спасибо за работу!")
                break
                
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            break


if __name__ == "__main__":
    main()