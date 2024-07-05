def guess_my_num(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток, затраченное на угадывание
    """
    count = 1
    predict = 50

    while number != predict:
        count += 1
        if number > predict:
            predict = predict + int((100-1) / (2**count)) + 1
        elif number < predict:
            predict = predict - int((100-1) / (2**count)) - 1

    return count
    
for i in range(101):
    print(f'{i} отгадано с ' + str(game_core_v3(i)) + ' попыток')