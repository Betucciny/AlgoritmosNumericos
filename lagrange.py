import numpy as np
from sympy import symbols, Matrix, solve

x, y, la = symbols('x y l')
f = x*y
g = 4*x**2+8*y**2-16
sistema = Matrix([x, y])
lagrange = f - la*g


def main():
    gradf = Matrix([f.diff(i) for i in sistema])
    gradg = Matrix([g.diff(i) for i in sistema])
    lamb1 = solve(gradf[0]-la*gradg[0], la)
    lamb2 = solve(gradf[1] - la * gradg[1], la)
    newx = [solve(l1-l2, x) for l1, l2 in zip(lamb1, lamb2)]
    newx = [j for i in newx for j in i]
    print(newx)








if __name__ == '__main__':
    main()
