#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа № 2: Структурное программирование на Python
Задание 6 (средней сложности): Калькулятор

Демонстрирует:
- Переменные и типы данных (int, float)
- Условные операторы if/elif/else
- Циклы while
- Функции с параметрами
- Словарь (dict) для хранения операций
- Обработка исключений
- Стиль PEP8
"""

import operator  # Демонстрация использования модуля для операций


class Calculator:
    """
    Класс для демонстрации организации кода.
    Хотя классы не требуются в задании, они показывают другой уровень организации.
    """
    
    # Словарь для хранения доступных операций
    OPERATIONS = {
        '+': {'name': 'сложение', 'func': operator.add},
        '-': {'name': 'вычитание', 'func': operator.sub},
        '*': {'name': 'умножение', 'func': operator.mul},
        '/': {'name': 'деление', 'func': operator.truediv},
        '**': {'name': 'возведение в степень', 'func': operator.pow},
        '%': {'name': 'остаток от деления', 'func': operator.mod},
        '//': {'name': 'целочисленное деление', 'func': operator.floordiv}
    }
    
    def __init__(self):
        """Конструктор класса."""
        self.history = []  # Список для хранения истории операций
        self.operation_count = 0
        
    def calculate(self, num1, num2, operation):
        """
        Выполнение арифметической операции.
        
        Параметры:
            num1 (float): первое число
            num2 (float): второе число
            operation (str): символ операции
            
        Возвращает:
            float/None: результат операции или None при ошибке
        """
        try:
            # Получаем функцию из словаря
            func = self.OPERATIONS[operation]['func']
            
            # Особые случаи для деления
            if operation in ['/', '//', '%'] and num2 == 0:
                print("Ошибка: Деление на ноль!")
                return None
            
            # Выполнение операции
            result = func(num1, num2)
            
            # Сохранение в историю
            self.operation_count += 1
            self.history.append({
                'id': self.operation_count,
                'num1': num1,
                'num2': num2,
                'op': operation,
                'result': result
            })
            
            return result
            
        except Exception as e:
            print(f"Ошибка при вычислении: {e}")
            return None
    
    def show_history(self):
        """Вывод истории операций."""
        if not self.history:
            print("История пуста")
            return
        
        print("\n" + "=" * 50)
        print("ИСТОРИЯ ОПЕРАЦИЙ")
        print("=" * 50)
        
        # Цикл for для вывода истории
        for record in self.history:
            print(f"{record['id']}: {record['num1']} {record['op']} {record['num2']} = {record['result']}")
        
        print(f"Всего операций: {len(self.history)}")


def display_menu():
    """Вывод меню программы."""
    print("\n" + "=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Тема: Структурное программирование на Python")
    print("Задание: Калькулятор")
    print("=" * 50)
    print("\nДОСТУПНЫЕ ОПЕРАЦИИ:")
    
    # Демонстрация работы со словарем и циклом for
    for op, info in Calculator.OPERATIONS.items():
        print(f"  {op:3} - {info['name']}")
    
    print("  q    - выход")
    print("  h    - показать историю")
    print("  help - показать это меню")


def get_number(prompt):
    """
    Функция для ввода числа с проверкой.
    
    Параметры:
        prompt (str): приглашение для ввода
        
    Возвращает:
        float/None: число или None при ошибке
    """
    while True:
        try:
            value = input(prompt)
            
            # Проверка на float или int
            if '.' in value:
                return float(value)
            else:
                return int(value)
                
        except ValueError:
            print("Ошибка: Введите корректное число!")
            continue


def main():
    """Основная функция программы."""
    calculator = Calculator()
    
    display_menu()
    
    # Основной цикл программы
    while True:
        try:
            print("\n" + "-" * 50)
            operation = input("Введите операцию: ").strip().lower()
            
            # Обработка специальных команд
            if operation == 'q':
                print("\nПрограмма завершена. Спасибо за работу!")
                break
            elif operation == 'h':
                calculator.show_history()
                continue
            elif operation == 'help':
                display_menu()
                continue
            
            # Проверка наличия операции
            if operation not in calculator.OPERATIONS:
                print("Ошибка: Неподдерживаемая операция!")
                print("Введите 'help' для списка операций")
                continue
            
            # Ввод чисел
            print(f"\nВыбрана операция: {calculator.OPERATIONS[operation]['name']}")
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")
            
            # Вычисление
            result = calculator.calculate(num1, num2, operation)
            
            # Вывод результата
            if result is not None:
                print(f"\nРЕЗУЛЬТАТ: {num1} {operation} {num2} = {result}")
                
                # Определение типа результата
                if isinstance(result, float):
                    print(f"Тип результата: float")
                else:
                    print(f"Тип результата: {type(result).__name__}")
                
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
            continue


if __name__ == "__main__":
    main()
