# Запуск всех модулей тестов в текузей директории включая подкаталоги
python -m pytest

# Запуск только одного модуля тестов
python -m pytest .\testing\main_test.py

# Запуск только одного теста
python -m pytest .\testing\main_test.py -k 'test_sum2'
# или
python -m pytest .\testing\main_test.py::test_plus2
#Запуск одного теста с тест класса
python -m pytest .\testing\main_class_test.py::TestClass::test_one

# вызов тестов с собственной отметкой - осторожно, предупреждение
python -m pytest -m my_mark

# список фикстур
python -m pytest --fixtures

# остановка после первого упавшего теста
python -m pytest -x

# остановка после первых двух упавших тестов
pytest --maxfail=2
