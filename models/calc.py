from random import randint


class Calc:
    def __init__(self: object, level: int, /) -> None:
        self.__level: int = level
        self.__v1: int = self._create_value
        self.__v2: int = self._create_value
        self.__operation: int = randint(1, 3)
        self.__result: float = self._create_result

    @property
    def level(self: object) -> int:
        return self.__level

    @property
    def v1(self: object) -> int:
        return self.__v1

    @property
    def v2(self: object) -> int:
        return self.__v2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Somar'
        elif self.operation == 2:
            op = 'Diminuir'
        elif self.operation == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.v1} \nValor 2: {self.v2} \nDificuldade: {self.level}\nOperação: {op}'

    @property
    def _create_value(self: object) -> int:
        if self.level == 1:
            return randint(0, 10)
        elif self.level == 2:
            return randint(0, 100)
        elif self.level == 3:
            return randint(0, 1000)
        elif self.level == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000000)

    @property
    def _create_result(self: object) -> int:
        if self.operation == 1:
            return self.v1 + self.v2
        elif self.operation == 2:
            return self.v1 - self.v2
        elif self.operation == 3:
            return self.v1 * self.v2

    @property
    def _op_symbol(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def check_result(self: object, anw: int) -> bool:
        check: bool = False

        if self.result == anw:
            print('Resposta Correta!')
            check = True
        else:
            print('Resposta Errada!')
        print(f'{self.v1} {self._op_symbol} {self.v2} = {self.result}')

        return check

    def show_op(self: object) -> None:
        print(f'{self.v1} {self._op_symbol} {self.v2} = ?')
