from random import randint

import prompt  # type: ignore

from brain_games.cli import welcome_user


def main():
    # Приветствие и выеснение имени пользователя
    name = welcome_user()

    # Правила
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Счётчик
    n = 0

    # Игра, где нужно ответить 3 раза подряд правильно определить чётность
    while n < 3:
        # Генерация числа и выяснение ответа пользователя
        number = randint(1, 100)
        user_answer = prompt.string(f"Question: {number}\nYour answer: ")
    
        # Определение чётности
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

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
