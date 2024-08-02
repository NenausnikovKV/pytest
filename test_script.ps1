# Запуск всех модулей тестов в текузей директории включая подкаталоги
pytest

# Запуск только одного модуля тестов
pytest .\testing\main_test.py

# Запуск только одного теста
pytest .\testing\main_test.py -k 'test_sum2'
