from brain_games.cli import welcome_user
import prompt  # type: ignore

def main():
    # Приветствие и выеснение имени пользователя
    name = welcome_user()

    # Правила
    print('What is the result of the expression?')

    

if __name__ == "__main__":
    main()