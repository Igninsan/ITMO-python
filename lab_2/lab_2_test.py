import unittest
import lab_2

class TestMath(unittest.TestCase):

    # Тесты для алгоритма медленного перебора:

    # Проверяется результат при корректном вводе данных
    def test_seq_normal(self):
        self.assertEqual(lab_2.guess_number(target=5, lst=[x for x in range(0, 51)], search_type='seq'), [5, 6])
    # Проверяется результат, при отсутствии искомого числа в списке
    def test_seq_target_not_found(self):
        self.assertEqual(lab_2.guess_number(target=11, lst=[x for x in range(0, 10)], search_type='seq'), None)
    # Проверяется результат, при наличии не целого числа в списке, до искомого числа
    def test_seq_not_int_in_list(self):
        self.assertEqual(lab_2.guess_number(target=3, lst=[0, 1, 2, 'a', 3, 4], search_type='seq'), None)
    # Проверяется результат, при вводе пустого списка
    def test_seq_empty_list(self):
        self.assertEqual(lab_2.guess_number(target=4, lst=[], search_type='seq'), None)
    # Проверяется результат, при наличии нескольких искомых чисел в списке
    def test_seq_many_targets_in_list(self):
        self.assertEqual(lab_2.guess_number(target=6, lst=[0, 1, 2, 3, 6, 5, 6, 4, 6], search_type='seq'), [6, 5])
    # Проверяется результат, при вводе не целого числа, в поле для искомого числа
    def test_seq_target_not_int(self):
        self.assertEqual(lab_2.guess_number(target='a', lst=[0, 1, 2, 3, 4, 5], search_type='seq'), None)


    # Тесты для алгоритма бинарного поиска:

    # Проверяется результат при корректном вводе данных
    def test_bin_normal(self):
        self.assertEqual(lab_2.guess_number(target=5, lst=[x for x in range(0, 51)], search_type='bin'), [5, 6])
    # Проверяется результат, при отсутствии искомого числа в списке
    def test_bin_target_not_found(self):
        self.assertEqual(lab_2.guess_number(target=11, lst=[x for x in range(0, 10)], search_type='bin'), None)
    # Проверяется результат, при наличии не целого числа в списке
    def test_bin_not_int_in_list(self):
        self.assertEqual(lab_2.guess_number(target=3, lst=[0, 1, 2, 'a', 3, 4], search_type='bin'), None)
    # Проверяется результат, при вводе пустого списка
    def test_bin_empty_list(self):
        self.assertEqual(lab_2.guess_number(target=4, lst=[], search_type='bin'), None)
    # Проверяется результат, при наличии нескольких искомых чисел в списке
    def test_bin_many_targets_in_list(self):
        self.assertEqual(lab_2.guess_number(target=6, lst=[0, 1, 2, 3, 6, 5, 6, 4, 6], search_type='bin'), [6, 2])
    # Проверяется результат, при вводе не целого числа, в поле для искомого числа
    def test_bin_target_not_int(self):
        self.assertEqual(lab_2.guess_number(target='a', lst=[0, 1, 2, 3, 4, 5], search_type='bin'), None)


if __name__ == '__main__':
    unittest.main()

