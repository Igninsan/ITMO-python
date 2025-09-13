import unittest
import lab_1

class TestMath(unittest.TestCase):

    # проверяется тест 1 (с сайта)
    def test_1(self):
        self.assertEqual(lab_1.find_sum(nums = [2,7,11,15], target = 9), [0, 1], 'bug in test_1')

    # проверяется тест 2 (с сайта)
    def test_2(self):
        self.assertEqual(lab_1.find_sum(nums = [3,2,4], target = 6), [1, 2], 'bug in test_2')

    # проверяется тест 3 (с сайта)
    def test_3(self):
        self.assertEqual(lab_1.find_sum(nums = [3,3], target = 6), [0, 1], 'bug in test_3')

    # проверяется случай с элементом списка не типа данных int
    def test_not_int(self):
        self.assertIsNone(lab_1.find_sum(nums = ['1', 2, 3, 4, 5], target = 6), 'bug in test_not_int')

    # проверяется случай с nums не типа данных list
    def test_nums_not_list(self):
        self.assertIsNone(lab_1.find_sum(nums = (1, 2, 3, 4, 5), target = 6), 'bug in test_not_list')

    # проверяется случай с target не типа данных int
    def test_target_not_int(self):
        self.assertIsNone(lab_1.find_sum(nums = (1, 2, 3, 4, 5), target = 6.5), 'bug in test_not_list')

    # проверяется случай с несколькими правильными ответами
    def test_many_answers(self):
        self.assertEqual(lab_1.find_sum(nums = [1, 2, 3, 4, 1, 5, 2, 1], target = 6), [0, 5], 'bug in test_many_answers')

    # проверяется случай без правильного ответа
    def test_no_answers(self):
        self.assertIsNone(lab_1.find_sum(nums = [1, 2, 4, 7, 13], target = 16), 'bug in test_no_answers')

    # проверяется случай с одним элементов в списке
    def test_one_number(self):
        self.assertIsNone(lab_1.find_sum(nums = [3], target = 6), 'bug in test_one_number')


if __name__ == '__main__':
    unittest.main()

