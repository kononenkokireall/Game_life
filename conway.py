# Игра Жизьнь.
import random, copy, time
# Глобальные переменные (Ширина, Длина)
WIDTH = 60
HEIGHT = 20
# Cоздание списка списков для клеток
nextCells = []
for x in range(WIDTH):
    collumn = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            collumn.append('#') # добавляется Живая клетка
        else:
            collumn.append('') # добавляется Мертвая клетка
    nextCells.append(collumn) # val(nextCells) - содержыт список столбцов
# Основной цыкл игры.
while True:
    print('/n, /n, /n, /n, /n') # Отделение каждого шага клетки.
currentCells = copy.deepcopy(nextCells)
