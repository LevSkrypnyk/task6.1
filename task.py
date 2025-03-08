# Функція для роботи зі списком
def process_list():
    # Введення списку
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()
    
    # Виведення списку у зворотному порядку
    reversed_list = lst[::-1]
    print("Список у зворотному порядку:", reversed_list)
    
    # Визначення кількості елементів у списку
    count = len(lst)
    print("Кількість елементів у списку:", count)

# Виконання функції
process_list()