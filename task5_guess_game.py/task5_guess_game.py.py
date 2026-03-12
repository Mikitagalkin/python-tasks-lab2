#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа № 2: Структурное программирование на Python
Задание 5 (повышенной сложности): Игра «Угадай число»

Демонстрирует:
- Переменные и типы данных (int, str, bool, list, dict)
- Условные операторы if/elif/else
- Циклы while, for
- Функции с параметрами и return
- Модуль random
- Обработка исключений
- Работа со списками и словарями
- Стиль PEP8
"""

import random  # Для генерации случайных чисел
import time    # Для создания задержек
import sys     # Для работы с системными функциями


class GuessGame:
    """
    Класс для организации игры "Угадай число".
    Демонстрирует организацию кода с использованием ООП.
    """
    
    # Константы уровней сложности (словарь)
    DIFFICULTY_LEVELS = {
        '1': {
            'name': 'Легкий',
            'max_num': 50,
            'attempts': 10,
            'hints': True,
            'description': '1-50, 10 попыток, с подсказками'
        },
        '2': {
            'name': 'Средний',
            'max_num': 100,
            'attempts': 7,
            'hints': True,
            'description': '1-100, 7 попыток, с подсказками'
        },
        '3': {
            'name': 'Сложный',
            'max_num': 200,
            'attempts': 5,
            'hints': False,
            'description': '1-200, 5 попыток, без подсказок'
        },
        '4': {
            'name': 'Эксперт',
            'max_num': 500,
            'attempts': 3,
            'hints': False,
            'description': '1-500, 3 попытки, без подсказок'
        }
    }
    
    def __init__(self, player_name="Игрок"):
        """
        Инициализация игры.
        
        Параметры:
            player_name (str): имя игрока
        """
        self.player_name = player_name
        self.games_played = 0
        self.games_won = 0
        self.total_attempts = 0
        self.best_score = float('inf')
        self.history = []  # Список для истории игр
        
    def generate_number(self, max_num):
        """
        Генерация случайного числа.
        
        Параметры:
            max_num (int): максимальное значение
            
        Возвращает:
            int: случайное число от 1 до max_num
        """
        return random.randint(1, max_num)
    
    def play_round(self, level_key):
        """
        Один раунд игры.
        
        Параметры:
            level_key (str): ключ уровня сложности
            
        Возвращает:
            bool: True если игрок выиграл, False если проиграл
        """
        # Получение параметров уровня
        level = self.DIFFICULTY_LEVELS[level_key]
        
        print(f"\n{'=' * 50}")
        print(f"УРОВЕНЬ: {level['name']}")
        print(f"Описание: {level['description']}")
        print(f"{'=' * 50}")
        
        # Генерация числа
        secret = self.generate_number(level['max_num'])
        attempts_left = level['attempts']
        attempts_used = 0
        
        # Список для хранения предположений
        guesses = []
        
        print(f"\nЯ загадал число от 1 до {level['max_num']}")
        print(f"У вас {attempts_left} попыток")
        
        if level['hints']:
            print("Подсказки: я буду говорить 'больше' или 'меньше'")
        else:
            print("Подсказок не будет! Я буду говорить только 'угадал/не угадал'")
        
        # Игровой цикл
        while attempts_left > 0:
            try:
                print(f"\nОсталось попыток: {attempts_left}")
                
                # Ввод числа с проверкой
                guess_input = input(f"Попытка #{attempts_used + 1}: ")
                
                # Проверка на специальные команды
                if guess_input.lower() == 'exit':
                    print("Игра прервана")
                    return False
                
                guess = int(guess_input)
                
                # Проверка диапазона
                if guess < 1 or guess > level['max_num']:
                    print(f"Число должно быть от 1 до {level['max_num']}!")
                    continue
                
                # Сохраняем предположение
                guesses.append(guess)
                attempts_left -= 1
                attempts_used += 1
                
                # Проверка результата
                if guess == secret:
                    print(f"\n{'=' * 50}")
                    print(f"ПОЗДРАВЛЯЮ! Вы угадали число {secret}!")
                    print(f"Использовано попыток: {attempts_used}")
                    
                    # Сохраняем результат
                    self.games_played += 1
                    self.games_won += 1
                    self.total_attempts += attempts_used
                    
                    if attempts_used < self.best_score:
                        self.best_score = attempts_used
                        print("🎉 Новый рекорд!")
                    
                    # Сохраняем в историю
                    self.history.append({
                        'level': level['name'],
                        'secret': secret,
                        'attempts': attempts_used,
                        'result': 'win',
                        'guesses': guesses.copy()
                    })
                    
                    return True
                    
                else:
                    # Подсказки в зависимости от уровня
                    if level['hints']:
                        if guess < secret:
                            print("👉 Загаданное число БОЛЬШЕ")
                        else:
                            print("👉 Загаданное число МЕНЬШЕ")
                        
                        # Дополнительная подсказка: холодно/горячо
                        if attempts_used > 1:
                            diff_current = abs(guess - secret)
                            diff_previous = abs(guesses[-2] - secret)
                            
                            if diff_current < diff_previous:
                                print("🔥 Теплее")
                            elif diff_current > diff_previous:
                                print("❄️ Холоднее")
                    else:
                        print("Не угадали")
                        
            except ValueError:
                print("Ошибка: Введите целое число!")
            except KeyboardInterrupt:
                print("\nИгра прервана")
                return False
        
        # Если попытки закончились
        print(f"\n{'=' * 50}")
        print(f"К сожалению, попытки закончились!")
        print(f"Было загадано число: {secret}")
        print(f"Ваши попытки: {guesses}")
        
        # Сохраняем в историю
        self.games_played += 1
        self.history.append({
            'level': level['name'],
            'secret': secret,
            'attempts': attempts_used,
            'result': 'loss',
            'guesses': guesses.copy()
        })
        
        return False
    
    def show_stats(self):
        """Вывод статистики игрока."""
        print(f"\n{'=' * 50}")
        print(f"СТАТИСТИКА ИГРОКА: {self.player_name}")
        print(f"{'=' * 50}")
        
        if self.games_played == 0:
            print("Статистика пуста")
            return
        
        win_rate = (self.games_won / self.games_played) * 100
        
        print(f"Всего игр: {self.games_played}")
        print(f"Побед: {self.games_won}")
        print(f"Поражений: {self.games_played - self.games_won}")
        print(f"Процент побед: {win_rate:.1f}%")
        
        if self.games_won > 0:
            avg_attempts = self.total_attempts / self.games_won
            print(f"Среднее число попыток: {avg_attempts:.1f}")
            print(f"Лучший результат: {self.best_score} попыток")
    
    def show_history(self):
        """Вывод истории игр."""
        if not self.history:
            print("\nИстория игр пуста")
            return
        
        print(f"\n{'=' * 50}")
        print(f"ИСТОРИЯ ИГР")
        print(f"{'=' * 50}")
        
        for i, game in enumerate(self.history, 1):
            result_symbol = "✅" if game['result'] == 'win' else "❌"
            print(f"{i:2}. {result_symbol} {game['level']}: "
                  f"число {game['secret']}, "
                  f"попыток {game['attempts']}")


def display_menu():
    """Вывод главного меню."""
    print("\n" + "=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Тема: Структурное программирование на Python")
    print("Задание: Игра 'Угадай число'")
    print("=" * 50)
    
    print("\nГЛАВНОЕ МЕНЮ:")
    print("1. Начать новую игру")
    print("2. Выбрать уровень сложности")
    print("3. Показать статистику")
    print("4. Показать историю игр")
    print("5. Сменить имя игрока")
    print("6. Правила игры")
    print("0. Выход")


def show_rules():
    """Вывод правил игры."""
    print("\n" + "=" * 50)
    print("ПРАВИЛА ИГРЫ")
    print("=" * 50)
    print("""
1. Компьютер загадывает случайное число в заданном диапазоне
2. Игрок должен угадать это число за ограниченное число попыток
3. После каждого ввода компьютер дает подсказку:
   - 'больше' - загаданное число больше введенного
   - 'меньше' - загаданное число меньше введенного
4. На сложных уровнях подсказки отключаются
5. Можно завершить игру в любой момент, введя 'exit'

УРОВНИ СЛОЖНОСТИ:""")
    
    for key, level in GuessGame.DIFFICULTY_LEVELS.items():
        print(f"  {key}. {level['name']}: {level['description']}")
    
    print("=" * 50)


def main():
    """Основная функция программы."""
    # Приветствие
    print("=" * 60)
    print("Добро пожаловать в игру 'Угадай число'!")
    print("=" * 60)
    
    # Ввод имени игрока
    player_name = input("Введите ваше имя: ").strip()
    if not player_name:
        player_name = "Игрок"
    
    # Создание объекта игры
    game = GuessGame(player_name)
    
    # Основной цикл программы
    while True:
        try:
            display_menu()
            choice = input("\nВаш выбор: ").strip()
            
            if choice == '0':
                print(f"\nСпасибо за игру, {player_name}!")
                game.show_stats()
                print("\nДо свидания!")
                break
                
            elif choice == '1':
                # Быстрая игра (средний уровень по умолчанию)
                game.play_round('2')
                
            elif choice == '2':
                # Выбор уровня сложности
                print("\nДОСТУПНЫЕ УРОВНИ:")
                for key, level in game.DIFFICULTY_LEVELS.items():
                    print(f"{key}. {level['name']} - {level['description']}")
                
                level_choice = input("\nВыберите уровень (1-4): ").strip()
                
                if level_choice in game.DIFFICULTY_LEVELS:
                    game.play_round(level_choice)
                else:
                    print("Неверный выбор уровня!")
                    
            elif choice == '3':
                game.show_stats()
                
            elif choice == '4':
                game.show_history()
                
            elif choice == '5':
                new_name = input("Введите новое имя: ").strip()
                if new_name:
                    game.player_name = new_name
                    print(f"Имя изменено на {new_name}")
                    
            elif choice == '6':
                show_rules()
                
            else:
                print("Неверный выбор! Пожалуйста, выберите пункт из меню.")
                
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена досрочно")
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            continue


if __name__ == "__main__":
    main()
