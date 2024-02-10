from models.calc import Calc


def main() -> None:
    pts: int = 0
    play(pts)


def play(pts: int) -> None:
    level: int = int(input('Informe a dificuldade desejada [1, 2, 3 ou 4]: '))

    calc: Calc = Calc(level)
    print('Informe o resultado para a seguinte operação: ')
    calc.show_op()

    result: int = int(input())

    if calc.check_result(result):
        pts += 1
        print(f'Você tem {pts} Ponto(s).')

    cont: int = int(input('Deseja continuar no jogo? [1 = sim, 0 = sair]: '))
    if cont:
        play(level)
    else:
        print(f'Fim de jogo! Ponto(s): {pts}')


if __name__ == '__main__':
    main()
