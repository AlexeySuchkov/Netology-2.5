import os
import datetime
import time
from pprint import pprint
import random
# Добавление менеджера контекста к заданию 2.4
class ContextManagerTimes:
    def __init__(self, path_to_file):
        print("Запуск менеджера контекста")
        self.start = datetime.datetime.now()
        self.start_sec = time.time()
        self.path = path_to_file

    def __enter__(self):
        print(f"Начало работы {self.start}")
        self.file = open(self.path, "a")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        self.end_sec = time.time()
        duration = round(self.end_sec - self.start_sec)
        print(f"Завершение программы {self.end}")
        print(f"Общее время выполнения программы {duration} секунд")
        print("Выход из менеджера контекста")
        self.file.close()




# Чтение из файла
path_to_file = "./recipes.txt"
with ContextManagerTimes(path_to_file) as file:
 def read_file(path_to_file):
    cook_book = {}
    with open(path_to_file, 'r', encoding = "utf-8") as f:
        for line in f:
            if line.strip().isdigit():
                quantity = int(line)
            elif line.strip().find("|") == -1 and line.strip():
                name = line.strip().lower()
                cook_book[name] = []
            elif line.strip().find("|") != -1:
                ingredients = line.strip().split("|")
                list_ingredients = {"ingredient_name": ingredients[0], "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(list_ingredients)
    return cook_book


# Создание списка
 def get_shop_list_by_dishes(dishes_list, count):
    path_to_file = "./recipes.txt"
    cook_book = read_file(path_to_file)
    shopping_list = {}
    for dish in dishes_list:
        if dish not in cook_book:
            pass
        else:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shopping_list:
                    shopping_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                    'quantity': ingredient['quantity'] * count}
                else:
                    all_amount = shopping_list[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * count
                    shopping_list[ingredient['ingredient_name']]['quantity'] = all_amount
    if shopping_list:
        pprint(shopping_list)
        return shopping_list
    else:
        print("Введенного блюда нет в списке")


# Получение данных для программы
 def start_program():
    dishes_list = []
    while True:
        dish = input("Введите название блюда (Омлет, Утка по-пекински, Запеченый картофель, Фахитос) "
                     "или нажмите ENTER для завершения ввода блюд: ")
        if not dish:
            person_count = int(input("Введите количество персон: "))
            get_shop_list_by_dishes(dishes_list, person_count)
            break
        else:
            dishes_list.append(dish.lower())


 start_program()