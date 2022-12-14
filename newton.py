import numpy as np
from sympy import symbols, Matrix


x, y = symbols('x y')
val = Matrix([x, y])
ecc = [x**2-10*x+y**2+8, x*y**2+x-10*y+8]
ecc = Matrix(ecc)


def main():
    actual = [300, 500]
    while True:
        h = calc(actual)
        h = [a for lista in h for a in lista]
        nuevos = np.add(actual, h)
        if error(actual, nuevos):
            break
        actual = nuevos
    print(nuevos)


def error(original, nuevo):
    e = np.subtract(original, nuevo)
    e = np.dot(e, e)
    if e > 0.0000001:
        return False
    return True


def calc(iniciales):
    right = ecc * -1
    jac = ecc.jacobian(val)
    x0, y0 = iniciales
    matriz = jac.subs(x, x0).subs(y, y0)
    matriz = np.array(matriz.tolist()).astype(np.float64)
    r = right.subs(x, x0).subs(y, y0)
    r = np.array(r.tolist()).astype(np.float64)
    return np.linalg.solve(matriz, r)


if __name__ == '__main__':
    main()
