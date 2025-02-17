import random
try:
    random_num = random.randrange(1,100)
    user_answer = int(input("Введите число: "))
    attempt_amount = 1 # Число попыток

    while attempt_amount <= 10:
        if user_answer == random_num:
            print(f'Вы угадали, загаданное число: {random_num}, за {attempt_amount} попыток')
            break
        elif user_answer > random_num:
            print('Ваше число больше')
            attempt_amount += 1
            user_answer = int(input("Напишите число: "))
        elif user_answer < random_num:
            print('Ваше число меньше')
            attempt_amount += 1
            user_answer = int(input("Напишите число: "))
        else:
            print("Кол-во попыток исчерпано")
except ValueError:
    print("Недопустимое значение")



