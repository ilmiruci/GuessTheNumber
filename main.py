import random

import answer, text


def run_game_logic() -> None:
    guess_num: int = random.randrange(1, 100)
    print(text.game_name, text.sep, text.rules, text.sep)

    attempt_amount: int = 0
    while attempt_amount < 3:
        attempt_amount += 1

        try:  # пробовать
            user_answer = answer.get_user_num()
            answer.validate_num(user_answer)
        except ValueError as err_msg:  # поймать
            print(err_msg)
        else:  # тогда
            if user_answer == guess_num:
                print(text.winner_msg.format(guess_num, attempt_amount))
                break
            print(answer.get_hint(user_answer, guess_num))

        finally:  # завершение
            pass

    else:
        print(text.sep)
        print("Кол-во попыток исчерпано")
        print(f"Загаданное число {guess_num}")


if __name__ == "__main__":
    run_game_logic()
