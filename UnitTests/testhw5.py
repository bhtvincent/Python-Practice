import unittest
import hw4

class TestQ1(unittest.TestCase):

    def setUp(self):
        """
        Sets up the variables used in test case top_students, extra_credit,
        and adjusted_grade
        :return: nothing
        """
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}
        self.iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                'Bryan': 2, 'Andrea': 110}
        self.exam = exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
            'Bryan': 95, 'Andrea': 86}

    def test_top_students(self):
        """
        Tests top_students function
        """
        self.assertEqual(hw4.top_students(self.cs122,2),['Anna', 'Alex'])
        self.assertEqual(hw4.top_students(self.cs122),['Anna', 'Alex', 'Zoe'])
        self.assertEqual(hw4.top_students(self.cs122,10),['Anna', 'Alex', 'Zoe', 'Dan'])
        self.assertEqual(hw4.top_students(self.empty_class),[])

    def test_extra_credit(self):
        """
        Tests extra_credit function
        """
        self.assertEqual(hw4.extra_credit(self.cs122),{'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101})
        self.assertEqual(hw4.extra_credit(self.cs122,2), {'Zoe':92, 'Alex': 95, 'Dan':81, 'Anna':102})
        self.assertEqual(hw4.extra_credit(self.empty_class,5),{})

    def test_adjusted_grade(self):
        """
        Tests adjusted_credit function
        """
        self.assertEqual(hw4.adjusted_grade(self.iclicker,self.exam),{'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96, 'Ryan': 90, 'Andrea': 87, 'Dan': 89})
        self.assertEqual(hw4.adjusted_grade(self.empty_class,self.exam),{'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64, 'Dan': 89, 'Alex': 95})
        self.assertEqual(hw4.adjusted_grade(self.iclicker,self.empty_class),{'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0, 'Anna': 1, 'Alex': 1})
        self.assertEqual(hw4.adjusted_grade(self.empty_class,self.empty_class), self.empty_class)

    def test_sum_of_inverse_odd(self):
        self.assertEqual(hw4.sum_of_inverse_odd(0),0)
        self.assertEqual(hw4.sum_of_inverse_odd(1),1.0)

    def test_same_length(self):
        self.assertEqual(hw4.same_length(), True)
        self.assertEqual(hw4.same_length('hi', 'ha', 'it', 'quiet'), False)
        self.assertEqual(hw4.same_length('hi', 'ha', 'it'), True)
        self.assertEqual(hw4.same_length('hello', 'ha', 'it', 'ok'), False)
        self.assertEqual(hw4.same_length('Spartan'), True)

if __name__ == '__main__':
    unittest.main()