#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа № 2: Структурное программирование на Python
Задание 10 (средней сложности): Словарь квадратов чисел

Демонстрирует:
- Переменные и типы данных (int, dict)
- Генераторы словарей
- Циклы for
- Функции с параметрами
- Условные операторы
- Работа со словарями
- Стиль PEP8
- Модуль random для демонстрации
"""

import random  # Для демонстрации дополнительных возможностей


def create_squares_dict(n):
    """
    Создание словаря квадратов чисел от 1 до n.
    Использует генератор словаря (dictionary comprehension).
    
    Параметры:
        n (int): верхняя граница диапазона
        
    Возвращает:
        dict: словарь {число: квадрат}
    """
    # Генератор словаря - элегантный способ создания словарей
    return {i: i ** 2 for i in range(1, n + 1)}


def create_custom_dict(start, end, power=2):
    """
    Создание словаря с настраиваемой степенью.
    
    Параметры:
        start (int): начало диапазона
        end (int): конец диапазона
        power (int): степень для возведения
        
    Возвращает:
        dict: словарь {число: число**power}
    """
    result = {}
    # Цикл for с range
    for i in range(start, end + 1):
        result[i] = i ** power
    return result


def analyze_dict(data_dict):
    """
    Анализ словаря: поиск минимума, максимума, среднего.
    
    Параметры:
        data_dict (dict): словарь для анализа
        
    Возвращает:
        dict: результаты анализа
    """
    if not data_dict:
        return {}
    
    # Получение всех значений
    values = list(data_dict.values())
    
    # Использование встроенных функций
    analysis = {
        'min_key': min(data_dict.keys()),
        'max_key': max(data_dict.keys()),
        'min_value': min(values),
        'max_value': max(values),
        'sum_values': sum(values),
        'avg_value': sum(values) / len(values),
        'count': len(data_dict)
    }
    
    return analysis


def demonstrate_dict_methods(squares_dict):
    """
    Демонстрация основных методов работы со словарями.
    
    Параметры:
        squares_dict (dict): словарь для демонстрации
    """
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ МЕТОДОВ РАБОТЫ СО СЛОВАРЯМИ")
    print("=" * 50)
    
    # 1. Получение ключей, значений и элементов
    print("\n1. Ключи словаря:")
    keys = list(squares_dict.keys())
    print(f"   {keys[:5]} ..." if len(keys) > 5 else f"   {keys}")
    
    print("\n2. Значения словаря:")
    values = list(squares_dict.values())
    print(f"   {values[:5]} ..." if len(values) > 5 else f"   {values}")
    
    print("\n3. Элементы словаря (ключ-значение):")
    items = list(squares_dict.items())
    print(f"   {items[:3]} ..." if len(items) > 3 else f"   {items}")
    
    # 4. Проверка наличия ключа
    test_key = random.randint(1, len(squares_dict))
    if test_key in squares_dict:
        print(f"\n4. Проверка наличия ключа {test_key}: есть")
        print(f"   Квадрат {test_key} = {squares_dict[test_key]}")
    
    # 5. Использование get с значением по умолчанию
    missing_key = len(squares_dict) + 1
    value = squares_dict.get(missing_key, "не найдено")
    print(f"\n5. Метод get для ключа {missing_key}: {value}")
    
    # 6. Обновление словаря
    new_dict = {0: 0, -1: 1}
    squares_dict.update(new_dict)
    print(f"\n6. После обновления словаря (добавлены ключи 0 и -1):")
    print(f"   Теперь есть ключи: {sorted(squares_dict.keys())[:7]}")


def main():
    """Основная функция программы."""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Тема: Структурное программирование на Python")
    print("Задание: Словарь квадратов чисел")
    print("=" * 60)
    
    # Демонстрация работы с различными типами данных
    program_info = {
        "student": "Иванов И.И.",
        "group": "ИТ-11",
        "date": "2024",
        "completed": True
    }
    
    print(f"\nИнформация о программе:")
    for key, value in program_info.items():
        print(f"  {key}: {value}")
    
    # Основной блок
    try:
        # Ввод числа
        n_input = input("\nВведите количество чисел N (или 'demo' для демонстрации): ")
        
        if n_input.lower() == 'demo':
            # Демонстрационный режим
            print("\nДЕМОНСТРАЦИОННЫЙ РЕЖИМ")
            test_values = [5, 10, 3]
            
            for n in test_values:
                print(f"\n--- Для N = {n} ---")
                squares = create_squares_dict(n)
                
                # Вывод в две колонки
                print("Число | Квадрат")
                print("-" * 15)
                for num, square in squares.items():
                    print(f"{num:5} | {square:7}")
                
                # Анализ словаря
                analysis = analyze_dict(squares)
                print(f"\nАнализ: максимум = {analysis['max_value']}, "
                      f"минимум = {analysis['min_value']}")
            
            # Демонстрация дополнительных возможностей
            squares = create_squares_dict(10)
            demonstrate_dict_methods(squares)
            
        else:
            # Обычный режим работы
            n = int(n_input)
            
            if n <= 0:
                print("Ошибка: N должно быть положительным числом!")
                return
            
            # Создание словаря
            squares_dict = create_squares_dict(n)
            
            # Вывод результатов
            print(f"\nСловарь квадратов чисел от 1 до {n}:")
            print("-" * 30)
            
            # Цикл for с enumerate для демонстрации
            for i, (num, square) in enumerate(squares_dict.items(), 1):
                print(f"{num:3} → {square:6}", end="  ")
                if i % 5 == 0:  # Каждые 5 чисел перенос строки
                    print()
            
            print("\n" + "-" * 30)
            
            # Анализ словаря
            analysis = analyze_dict(squares_dict)
            print(f"\nАНАЛИЗ СЛОВАРЯ:")
            print(f"  Количество элементов: {analysis['count']}")
            print(f"  Минимальное значение: {analysis['min_value']} (для числа {analysis['min_key']})")
            print(f"  Максимальное значение: {analysis['max_value']} (для числа {analysis['max_key']})")
            print(f"  Сумма квадратов: {analysis['sum_values']}")
            print(f"  Среднее значение: {analysis['avg_value']:.2f}")
            
            # Демонстрация случайного доступа
            random_key = random.randint(1, n)
            print(f"\nСлучайный доступ: квадрат числа {random_key} = {squares_dict[random_key]}")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число!")
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
