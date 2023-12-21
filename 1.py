from queue import Queue
import random


# Створити чергу заявок
queue = Queue()

# Функція generate_request(): Створити нову заявку та Додати заявку до черги

def generate_request():
    new_application = random.randint(1, 100)
    queue.put(new_application)
    print (f"Надійшла нова заявка № {new_application} у роботу")

# Функція process_request(): Якщо черга не пуста:
    #     Видалити заявку з черги
    #     Обробити заявку
    # Інакше:
    #     Вивести повідомлення, що черга пуста

def process_request():
    if not queue.empty():
         current_application = queue.get()
         print(f"Обробляється заявка № {current_application}")
    else:
      print("Черга заявок порожня.")

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявокuser_command = input("Введіть команду, для виходу виконайте end:")

user_command = input("Введіть команду, для виходу введіть end: \n")
while user_command != "end":
    generate_request()
    process_request()
    user_command = input("Введіть команду, для виходу введіть end: \n")

print ("Програма завершила виконання")

