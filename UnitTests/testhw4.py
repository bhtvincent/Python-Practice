# ----------------------------------------------------------------------
# Name: testhw4.py
# Purpose: Practice unittest
#
# Date: 2019-03-09
# ----------------------------------------------------------------------
"""
Test all the functions in homework4
"""

import unittest
import hw4 as hw4


class TestQ1(unittest.TestCase):
    """
    Test case for the normal execution of top_students function
    """

    def setUp(self):
        """
        Create dictionary for testing
        :return: None
        """
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_top_students_default(self):
        """
        Test the top_students function default parameter
        :return: None
        """
        self.assertEqual(hw4.top_students(self.cs122),
                         ['Anna', 'Alex', 'Zoe'])

    def test_top_students_empty(self):
        """
        Test the top_students function with empty dictionary
        :return: None
        """
        self.assertEqual(hw4.top_students(self.empty_class, 6), [])

    def test_top_students_2(self):
        """
        Test the top_students function with n=2
        :return: None
        """
        self.assertEqual(hw4.top_students(self.cs122, 2),
                         ['Anna', 'Alex'])

    def test_top_students_10(self):
        """
        Test the top_students function with n=10
        :return: None
        """
        self.assertEqual(hw4.top_students(self.cs122, 10),
                         ['Anna', 'Alex', 'Zoe', 'Dan'])


class TestQ2(unittest.TestCase):
    """
    Test case for the normal execution of extra_credit function
    """

    def setUp(self):
        """
        Create dictionary for testing
        :return: None
        """
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_extra_credit_default(self):
        """
        Test the extra_credit function default parameter
        :return: None
        """
        self.assertEqual(hw4.extra_credit(self.cs122),
                         {'Zoe': 91, 'Alex': 94,
                          'Dan': 80, 'Anna': 101})

    def test_extra_credit_empty(self):
        """
        Test the extra_credit function with empty dictionary
        :return: None
        """
        self.assertEqual(hw4.extra_credit(self.empty_class, 5), {})

    def test_extra_credit_2(self):
        """
        Test the extra_credit function with n=2
        :return: None
        """
        self.assertEqual(hw4.extra_credit(self.cs122, 2),
                         {'Zoe': 92, 'Alex': 95,
                          'Dan': 81, 'Anna': 102})


class TestQ3(unittest.TestCase):
    """
    Test case for the normal execution of adjust_grade function
    """

    def setUp(self):
        """
        Create dictionary for testing
        :return: None
        """
        self.iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100,
                         'Anna': 110, 'Bryan': 2, 'Andrea': 110}
        self.exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
                     'Bryan': 95, 'Andrea': 86}

    def test_adjust_grade_normal(self):
        """
        Test the adjust_grade with normal parameter
        :return: None
        """
        self.assertEqual(hw4.adjusted_grade(self.iclicker, self.exam),
                         {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96,
                          'Ryan': 90, 'Andrea': 87, 'Dan': 89})

    def test_adjust_grade_empty(self):
        """
        Test the adjust_grade with empty parameter
        :return: None
        """
        self.assertEqual(hw4.adjusted_grade({}, {}), {})

    def test_adjust_grade_iclicker(self):
        """
        Test the adjust_grade with only iclicker
        :return: None
        """
        self.assertEqual(hw4.adjusted_grade(self.iclicker, {}),
                         {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0,
                          'Anna': 1, 'Alex': 1})

    def test_adjust_grade_exam(self):
        """
        Test the adjust_grade with only exam
        :return: None
        """
        self.assertEqual(hw4.adjusted_grade({}, self.exam),
                         {'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64,
                          'Dan': 89, 'Alex': 95})


class TestQ4(unittest.TestCase):
    """
    Test case for the normal execution of sum_of_inverse_odd function
    """

    def test_sum_of_inverse_odd_0(self):
        """
        Test the sum_of_inverse_odd with 0 as parameter
        :return: None
        """
        self.assertEqual(hw4.sum_of_inverse_odd(0), 0)

    def test_sum_of_inverse_odd_1(self):
        """
        Test the sum_of_inverse_odd with 1 as parameter
        :return: None
        """
        self.assertEqual(hw4.sum_of_inverse_odd(1), 1)

    def test_sum_of_inverse_odd_2(self):
        """
        Test the sum_of_inverse_odd with 2 as parameter
        :return: None
        """
        self.assertEqual(hw4.sum_of_inverse_odd(2), 1)

    def test_sum_of_inverse_odd_3(self):
        """
        Test the sum_of_inverse_odd with 3 as parameter
        :return: None
        """
        self.assertEqual(hw4.sum_of_inverse_odd(3), 1.3333333333333333)

    def test_sum_of_inverse_odd_2000(self):
        """
        Test the sum_of_inverse_odd with 2000 as parameter
        :return: None
        """
        self.assertEqual(hw4.sum_of_inverse_odd(2000),
                         4.435632673335106)


class TestQ5(unittest.TestCase):
    """
    Test case for the normal execution of same_length function
    """

    def test_same_length_empty(self):
        """
        Test the same_length with empty parameter
        :return: None
        """
        self.assertTrue(hw4.same_length())

    def test_same_length_examples(self):
        """
        Test the same_length with some examples
        :return: None
        """
        self.assertFalse(hw4.same_length('hi', 'ha', 'it', 'quiet'))
        self.assertTrue(hw4.same_length('hi', 'ha', 'it'))
        self.assertFalse(hw4.same_length('hello', 'ha', 'it', 'ok'))
        self.assertTrue(hw4.same_length('Spartan'))


