from random import randint

import prompt  # type: ignore

from brain_games.cli import welcome_user


def main():
    # Приветствие и выеснение имени пользователя
    name = welcome_user()

    # Правила
    print('What number is missing in the progression?')

    # Счётчик
    n = 0

    # Игра, где нужно ответить 3 раза подряд правильно
    # заполнить пропуск в последовательности цисел
    while n < 3:
        # Генерация последовательности и выяснение ответа пользователя
        number = randint(1, 100)
        step = randint(1, 10)
        # Номер удалённого числа
        del_number = randint(1, 9)
        progression = list(range(number, number + step * 10, step))
        # Запоминание правльного ответа
        answer = progression[del_number]
        progression[del_number] = ".."
        user_answer = prompt.string(f"Question: {progression}"
                                    f"\nYour answer: ")   

        # Проверка
        if str(answer) == user_answer:
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