from random import randint

import prompt  # type: ignore

from brain_games.cli import welcome_user


# Проверка на простое ли число
def prime(number):
    if number <= 1:
        return "no"
    if number <= 3:
        return "yes"
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    
    return 'yes'


def main():
    # Приветствие и выеснение имени пользователя
    name = welcome_user()

    # Правила
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # Счётчик
    n = 0

    # Игра, где нужно ответить 3 раза подряд правильно определить простое число
    while n < 3:
        # Генерация числа и выяснение ответа пользователя
        number = randint(1, 100)
        user_answer = prompt.string(f"Question: {number}\nYour answer: ")

        # Выяснение правильного ответа
        answer = prime(number)

        # Проверка
        if answer == user_answer:
            print('Correct!')
            n += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'.\nLet's try again, {name}!")
            break

    # Победа
    if n == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()