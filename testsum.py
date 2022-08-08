import unittest

from my_sum import sum

class TestSum2(unittest.TestCase):
    
    def test_tuple_int(self):
        """
            AI is creating summary for test_tuple_int
        """
        data=(1,2,3)
        result=sum(data)
        self.assertEqual(result,6)


if __name__=='__main__':
    unittest.main()