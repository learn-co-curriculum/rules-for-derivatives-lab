import unittest
from ipynb.fs.full.index import (find_term_derivative, find_derivative, derivative_at,
tangent_line, derivative_function_trace)

class DerivativeRules(unittest.TestCase):
    def test_find_derivative_term(self):
        one_x_cubed = (1, 3)
        self.assertEqual(find_term_derivative(one_x_cubed), (3, 2))
        two_x_squared = (2, 2)
        self.assertEqual(find_term_derivative(two_x_squared), (4, 1))

    def test_find_derivative(self):
        first_terms = [(4, 3), (-3, 1)]
        self.assertEqual(find_derivative(first_terms), [(12, 2), (-3, 0)])
        second_terms = [(3, 2), (-11, 0)]
        self.assertEqual(find_derivative(second_terms), [(6, 1)])

    def test_derivative_at(self):
        second_terms = [(3, 2), (-11, 0)]
        self.assertEqual(derivative_at(second_terms, 2), 12)

    def test_tangent_line(self):
        second_terms = [(3, 2), (-11, 0)]
        self.assertEqual(tangent_line(second_terms, 5, line_length = 4), {'x': [1, 5, 9], 'y': [-56, 64, 184]})
        first_terms = [(4, 3), (-3, 1)]
        self.assertEqual(tangent_line(first_terms, 8, line_length = 3), {'x': [5, 8, 11], 'y': [-271, 2024, 4319]})

    def test_derivative_trace(self):
        second_terms = [(3, 2), (-11, 0)]
        x_values = list(range(-5, 5))
        second_terms_deriv_trace = {'x': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],
        'y': [-30, -24, -18, -12, -6, 0, 6, 12, 18, 24]}
        self.assertEqual(derivative_function_trace(second_terms, x_values), second_terms_deriv_trace)
