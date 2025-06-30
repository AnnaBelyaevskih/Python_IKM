class Stack:
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


class AddOperation:
    """Класс, реализующий операцию сложения"""

    def execute(self, first_operand: float, second_operand: float) -> float:
        """
        Выполняет сложение двух чисел.

        Ards:
            first_operand: Первое слагаемое.
            second_operand: Второе слагаемое.
        Return:
            Сумма.
        """
        return first_operand + second_operand


class SubtractOperation:
    """Класс, реализующий операцию вычитания"""

    def execute(self, first_operand: float, second_operand: float) -> float:
        """
        Выполняет вычитание второго числа из первого.

        Args:
            first_operand: Уменьшаемое.
            second_operand: Вычитаемое.
        Return:
            Разность.
        """
        return first_operand - second_operand


class MultiplyOperation:
    """Класс, реализующий умножение"""

    def execute(self, first_operand: float, second_operand: float) -> float:
        """
        Выполняет умножение двух чисел.

        Args:
            first_operand: Первый множитель.
            second_operand: Второй множитель.
        Return:
            Произведение.
        """
        return first_operand * second_operand


class DivideOperation:
    """Класс, реализующий операцию деления"""

    def execute(self, first_operand: float, second_operand: float) -> float:
        """
        Делит первое число на второе.

        Args:
            first_operand: Делимое.
            second_operand: Делитель.
        Return:
            Частное.
        """
        if second_operand == 0:
            raise ZeroDivisionError("Деление на ноль")
        return first_operand / second_operand


class OperationFactory:
    """
    Класс, реализующий операции возвращающие объект соответствующей арифметической операции.
    """

    def create_operation(self, operator_symbol: str):
        """
        Возвращает экземпляр соответствующей операции по символу.

        Args:
            operator_symbol: Символ операции ('+', '-', '*', '/').
        Return:
            Объект операции.
        """
        operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation()
        }
        if operator_symbol not in operations:
            raise ValueError(f"Неизвестный оператор: {operator_symbol}")
        return operations[operator_symbol]


class RPNCalculator:
    """
    Класс, реализующий калькулятор обратной польской записи (постфиксной записи).
    """

    def __init__(self):
        """
        Инициализирует стек и фабрику операций.
        """
        self.__stack = Stack()
        self.__operation_factory = OperationFactory()

    def calculate(self, expression: str) -> float:
        """
        Вычисляет значение выражения в обратной польской записи.

        Args:
            expression: Строка с выражением (например: '3 4 +').
        Return:
            Результат вычисления.
        """
        if not expression.strip():
            raise ValueError("Пустое выражение")

        tokens = expression.split()

        for token in tokens:
            try:
                if token in '+-*/':
                    self.__perform_operation(token)
                else:
                    self.__process_operand(token)
            except Exception as error:
                raise ValueError(f"Ошибка в токене '{token}': {str(error)}")

        if self.__stack.size() != 1:
            raise ValueError("Некорректное выражение: в стеке должно остаться одно значение")

        return self.__stack.pop()

    def __process_operand(self, token: str) -> None:
        """
        Обрабатывает операнд: преобразует в число и помещает в стек.

        Args:
            token: Токен операнда.
        """
        try:
            number = float(token)
            if number < 0.0:
                raise ValueError("Числа должны быть положительными")
            self.__stack.push(number)
        except ValueError:
            if any(char.isalpha() for char in token):
                raise ValueError(f"Неизвестный оператор: {token}")
            raise ValueError("Некорректный формат числа")

    def __perform_operation(self, operator_symbol: str) -> None:
        """
        Выполняет арифметическую операцию на двух верхних элементах стека.

        Args:
            operator_symbol: Символ операции.
        """
        if self.__stack.size() < 2:
            raise ValueError("Недостаточно операндов для выполнения операции")

        try:
            second_operand = self.__stack.pop()
            first_operand = self.__stack.pop()
            operation = self.__operation_factory.create_operation(operator_symbol)
            result = operation.execute(first_operand, second_operand)
            self.__stack.push(result)
        except ZeroDivisionError:
            raise ValueError("Ошибка: деление на ноль")
        except Exception as error:
            raise ValueError(f"Ошибка при выполнении операции: {str(error)}")


def display_welcome_message() -> None:
    """
    Выводит приветственное сообщение и инструкцию по использованию калькулятора.
    """
    print("Калькулятор обратной польской записи")
    print("Введите выражение, например: '3.5 4 +'")
    print("Числа должны быть положительными (>= 0)")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'break'")


def get_user_input() -> str:
    """
    Получает строку ввода от пользователя.

    Return:
        Строка с выражением.
    """
    return input("\nВведите выражение: ").strip()


def display_result(result: float) -> None:
    """Выводит результат вычисления."""
    print(f"Результат: {result:.2f}")


def display_error(message: str) -> None:
    """Выводит сообщение об ошибке."""
    print(f"Ошибка: {message}")


def main() -> None:
    """
    Основной цикл программы. Обрабатывает пользовательский ввод и вычисляет выражения.
    """
    display_welcome_message()
    calculator = RPNCalculator()

    while True:
        try:
            user_input = get_user_input()

            if user_input.lower() == 'break':
                print("Завершение работы...")
                break

            try:
                result = calculator.calculate(user_input)
                display_result(result)
            except ValueError as error:
                display_error(str(error))

        except KeyboardInterrupt:
            print("\nРабота прервана пользователем")
            break
        except Exception as error:
            display_error(f"Неизвестная ошибка: {str(error)}")


if __name__ == "__main__":
    main()
