#напишите программу для бинарного поиска загаданно

#user_num = int(input("Введите целое число от 1 до 100: "))

def binary_search(min_num, max_num):
    #min_num = 0
    #max_num = 100
    center = (min_num + max_num) // 2

    while True:
        print(f"Ваше число {center}?")
        check = input("Если больше > , если меньше < , если равно = ")

        if check == ">":
            min_num = center
            center = (min_num + max_num) // 2
        
        elif check == "<":
            max_num = center
            center = (min_num + max_num) // 2

        elif check == "=":
            print(f"Я угадал!")
            break
        else:
            print("Я не знаю это число")

binary_search(int(input("минимальное число "), int(input("максимальное число "))))
