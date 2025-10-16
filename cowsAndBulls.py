

# Это логическая игра. В ходе неё игрок за несколько попыток должен. понять, 
# что загадал соперник (это могут быть числа, символы, слова и так далее). 
# После каждой попытки задумавший игрок выставляет «оценку»: 
# сколько букв/цифр/символов угадано без совпадения с позициями (то есть показывает количество «коров») 
# и сколько угадано точно, вместе с расположением (то есть показывает количество «быков»).

import random

# генерирует 4 цифры
def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

# быки и коровы
def count_bulls_cows(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

# проверка пользователя
def is_correct(guess):
    if len(guess) != 4:
        return False
    if not guess.isdigit():
        return False
    if len(set(guess)) != 4:  # все цифры должны быть разными
        return False
    return True


def main():
    print("Быки - правильные цифры на правильных местах")
    print("Коровы - правильные цифры на неправильных местах")
    print("-" * 50)

    secret = generate_secret()
    score = 0
    print(f"{secret} - загаданное число, выводится для проверки программы")
    while True:
        guess = input("Введите вашу догадку (4 разные цифры): ").strip() #чистим пробелы

        if not is_correct(guess): #если пользователь ввёл неправильный формат и тп
            print("Некорректный ввод!")
            continue

        score += 1
        bulls, cows = count_bulls_cows(secret, guess)

        print(f"Результат: {bulls} быков, {cows} коров")

        if bulls == 4:
            print(f"Поздравляю! Вы угадали число {secret} за {score} попыток!")
            break


main()




