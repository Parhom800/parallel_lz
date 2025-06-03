from multiprocessing import Process, Pipe
import random

# Генерация 
def generate(conn):
    count = random.randint(1, 1000)  
    numbers = [random.randint(-1000000, 1000000) for _ in range(count)]
    conn.send(numbers)  
    conn.close()
    print(f" process 1 generated {count} numbers")

# Возведение
def square(conn):
    numbers = conn.recv()
    squared = [x**2 for x in numbers]
    print(f"procces 2: \n{squared}")
    conn.close()

if __name__ == "__main__":
    read, write = Pipe()

    p1 = Process(target=generate, args=(write,))
    p2 = Process(target=square, args=(read,))

    p1.start()
    p2.start()

   
