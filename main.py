"""
Модуль для демонстрации работы с исключениями в Python:
1. Создание пользовательских исключений
2. Обработка нескольких типов исключений
3. Использование блока finally для гарантированного освобождения ресурсов
"""

import os


class InvalidInputError(Exception):
    """
    Пользовательское исключение для невалидных входных данных.
    Наследуется от базового класса Exception.
    """
    def __init__(self, message="Входные данные не соответствуют критериям"):
        self.message = message
        super().__init__(self.message)


def validate_input(value, min_value, max_value):
    """
    Проверяет, что значение находится в заданном диапазоне.
    
    Аргументы:
        value: Проверяемое значение (int или float)
        min_value: Минимальное допустимое значение
        max_value: Максимальное допустимое значение
    
    Исключения:
        InvalidInputError: Если значение вне диапазона или не является числом
    
    Пример использования:
        validate_input(15, 10, 20)  # Валидные данные
        validate_input(5, 10, 20)   # Вызовет InvalidInputError
    """
    if not isinstance(value, (int, float)):
        raise InvalidInputError("Входные данные должны быть числом")
    
    if not min_value <= value <= max_value:
        raise InvalidInputError(
            f"Значение {value} должно быть между {min_value} и {max_value}"
        )
    
    print(f"✓ Входные данные {value} валидны")


def process_file(file_path):
    """
    Обрабатывает файл, демонстрируя обработку различных исключений.
    Реализует обработку FileNotFoundError, PermissionError и ValueError.
    
    Аргументы:
        file_path: Путь к файлу для обработки
    
    Исключения:
        FileNotFoundError: Если файл не существует
        PermissionError: Если нет прав на чтение файла
        ValueError: Если файл пустой
    
    Пример использования:
        process_file("existing_file.txt")  # Успешная обработка
        process_file("nonexistent.txt")    # FileNotFoundError
    """
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден")
        
        # Проверка прав на чтение
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Нет прав на чтение файла {file_path}")
        
        # Чтение файла
        with open(file_path, 'r') as file:
            content = file.read()
            
            if not content:
                raise ValueError("Файл пустой")
            
            print(f"Содержимое файла (первые 100 символов): {content[:100]}...")
            
    except FileNotFoundError as fnf_error:
        print(f"⛔ Ошибка: {fnf_error}")
    except PermissionError as perm_error:
        print(f"⛔ Ошибка прав доступа: {perm_error}")
    except ValueError as val_error:
        print(f"⛔ Ошибка значения: {val_error}")
    except Exception as e:
        print(f"⛔ Неожиданная ошибка: {e}")
    else:
        print("✓ Файл успешно обработан")


def read_file_with_finally(file_path):
    """
    Читает файл с гарантированным закрытием в блоке finally.
    Демонстрирует правильное управление ресурсами.
    
    Аргументы:
        file_path: Путь к файлу для чтения
    
    Пример использования:
        read_file_with_finally("example.txt")      # Успешное чтение
        read_file_with_finally("nonexistent.txt") # Обработка ошибки
    """
    file = None
    try:
        file = open(file_path, 'r')
        content = file.read()
        print(f"Содержимое файла ({len(content)} символов):")
        print(content[:50] + "...")  # Печатаем первые 50 символов
    except FileNotFoundError:
        print(f"⛔ Файл {file_path} не найден")
    except IOError as e:
        print(f"⛔ Ошибка ввода/вывода: {e}")
    finally:
        if file is not None:
            file.close()
            print("✓ Файл закрыт в блоке finally")


def demonstrate_exceptions():
    """
    Демонстрационная функция, показывающая работу всех реализованных методов.
    """
    print("\n=== Демонстрация пользовательского исключения ===")
    try:
        validate_input(15, 10, 20)  # Валидные данные
        validate_input("текст", 10, 20)  # Нечисловые данные
    except InvalidInputError as e:
        print(f"⛔ Поймано пользовательское исключение: {e}")

    print("\n=== Демонстрация обработки нескольких исключений ===")
    process_file("example.txt")      # Предполагается, что файл существует
    process_file("nonexistent.txt")  # Файл не существует

    print("\n=== Демонстрация блока finally ===")
    read_file_with_finally("example.txt")
    read_file_with_finally("nonexistent.txt")


if __name__ == "__main__":
    demonstrate_exceptions()
