def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Ошибка")
    return number
def checkNumber(num):
    if  num <= 1:
        print("X => 0, Y => 0")
    elif 1 < num <= 2:
        print("X <= 0, Y => 0")
    elif 2 < num <= 3:
        print("X <= 0, Y <= 0")
    elif 3 < num <= 4:
        print("X => 0, Y <= 0")
    else:
        print("Число не является номером координатной четверти")
num = InputNumbers("Введите номер координатной четверти: ")
checkNumber(num)