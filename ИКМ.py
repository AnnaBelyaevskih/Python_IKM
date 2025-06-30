    """
    Класс, реализующий структуру данных стек.
    """

    def __init__(self):
        """
        Инициализация пустого стека.
        """
        self.__items = []

    def push(self, item: float) -> None:
        """
        Добавление элемента в стек.

        Args:
            item: Элемент, добавляемый в стек.
        """
        self.__items.append(item)

    def pop(self) -> float:
        """
        Удаление и возврат верхнего элемента стека.

        Return:
            Верхний элемент стека.
        """
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.__items.pop()

    def is_empty(self) -> bool:
        """
        Проверка, пуст ли стек.

        Return:
            True, если стек пуст, иначе False.
        """
        return len(self.__items) == 0

    def size(self) -> int:
        """
        Возвращает количество элементов в стеке.

        Return:
            Количество элементов.
        """
        return len(self.__items)
