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
            collumn.append('#') # добавляется мертвая клетка
        else:
            collumn.append('') # добавляется живая клетка
    nextCells.append(collumn)
    