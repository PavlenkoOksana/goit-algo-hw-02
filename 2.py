from collections import deque

def is_palindrome(s):
    # Прибираємо пробіли та переводимо рядок до нижнього регістру
    s = s.replace(" ", "").lower()
    
    # Ініціалізуємо чергу (deque)
    string_queue = deque()
    
    # Додаємо символи рядка до черги
    for char in s:
        string_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги для перевірки паліндрома
    while len(string_queue) > 1:
        if string_queue.popleft() != string_queue.pop():
            return False
    
    return True

input_string = input ("Введіть рядок: \n")
result = is_palindrome(input_string)

if result:
    print(f'Рядок "{input_string}" є паліндромом.')
else:
    print(f'Рядок "{input_string}" не є паліндромом.')