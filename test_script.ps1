# Запуск всех модулей тестов в текузей директории включая подкаталоги
python -m pytest

# Запуск только одного модуля тестов
python -m pytest .\testing\main_test.py

# Запуск только одного теста
python -m pytest .\testing\main_test.py -k 'test_sum2'
# или
python -m pytest .\testing\main_test.py::test_plus2
#Запуск одного теста с тест класса
#pytest test_mod.py::TestClass::test_method

# вызов тестов с собственной отметкой - осторожно, предупреждение
python -m pytest -m my_mark
