# This moudle is an implementation of Lagrange polynomial
# It was neglected due to lack of univalentsy(חד-ערכיות) in the given csv elements

import numpy # Was seppose to optimise calculations but was not implemented in the end.
# NumPy allows operations on arrays directly, eliminating the need for explicit loops. 
# This results in faster computation due to optimized low-level implementations.

def calc_numerator(xs, input_x, current_x):
    """Calculate the numerator for the Lagrange basis polynomial."""
    product = 1
    for x in xs:
        if x != current_x:
            product *= (input_x - x)
    return product


def calc_denominator(xs, current_x):
    """Calculate the denominator for the Lagrange basis polynomial."""
    product = 1
    for x in xs:
        if x != current_x:
            product *= (current_x - x)
    return product

class Polynomial:
    """Lagrange basis polynomial."""
    def __init__(self, xs, current_x): #xs is all the xs
        self.xs = xs
        self.current_x = current_x
        self.denominator = calc_denominator(xs, current_x)

    def p(self, input_x):
        """Evaluate the basis polynomial at a given input_x."""
        if input_x == self.current_x: return 1
        if input_x in self.xs: return 0
        return calc_numerator(self.xs, self.current_x, input_x)/self.denominator

def build_polynoms(xs):
    """Build all basis polynomials for the given x values."""
    arr = list()
    for x in xs:
        arr.append(Polynomial(xs,x))
    return arr


class Lagrange:
    """Lagrange polynomial interpolator."""
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.polynoms = build_polynoms(xs)
    
    def p(self, input_x):
        """Evaluate the Lagrange polynomial at a given target_x."""
        sum = 0
        for polynomial, y in zip(self.polynomials, self.ys):
            sum += (polynomial.p(input_x) * y)
        return sum