print("Добро пожаловать в калькулятор!")

while True:
    text = input("Введи первое число (или 'q' для выхода): ")
    if text == "q":
        print("Всего хорошего!")
        break
    try:
        a = float(text)
        b = float(input("Введи второе число: "))
    except ValueError:
        print("Нужно ввести число!")
        continue
    c = input("Введи действие '+, -, *, /': ")
    
    if c == "+":
        res = a + b
        print(f"Результат: {res}")
    elif c == "-":
        res = a - b
        print(f"Результат: {res}")
    elif c == "*":
        res = a * b
        print(f"Результат: {res}")
    elif c == "/":
        if b == 0:
            print("Ошибка, на 0 делить нельзя!")
        else:
            res = a / b
            print(f"Результат: {res}")
    else:
        print("Неизвестное действие")