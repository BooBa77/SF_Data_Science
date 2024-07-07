def guess_my_num(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число

    Returns:
        int: Число попыток, затраченное на угадывание
    """
    count = 1 # кол-во попыток
    predict = 50 # предполагаемое число

    """
    Угадывать число будем, пользуясь подсказкой "больше/меьше", 
    начиная с середины, т.е. 50,
    смещаясь в предполжении на половину оставшего диапозона.
    И он, с свою очередь, уменьшается с каждой попыткой в два раза,
    или по формуле 100 / 2^count
    """

    while number != predict:
        count += 1
        if number > predict:
            predict = predict + int(100 / (2**count)) + 1
        elif number < predict:
            predict = predict - int(100 / (2**count)) - 1

    return count
    
import numpy as np
count_attempts = 0 # общее кол-во попыток отгадывания
for i in range(10000):
    hidden_number = np.random.randint(1, 101)  # загаданное компьютером число
    count_attempts += guess_my_num(hidden_number)

# вывод на экран среднего количества попыток
print(f'10000 чисел отгадано в среднем за ' + str(round(count_attempts / 10000, 2)) + ' попыток')