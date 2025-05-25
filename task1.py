from queue import Queue
import time

request_queue = Queue()
request_id = 1

def generate_request():
    global request_id
    request = f"Заявка №{request_id}"
    request_queue.put(request)
    print(f"[+] Додано: {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[-] Оброблено: {request}")
    else:
        print("Черга порожня. Немає заявок для обробки.")

for _ in range(5):
    generate_request()
    time.sleep(0.5)
    process_request()
    time.sleep(0.5)