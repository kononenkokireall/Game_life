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
    print('/n, /n, /n, /n, /n') # Отделение каждого шага клетки в игре.
    currentCells = copy.deepcopy(nextCells)
    for x in range(HEIGHT):
        for y in range(WIDTH):
            print(currentCells[x],[y], end='') # Вывод решетки.
        print() # Вывод символа новой строки в конце.
        # Вычисление клеток следующего шага
        # на основе текущего шага.
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Выражение '% WIDTH’ гарантирует, что значение
                # leftCoord всегда находится между 0 и WIDTH - 1
                left_cords = (x - 1) % WIDTH
                right_cords = (x + 1) % WIDTH
                above_cords = (y - 1) % HEIGHT
                belou_cords = (y + 1) % HEIGHT
                # Вычисление количества живых соседних клеток.
                NUM_NEIGHBORS = 0
                if currentCells[left_cords][above_cords] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка с верху, слева
                if currentCells[x][above_cords] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка с верху
                if currentCells[right_cords][above_cords] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка с верху, с права
                if currentCells[left_cords][y] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка слева
                if currentCells[right_cords][y] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка с права
                if currentCells[left_cords][belou_cords] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка слева снизу
                if currentCells[x][belou_cords] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка снизу
                if currentCells[right_cords][belou_cords] == '#':
                    NUM_NEIGHBORS += 1
                    # жива соседняя клетка с права снизу
                
