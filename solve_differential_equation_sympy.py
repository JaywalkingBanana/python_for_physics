from sympy.interactive import printing
printing.init_printing(use_latex = True)
from sympy import *
import sympy as sp

x = sp.symbols('x')
f = sp.Function('f')(x)

diffeq = Eq(f.diff(x, x) - 5 * f, 0)
display(diffeq)

dsolve(diffeq, f)
