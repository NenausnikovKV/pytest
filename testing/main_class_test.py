"""
Тестовые классы
"""


class TestClass:
    """
    Тестовый класс
    """
    def test_one(self):
        """ Тест внутри """
        word = "this"
        assert "h" in word

    def test_two(self):
        """Второй тест"""
        word = "hello"
        assert "h" in word


class TestClassVariable:
    """
    Тестовый класс - проверка переменной класса
    """
    word = "this"
    def test_one(self):
        """ Тест после проверки переназначил строку класса"""
        assert "h" in self.word
        self.word = "not needed letter"

    def test_two(self):
        """
        Тест. Ошибки не будет несмотря на переназначение self.word в предыдущем методе
        Переменная класса для каждого теста класса инициализируется.
        """
        assert "h" in self.word
