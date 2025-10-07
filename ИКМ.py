from typing import Union

class Stack:
    """Реализация структуры данных стек."""

    def __init__(self) -> None:
        self.__items: list[Union[int, float]] = []

    def push(self, item: Union[int, float]) -> None:
        """Добавляет элемент в стек."""
        self.__items.append(item)

    def pop(self) -> Union[int, float]:
        """Извлекает и возвращает верхний элемент стека."""
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.__items.pop()

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return len(self.__items) == 0

    def size(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self.__items)


class MathOperations:
    """Класс, содержащий все арифметические операции."""

    def execute(self, operator: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Выполняет арифметическую операцию.

        Аргументы:
            operator: Символ операции ('+', '-', '*', '/')
            a: Первый операнд
            b: Второй операнд

        Возвращает:
            Результат операции

        Выбрасывает:
            ValueError: Если оператор неизвестен
            ZeroDivisionError: При делении на ноль
        """
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            return a / b
        else:
            raise ValueError(f"Неизвестный оператор: {operator}")


class RPNCalculator:
    """Калькулятор обратной польской записи."""

    def __init__(self) -> None:
        self.__stack: Stack = Stack()
        self.__operations: MathOperations = MathOperations()

    def calculate(self, expression: str) -> Union[int, float]:
        """Вычисляет выражение в RPN-формате."""
        if not expression.strip():
            raise ValueError("Пустое выражение")

        for token in expression.split():
            try:
                if token in '+-*/':
                    self._perform_operation(token)
                else:
                    self._process_operand(token)
            except Exception as e:
                raise ValueError(f"Ошибка в токене '{token}': {str(e)}")

        if self.__stack.size() != 1:
            raise ValueError("Некорректное выражение")

        return self.__stack.pop()

    def _process_operand(self, token: str) -> None:
        """Обрабатывает операнд."""
        try:
            num = float(token)
            if num < 0:
                raise ValueError("Числа должны быть положительными")
            self.__stack.push(num)
        except ValueError:
            if any(c.isalpha() for c in token):
                raise ValueError(f"Неизвестный оператор: {token}")
            raise ValueError("Некорректный формат числа")

    def _perform_operation(self, operator: str) -> None:
        """Выполняет операцию."""
        if self.__stack.size() < 2:
            raise ValueError("Недостаточно операндов")

        b = self.__stack.pop()
        a = self.__stack.pop()

        try:
            result = self.__operations.execute(operator, a, b)
            self.__stack.push(result)
        except ZeroDivisionError:
            raise ValueError("Деление на ноль")
        except Exception as e:
            raise ValueError(f"Ошибка операции: {str(e)}")


def display_welcome() -> None:
    """Выводит приветственное сообщение."""
    print("Калькулятор обратной польской записи")
    print("Введите выражение (например: '3 4 +')")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'exit'")


def get_input() -> str:
    """Получает ввод пользователя."""
    return input("\nВведите выражение: ").strip()


def show_result(result: Union[int, float]) -> None:
    """Выводит результат."""
    print(f"Результат: {result:.2f}")


def show_error(message: str) -> None:
    """Выводит сообщение об ошибке."""
    print(f"Ошибка: {message}")


def main() -> None:
    """Точка входа в программу."""
    display_welcome()
    calc = RPNCalculator()

    while True:
        try:
            user_input = get_input()

            if user_input.lower() == 'exit':
                print("Работа завершена")
                break

            try:
                result = calc.calculate(user_input)
                show_result(result)
            except ValueError as e:
                show_error(str(e))

        except KeyboardInterrupt:
            print("\nПрограмма прервана")
            break
        except Exception as e:
            show_error(f"Неизвестная ошибка: {str(e)}")


if __name__ == "__main__":
    main()
