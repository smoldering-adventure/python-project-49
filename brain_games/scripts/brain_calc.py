from random import randint, choice
import prompt  # type: ignore
from brain_games.cli import welcome_user

def main():
    # Приветствие и выеснение имени пользователя
    name = welcome_user()

    # Правила
    print('What is the result of the expression?')

    # Счётчик и арефмитические опирации
    n = 0
    operators = ['+', '-', '*']

    # Игра, где нужно ответить 3 раза подряд правильно посчитать +-* двух числел
    while n < 3:
        # Генерация чисел с операцией и выяснение ответа пользователя
        number_one = randint(1, 100)
        number_two = randint(1, 100)
        random_operator = choice(operators)
        user_answer = prompt.string(f"Question: {number_one} {random_operator} {number_two}\nYour answer: ")
    
        # Вычисление правильного ответа
        if random_operator == '+':
            answer = number_one + number_two
        elif random_operator == '-':
            answer = number_one - number_two
        else:
            answer = number_one * number_two

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