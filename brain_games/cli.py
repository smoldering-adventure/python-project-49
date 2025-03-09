import prompt  # type: ignore

def welcome_user():
    # Приветствие и выеснение имени пользователя
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name
