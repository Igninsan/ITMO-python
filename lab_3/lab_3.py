# Вариант №6
# Root = 6; height = 5, left_leaf = (root*2)-2, right_leaf = root+4

def gen_bin_tree(root=6, height=5, left_leaf=lambda root: (root*2)-2, right_leaf=lambda root: root+4):
    """
    Функция, которая строит дерево по заданным параметрам (есть значения по умолчанию):
    root -> значение корня (самого первого числа)
    height -> высота дерева (глубина списка со словарями)
    left_leaf и right_leaf -> лямбда-функции - формулы для левой и правой ветки соответственно
    При корректном вводе данных возвращает словарь, состоящий из:
        {'значение корня': [{'результат формулы для левой ветки': [...]},{'результат формулы для правой ветки': [...]}]}
    При некорректном вводе данных, возвращает "None"
    """

    # Проверяем, являются ли корень и высота целыми числами
    if type(root) != int or type(height) != int:
        return None
    # Проверяем, являются ли левая и правая ветки (лямбда)функциями
    if type(left_leaf) != type(lambda: None) or type(right_leaf) != type(lambda: None):
        return None

    # Проверяем, равна ли высота дерева 0
    if height == 0:
        return {str(root): []}

    return {str(root): [gen_bin_tree(left_leaf(root), height - 1), gen_bin_tree(right_leaf(root), height - 1)]}
