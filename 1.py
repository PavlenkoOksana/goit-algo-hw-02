from queue import Queue


queue = Queue()
num_app = 1

def generate_request():
    global num_app
    queue.put(num_app)
    print (f"Надійшла нова заявка № {num_app} у роботу")
    num_app += 1


def process_request():
    if not queue.empty():
         current_application = queue.get()
         print(f"Обробляється заявка № {current_application}")
    else:
      print("Черга заявок порожня.")

try:
    while True:
        generate_request()
        process_request()
except KeyboardInterrupt:
    print("\nПрограма була перервана користувачем.")
    print("Програма завершила виконання.")

