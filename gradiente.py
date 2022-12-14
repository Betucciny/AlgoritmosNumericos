import numpy as np
from sympy import symbols, Matrix, solve

x, y, a = symbols('x y a')
ecuacion = x**2-24*x+y**2-10*y

sistema = Matrix([x, y])
grad = Matrix([ecuacion.diff(i) for i in sistema])


def main():
    global grad
    actual = [300, 200]

    while True:
        x0, y0 = actual
        direc = -grad.subs(x, x0).subs(y, y0)
        direc = [uni for uni in direc]
        dx, dy = direc

        mag = ecuacion.subs(x, x0+a*dx).subs(y, y0+a*dy)
        der = mag.diff(a)
        newa = solve(der, a)
        if len(newa) == 0:
            break
        newa = newa[0]
        nx, ny = x0 + newa*dx, y0 + newa*dy
        nuevos = [nx, ny]
        if error(actual, nuevos):
            print('Salida via error')
            break
        actual = nuevos

    print(actual)


def error(original, nuevo):
    e = np.subtract(original, nuevo)
    e = np.dot(e, e)
    if e > 0.0000001:
        return False
    return True


if __name__ == '__main__':
    main()

