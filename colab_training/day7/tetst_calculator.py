import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(3,8)
        self.assertEqual(result, 11)
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(17,2)
        self.assertEqual(result, 34)
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

# 수학 함수 테스트
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

# 문자열 반전 함수 테스트
class TestStringFunction(unittest.TestCase):
    def test_reverse_string(self):
        result = reverse_string("hello")
        self.assertEqual(result, 'olleh')

# 리스트 정렬 함수
class TestListFunction(unittest.TestCase):
    def test_sort_list(self):
        result = sort_list(['찬희', '윤아', '현수', '신혁'])
        self.assertEqual(result, ['신혁','윤아', '찬희', '현수'])

# 사용자 정의 클래스 메서드 테스트
class TestPersonClass(unittest.TestCase):
    def test_is_adult(self):
        with self.asserRaises(ValueError):
            divide_new(10,0)

#파일 처리 함수 테스트
class TestFileOperation(unittest.TestCase):
    def test_write_to_file(self):
        write_to_file("test.txt","hello world")
        with open("test.txt","r")as f:
            self.assertEqualt(f.read(),"hello world")


if __name__=="__main__":
    unittest.main
