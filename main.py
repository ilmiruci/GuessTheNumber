import random


# TODO: Переписать код в функциональном стиле.
#  - Декомпозировать задачу: Одна функция решает только одну задачу

# TODO: Вывести информацию об игре:
#  - Название игры
#  - В каком диапазоне было загадано число
#  - Кол-во возможных попыток


def game_logic():
    random_num = random.randrange(1, 100)
    attempt_amount = 0  # Число попыток

    while attempt_amount < 3:
        attempt_amount += 1
        try:
            user_answer = int(input("Введите число: "))
            # TODO: Что если, пользователь ввел число вне диапазона?

            if user_answer == random_num:
                print(f'Вы угадали, загаданное число: {random_num}, за {attempt_amount} попыток')
                break

            if user_answer > random_num:
                print('Ваше число больше')
            elif user_answer < random_num:
                print('Ваше число меньше')
        except ValueError:
            print("Недопустимое значение")

    else:
        # TODO: Вывести информацию какое число было загадано.
        print("Кол-во попыток исчерпано")


def run():
    game_logic()


if __name__ == '__main__':
    run()
