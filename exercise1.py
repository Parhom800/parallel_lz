import requests
import threading
import time

urls = [
        "https://example.net", 
        "https://www.microsoft.com/ru-ru", 
        "https://www.apple.com", 
        "https://www.python.org", 
        "https://www.window-swap.com",
        "https://trypap.com/",
        "https://pointerpointer.com/",
        "https://app.radiooooo.com/",
        "https://www.mapcrunch.com/",
        "https://chatgpt.com",
        ]

# Загрузка одной страницы
def download(url):
    response = requests.get(url)
    print(f"Downloaded {url} (size: {len(response.content)} bytes)")

# Последовательно
def sequential_download(urls):
    print("\nSequential download started...")
    start = time.time()
    for url in urls:
        download(url)
    duration = time.time() - start
    print(f"Sequential download completed in {duration:.2f} seconds\n")
    return duration

# Параллельно
def threaded_download(urls):
    print("Threaded download started...")
    start = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time.time() - start
    print(f"Threaded download completed in {duration:.2f} seconds\n")
    return duration

if __name__ == "__main__":
    seq_time = sequential_download(urls)
    thread_time = threaded_download(urls)

    print("=== Comparison ===")
    if seq_time > thread_time:
        print("Результат: многопоточная загрузка быстрее.")
    elif seq_time < thread_time:
        print("Результат: последовательная загрузка быстрее.")
    else:
        print("Результат: время одинаковое.")