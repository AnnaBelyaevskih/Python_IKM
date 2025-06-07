Беляевских Анна ИТ-9, вариант-15
class Stack:
    """Реализация структуры данных стек."""

    def __init__(self):
        self.__items = []

    def push(self, item):
        """Добавление элемента в стек."""
        self.__items.append(item)

    def pop(self):
        """Извлечение элемента из стека."""
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.__items.pop()

    def is_empty(self):
        """Проверка стека на пустоту."""
        return len(self.__items) == 0

    def size(self):
        """Получение количества элементов в стеке."""
        return len(self.__items)


class AddOperation:
    """Операция сложения."""

    def execute(self, first_operand, second_operand):
        """Выполнение операции сложения."""
        return first_operand + second_operand


class SubtractOperation:
    """Операция вычитания."""

    def execute(self, first_operand, second_operand):
        """Выполнение операции вычитания."""
        return first_operand - second_operand


class MultiplyOperation:
    """Операция умножения."""

    def execute(self, first_operand, second_operand):
        """Выполнение операции умножения."""
        return first_operand * second_operand


class DivideOperation:
    """Операция деления."""

    def execute(self, first_operand, second_operand):
        """Выполнение операции деления."""
        if second_operand == 0:
            raise ZeroDivisionError("Деление на ноль")
        return first_operand / second_operand


class OperationFactory:
    """Создание операций по символу."""

    def create_operation(self, operator_symbol):
        """Создание объекта операции по символу."""
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
    """Калькулятор обратной польской записи."""

    def __init__(self):
        self.__stack = Stack()
        self.__operation_factory = OperationFactory()

    def calculate(self, expression):
        """Вычисление выражения в обратной польской записи."""
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
            raise ValueError("Некорректное выражение: после вычислений в стеке должно остаться ровно одно значение")

        return self.__stack.pop()

    def __process_operand(self, token):
        """Обработка операнда с поддержкой вещественных положительных чисел."""
        try:
            number = float(token)
            if number < 0.0:
                raise ValueError("Числа должны быть положительными")
            self.__stack.push(number)
        except ValueError:
            if any(char.isalpha() for char in token):
                raise ValueError(f"Неизвестный оператор: {token}")
            raise ValueError("Некорректный формат числа")

    def __perform_operation(self, operator_symbol):
        """Выполнение арифметической операции."""
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


def display_welcome_message():
    """Отображение приветственного сообщения."""
    print("Калькулятор обратной польской записи")
    print("Введите выражение, например: '3.5 4 +'")
    print("Числа должны быть положительными (> 0)")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'break'")


def get_user_input():
    """Получение ввода от пользователя."""
    return input("\nВведите выражение: ").strip()


def display_result(result):
    """Отображение результата вычислений."""
    print(f"Результат: {result:.2f}")


def display_error(message):
    """Отображение сообщения об ошибке."""
    print(f"Ошибка: {message}")


def main():
    """Основная функция программы."""
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
