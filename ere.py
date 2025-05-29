import requests
import threading

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

def download(url):
        response = requests.get(url)
        print(f"Загружена {url}, размер: {len(response.content)} байт")

threads = []

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

 




