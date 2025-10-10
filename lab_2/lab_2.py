def main():
    target = int(input('Введите число для поиска: '))
    is_range = bool(input('Хотите ввести диапазон для создания списка? Если нет -> пропустите ввод: '))
    search_type = input("Введите тип поиска числа:\n'seq' -> медленный перебор\n'bin' -> бинарный поиск\n")

    if is_range:
        first_range = int(input('Введите начало диапазона: '))
        second_range = int(input('Введите конец диапазона: '))
        lst = list(range(first_range, second_range + 1))

    else:
        str_lst = input('Введите список с числами (Пример ввода: 1, 2, 3, 4, 5)\n')
        try:
            lst = [int(x) for x in str_lst.split(', ')]
        except:
            raise Exception('Вы ввели список, содержащий не число или неверно ввели список')

    result = guess_number(target, lst, search_type)

    print(f'{result}')

def guess_number(target: int, lst: list[int], search_type: str) -> list[int] or str:
    """
    Функция, которая ищет число в заданном списке. Имеет 2 варианта поиска:
        1)алгоритм медленного перебора -> seq.
        2)алгоритм бинарного поиска -> bin.
    При корректном вводе данных возвращает список из 2 элементов, в котором:
        Первый элемент - искомое число.
        Второй элемент - количество шагов сделанных для поиска числа
    При некорректном вводе данных -> возвращает None
        """

    # None -> Какая-либо ошибка (Например: искомого числа нет в списке, искомое число имеет не тот тип данных и т.п.)
    step = 0

    # Проверяем есть ли искомое число в заданном списке
    if target not in lst:
        return None

    if search_type == 'seq':
        # Проверяем является ли искомое число целым значением
        if type(target) != int:
            return None

        for number in lst:
            step += 1
            # Проверяем является ли текущий элемент списка целым числом
            if type(number) != int:
                return None

            if number == target:
                return [number, step]


    elif search_type == 'bin':

        # Пробуем отсортировать список, если не получается (например: разные типы данных в списке -> возвращаем None)
        try:
            lst.sort()
        except:
            return None

        # Сортируем список, чтобы выборка правильно работала
        lst.sort()

        while True:
            step += 1
            lst_length = len(lst)
            middle_index = lst_length // 2
            middle_number = lst[middle_index]

            # Проверяем является ли среднее число целым
            if type(middle_number) != int:
                return None
            # Сравниваем среднее число с искомым и в зависимости от результата, сужаем поиск (или выдаём само число)
            if middle_number == target:
                return [middle_number, step]

            elif middle_number > target:
                lst = lst[:middle_index]

            elif middle_number < target:
                lst = lst[middle_index:]

            else:
                return None

    else:
        return None

if __name__ == '__main__':
    main()
