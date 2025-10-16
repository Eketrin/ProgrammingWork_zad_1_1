import random

# Создаем игровое поле
box = []
for i in range(1, 17):
    if i == 16:
        box.append(0)  # пустая клетка
    else:
        box.append(i)

# Перемешиваем костяшки
random.shuffle(box)

# Находим где пустая клетка
null_pozit = 0
for i in range(16):
    if box[i] == 0:
        null_pozit = i


# Функция для отображения поля
def show_box():
    print("\n" + "-" * 20)
    for i in range(4):
        for j in range(4):
            index = i * 4 + j
            if box[index] == 0:
                print("   ", end=" ")  # пустая клетка
            else:
                print(f"{box[index]:2} ", end=" ")
        print()
    print("-" * 20)


# Функция для проверки победы
def check_win():
    # Проверяем, все ли числа на своих местах
    for i in range(15):
        if box[i] != i + 1:
            return False
    return box[15] == 0


# Функция для движения костяшек
def movement(direction):
    u = 0
# в процессе


# Основная игра
print("--- ПЯТНАШКИ ---")
print("Нужно расставить числа по порядку от 1 до 15")
print("Управление:")
print("w - вверх")
print("s - вниз")
print("a - влево")
print("d - вправо")
print("q - выход")

score = 0

while True:
    show_box()
    score += 1

    # Проверяем победу
    if check_win():
        print(f"Вы выиграли за {score} ходов")
        break

    # Получаем ход от игрока
    hod = input("\nВведите направление (w/a/s/d): ").lower()

    if hod == "q":
        print("Игра окончена")
        break
    elif hod in ["w", "a", "s", "d"]:
        # Пытаемся сделать ход
        if movement(hod):
            print(f"Ход {score} выполнен!")
        else:
            score -= 1  # если ход не удался, не считаем его
    else:
        print("Неправильная команда! Используйте w/a/s/d или q для выхода")
        score -= 1