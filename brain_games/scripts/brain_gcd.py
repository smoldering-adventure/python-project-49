from random import randint
import prompt  # type: ignore
from brain_games.cli import welcome_user

def main():
    # Приветствие и выеснение имени пользователя
    name = welcome_user()

    # Правила
    print('Find the greatest common divisor of given numbers.')

    # Счётчик
    n = 0

    # Игра, где нужно ответить 3 раза подряд правильно посчитать +-* двух числел
    while n < 3:
        # Обнуление ответа
        answer = 0
        # Генерация чисел с операцией и выяснение ответа пользователя
        number_one = randint(1, 100)
        number_two = randint(1, 100)
        user_answer = prompt.string(f"Question: {number_one} {number_two}\nYour answer: ")
    
        # Вычисление правильного ответа
        for i in range(1, min(number_one, number_two)):
            if number_one % i == 0 and number_two % i == 0:
                answer = i

        # Проверка
        if str(answer) == user_answer:
            print('Correct!')
            n += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'.\nLet's try again, {name}!")
            n = 0  # Обнуление счётчика

    # Победа
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()