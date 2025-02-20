def get_user_num() -> int:
    return int(input("Введите число: "))


def validate_num(num: int,
                 min_value: int = 1,
                 max_value: int = 100) -> int:
    if not (min_value <= num <= max_value):
        raise ValueError("Число должно быть в "
                         f"диапазоне от {min_value} до {max_value}")

    return num


def get_hint(num: int, guess_num: int) -> str:
    """
    Возвращает информацию о том, число пользователя
    больше или меньше загаданного числа.

    :param num: Число пользователя.
    :param guess_num: Загаданное число.
    :return: Подсказка.
    """
    if num > guess_num:
        return "Ваше число больше"
    elif num < guess_num:
        return "Ваше число меньше"
