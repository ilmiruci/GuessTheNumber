import random, answer, text


# TODO: Переписать код в функциональном стиле.
#  - Декомпозировать задачу: Одна функция решает только одну задачу

# TODO: Вывести информацию об игре:
#  - Название игры
#  - В каком диапазоне было загадано число
#  - Кол-во возможных попыток


def game_logic():
    random_num = random.randrange(1, 100)
    attempt_amount = 0  # Число попыток

    print(text.game_name, text.sep, text.rules, text.sep)


    while attempt_amount < 3:
        attempt_amount += 1
        try:
            user_answer = answer.get_user_num()
            # TODO: Что если, пользователь ввел число вне диапазона?
            # Вынес запрос ответа пользователя (с проверкой входного значения) в отдельный модуль

            if user_answer == random_num:
                print(f'Вы угадали, загаданное число: {random_num}, за {attempt_amount} попыток')
                break

            if user_answer > random_num:
                print('Ваше число больше')
            elif user_answer < random_num:
                print('Ваше число меньше')
        except ValueError:
            print("Неправильное значение")

    else:
        # TODO: Вывести информацию какое число было загадано.
        # Вывел
        print(text.sep)
        print("Кол-во попыток исчерпано")
        print(f"Загаданное число {random_num}")


def run():
    game_logic()


if __name__ == '__main__':
    run()
