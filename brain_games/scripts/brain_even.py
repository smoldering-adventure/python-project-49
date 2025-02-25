from random import random

import prompt  # type: ignore

# Приветствие и выеснение имени пользователя
print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print("Hello, " + name + "!")

# Правила
print('Answer "yes" if the number is even, otherwise answer "no".')

n = 0

# Игра, где нужно ответить 3 раза подряд правильно определить чётность
while n < 3:
    # Генерация числа и выяснение ответа пользователя
    number = random()
    user_answer = prompt.string(f"Question: {number}\nYour answer: ")
    
    # Определение чётности
    if number // 2 == 0:
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
        n = 0  # Обнуление счётчика

# Победа
print(f"Congratulations, {name}!")