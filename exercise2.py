from multiprocessing import Process, Pipe
import random

# Генерация чисел
def generate(conn):
    count = random.randint(1, 1000)  # случайное количество чисел от 1 до 1000
    numbers = [random.randint(-1_000_000, 1_000_000) for _ in range(count)]
    conn.send(numbers)  # передаём список через Pipe
    conn.close()
    print(f"[p1] Сгенерировано {count} чисел.")

# Возведение
def square(conn):
    numbers = conn.recv()
    squared = [x**2 for x in numbers]
    print(f"[p2] Все квадраты:\n{squared}")
    conn.close()

    read, write = Pipe()

    # Создание процессов
    p1 = Process(target=generate, args=(write,))
    p2 = Process(target=square, args=(read,))

    # Запуск процессов
    p1.start()
    p2.start()

   
